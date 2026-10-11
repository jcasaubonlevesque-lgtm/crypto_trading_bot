import time

from app.market_data import get_klines, get_current_price
from app.strategy import generate_signal
from app.config import (
    SYMBOLS,
    PRIMARY_SYMBOL,
    RISK_PERCENT,
    STOP_LOSS_PERCENT,
    TAKE_PROFIT_PERCENT,
    PAPER_MODE,
    INITIAL_USDT,
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
)
from app.notifications import send_telegram_message


class PaperPortfolio:
    def __init__(self, initial_usdt=INITIAL_USDT):
        self.usdt = initial_usdt
        self.position_qty = 0.0
        self.entry_price = None
        self.total_trades = 0
        self.winning_trades = 0
        self.losing_trades = 0

    def buy(self, price, symbol=PRIMARY_SYMBOL):
        if self.position_qty > 0:
            return

        risk_amount = self.usdt * (RISK_PERCENT / 100)
        qty = risk_amount / price

        self.position_qty = qty
        self.entry_price = price
        self.usdt -= qty * price
        self.total_trades += 1
        print(f"[BUY] {qty:.6f} {symbol} @ {price:.4f}")

    def sell(self, price, symbol=PRIMARY_SYMBOL):
        if self.position_qty <= 0:
            return

        pnl = (price - self.entry_price) * self.position_qty
        self.usdt += self.position_qty * price

        if pnl > 0:
            self.winning_trades += 1
        else:
            self.losing_trades += 1

        self.position_qty = 0
        self.entry_price = None
        print(f"[SELL] {symbol} @ {price:.4f} | PnL: {pnl:.4f} USDT")

    def check_risk(self, price, symbol=PRIMARY_SYMBOL):
        if self.entry_price is None:
            return

        change = ((price - self.entry_price) / self.entry_price) * 100

        if change <= -STOP_LOSS_PERCENT:
            print(f"[STOP LOSS] {symbol} change={change:.2f}%")
            self.sell(price, symbol)
        elif change >= TAKE_PROFIT_PERCENT:
            print(f"[TAKE PROFIT] {symbol} change={change:.2f}%")
            self.sell(price, symbol)


class TraderBot:
    def __init__(self, paper_mode=PAPER_MODE, symbol=PRIMARY_SYMBOL):
        self.paper_mode = paper_mode
        self.symbol = symbol
        self.portfolio = PaperPortfolio()
        self.last_signal = 0

    def run_once(self):
        df = get_klines(symbol=self.symbol)
        signal_info = generate_signal(df)
        signal = signal_info["signal"]
        price = get_current_price(symbol=self.symbol)

        print(f"Signal={signal} | Price={price:.4f} | Confidence={signal_info['confidence']} | {signal_info['reason']} | USDT={self.portfolio.usdt:.2f}")

        if signal == 1:
            self.last_signal = 1
            self.portfolio.buy(price, self.symbol)
            if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
                send_telegram_message(f"BUY {self.symbol} @ {price:.4f} | confidence={signal_info['confidence']}")
        elif signal == -1:
            self.last_signal = -1
            self.portfolio.sell(price, self.symbol)
            if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
                send_telegram_message(f"SELL {self.symbol} @ {price:.4f} | confidence={signal_info['confidence']}")

        self.portfolio.check_risk(price, self.symbol)

    def run_forever(self, interval_seconds=30):
        while True:
            try:
                self.run_once()
                time.sleep(interval_seconds)
            except Exception as exc:
                print(f"[ERREUR] {exc}")
                time.sleep(interval_seconds)
