from app.market_data import get_klines
from app.strategy import generate_signal


def run_backtest(initial_balance=100.0, symbol="BTCUSDT"):
    df = get_klines(symbol=symbol)
    balance = initial_balance
    position = 0.0
    entry_price = 0.0
    result = []
    trades = 0

    for i in range(100, len(df)):
        window = df.iloc[max(0, i - 100): i + 1].copy()
        signal = generate_signal(window)
        close_price = df["close"].iloc[i]

        if signal == 1 and position <= 0:
            position = balance / close_price
            entry_price = close_price
            result.append({"type": "BUY", "price": close_price, "time": df["timestamp"].iloc[i]})

        elif signal == -1 and position > 0:
            pnl = (close_price - entry_price) * position
            balance += position * close_price
            trades += 1
            position = 0.0
            entry_price = 0.0
            result.append({"type": "SELL", "price": close_price, "time": df["timestamp"].iloc[i]})

    if position > 0:
        balance += position * df["close"].iloc[-1]
        trades += 1

    final_balance = balance

    return {
        "initial_balance": initial_balance,
        "final_balance": final_balance,
        "pnl": final_balance - initial_balance,
        "trades": trades,
        "result": result,
    }
