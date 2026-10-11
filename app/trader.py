import time

from app.market_data import get_klines, get_current_price
from app.strategy import generate_signal
from app.config import (
    SYMBOL,
    RISK_PERCENT,
    STOP_LOSS_PERCENT,
    TAKE_PROFIT_PERCENT,
    PAPER_MODE,
    INITIAL_USDT,
)


class PaperPortfolio:
    def __init__(self, initial_usdt=INITIAL_USDT):
        self.usdt = initial_usdt
        self.position_qty = 0.0
        self.entry_price = None
        self.total_trades = 0

    def buy(self, price):
        if self.position_qty > 0:
            return

        risk_amount = self.usdt * (RISK_PERCENT / 100)
        qty = risk_amount / price

        self.position_qty = qty
        self.entry_price = price
        self.usdt -= qty * price
        self.total_trades += 1
        print(f"[BUY] {qty:.6f} {SYMBOL} @ {price:.4f}")

    def sell(self, price):
        if self.position_qty <= 0:
            return

        pnl = (price - self.entry_price) * self.position_qty
        self.usdt += self.position_qty * price
        self.position_qty = 0
        self.entry_price = None

        print(f"[SELL] @ {price:.4f} | PnL: {pnl:.4f} USDT")

    def check_risk(self, price):
        if self.entry_price is None:
            return

        change = ((price - self.entry_price) / self.entry_price) * 100

        if change <= -STOP_LOSS_PERCENT:
            print(f"[STOP LOSS] change={change:.2f}%")
            self.sell(price)
        elif change >= TAKE_PROFIT_PERCENT:
            print(f"[TAKE PROFIT] change={change:.2f}%")
            self.sell(price)


class TraderBot:
    def __init__(self, paper_mode=PAPER_MODE):
        self.paper_mode = paper_mode
        self.portfolio = PaperPortfolio()

    def run_once(self):
        df = get_klines()
        signal = generate_signal(df)
        price = get_current_price()

        print(f"Signal={signal} | Prix={price:.4f} | USDT={self.portfolio.usdt:.2f}")

        if signal == 1:
            self.portfolio.buy(price)
        elif signal == -1:
            self.portfolio.sell(price)

        self.portfolio.check_risk(price)

    def run_forever(self, interval_seconds=30):
        while True:
            try:
                self.run_once()
                time.sleep(interval_seconds)
            except Exception as exc:
                print(f"[ERREUR] {exc}")
                time.sleep(interval_seconds)
