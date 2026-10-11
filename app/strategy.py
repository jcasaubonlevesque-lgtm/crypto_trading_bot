import pandas as pd
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator


def add_indicators(df: pd.DataFrame):
    close = df["close"]

    ema_fast = EMAIndicator(close, window=12).ema_indicator()
    ema_slow = EMAIndicator(close, window=26).ema_indicator()
    macd = ema_fast - ema_slow
    rsi = RSIIndicator(close, window=14).rsi()

    df["ema_fast"] = ema_fast
    df["ema_slow"] = ema_slow
    df["macd"] = macd
    df["rsi"] = rsi

    return df


def generate_signal(df: pd.DataFrame):
    if df.empty:
        return 0

    df = add_indicators(df)

    ema_fast = df["ema_fast"].iloc[-1]
    ema_slow = df["ema_slow"].iloc[-1]
    macd = df["macd"].iloc[-1]
    rsi = df["rsi"].iloc[-1]

    if pd.isna(ema_fast) or pd.isna(ema_slow) or pd.isna(macd) or pd.isna(rsi):
        return 0

    if ema_fast > ema_slow and macd > 0 and rsi > 50:
        return 1

    if ema_fast < ema_slow and macd < 0 and rsi < 50:
        return -1

    return 0
