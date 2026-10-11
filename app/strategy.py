import pandas as pd
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator
from ta.volatility import AverageTrueRange


def add_indicators(df: pd.DataFrame):
    close = df["close"]
    high = df["high"]
    low = df["low"]

    ema_fast = EMAIndicator(close, window=12).ema_indicator()
    ema_slow = EMAIndicator(close, window=26).ema_indicator()
    macd_line = ema_fast - ema_slow
    signal_line = EMAIndicator(macd_line, window=9).ema_indicator()
    macd_hist = macd_line - signal_line
    rsi = RSIIndicator(close, window=14).rsi()
    atr = AverageTrueRange(high, low, close, window=14).average_true_range()

    df["ema_fast"] = ema_fast
    df["ema_slow"] = ema_slow
    df["macd_line"] = macd_line
    df["macd_signal"] = signal_line
    df["macd_hist"] = macd_hist
    df["rsi"] = rsi
    df["atr"] = atr

    return df


def generate_signal(df: pd.DataFrame):
    if df.empty:
        return {"signal": 0, "confidence": 0.0, "reason": "empty data"}

    df = add_indicators(df)

    ema_fast = df["ema_fast"].iloc[-1]
    ema_slow = df["ema_slow"].iloc[-1]
    macd_hist = df["macd_hist"].iloc[-1]
    rsi = df["rsi"].iloc[-1]
    atr = df["atr"].iloc[-1]

    if pd.isna(ema_fast) or pd.isna(ema_slow) or pd.isna(macd_hist) or pd.isna(rsi) or pd.isna(atr):
        return {"signal": 0, "confidence": 0.0, "reason": "indicators unavailable"}

    if ema_fast > ema_slow and macd_hist > 0 and rsi > 50:
        confidence = min(0.95, 0.55 + ((ema_fast - ema_slow) / max(ema_slow, 1e-8)) * 80 + (rsi - 50) / 100)
        return {
            "signal": 1,
            "confidence": round(max(0.0, confidence), 2),
            "reason": "trend bullish + momentum + RSI above 50",
        }

    if ema_fast < ema_slow and macd_hist < 0 and rsi < 50:
        confidence = min(0.95, 0.55 + ((ema_slow - ema_fast) / max(ema_fast, 1e-8)) * 80 + (50 - rsi) / 100)
        return {
            "signal": -1,
            "confidence": round(max(0.0, confidence), 2),
            "reason": "trend bearish + momentum + RSI below 50",
        }

    return {"signal": 0, "confidence": 0.0, "reason": "neutral market"}
