from app.market_data import get_klines
from app.strategy import generate_signal


def run_backtest(initial_balance=100.0, symbol="BTCUSDT"):
    df = get_klines(symbol=symbol)

    cash = initial_balance
    position_qty = 0.0
    entry_price = 0.0
    trades = 0
    wins = 0
    losses = 0
    equity_curve = []
    max_drawdown = 0.0

    for i in range(100, len(df)):
        window = df.iloc[max(0, i - 100): i + 1].copy()
        signal_info = generate_signal(window)
        signal = signal_info["signal"]
        close_price = df["close"].iloc[i]

        if signal == 1 and position_qty <= 0:
            position_qty = cash / close_price
            entry_price = close_price
            trades += 1

        elif signal == -1 and position_qty > 0:
            pnl = (close_price - entry_price) * position_qty
            cash += position_qty * close_price
            position_qty = 0.0
            if pnl > 0:
                wins += 1
            else:
                losses += 1
            entry_price = 0.0

        if position_qty > 0:
            equity = cash + position_qty * close_price
        else:
            equity = cash

        equity_curve.append(equity)

        if len(equity_curve) > 1:
            max_drawdown = max(max_drawdown, (max(equity_curve[:-1]) - equity) / max(max(equity_curve[:-1]), 1e-8))

    if position_qty > 0:
        cash += position_qty * df["close"].iloc[-1]
        position_qty = 0.0

    final_balance = cash

    return {
        "initial_balance": initial_balance,
        "final_balance": round(final_balance, 2),
        "pnl": round(final_balance - initial_balance, 2),
        "trades": trades,
        "wins": wins,
        "losses": losses,
        "max_drawdown": round(max_drawdown * 100, 2),
    }
