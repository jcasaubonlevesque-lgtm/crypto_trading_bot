import pandas as pd
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator
from ta.volatility import AverageTrueRange

class StrategyEngine:
    def __init__(self):
        self.name = "EMA_MACD_RSI"

    def add_indicators(self, df: pd.DataFrame):
        close = df["close"]
        high = df["high"]
        low = df["low"]

        ema_fast = EMAIndicator(close, window=12).ema_indicator()
        ema_slow = EMAIndicator(close, window=26).ema_indicator()
        macd_line = ema_fast - ema_slow
        macd_signal = EMAIndicator(macd_line, window=9).ema_indicator()
        macd_hist = macd_line - macd_signal
        rsi = RSIIndicator(close, window=14).rsi()
        atr = AverageTrueRange(high, low, close, window=14).average_true_range()

        df["ema_fast"] = ema_fast
        df["ema_slow"] = ema_slow
        df["macd_hist"] = macd_hist
        df["rsi"] = rsi
        df["atr"] = atr
        return df

    def generate_signal(self, df: pd.DataFrame):
        if df.empty:
            return {"action": 0, "confidence": 0.0, "reason": "No data"}

        df = self.add_indicators(df)
        ema_fast = df["ema_fast"].iloc[-1]
        ema_slow = df["ema_slow"].iloc[-1]
        macd_hist = df["macd_hist"].iloc[-1]
        rsi = df["rsi"].iloc[-1]

        if pd.isna(ema_fast) or pd.isna(ema_slow) or pd.isna(macd_hist) or pd.isna(rsi):
            return {"action": 0, "confidence": 0.0, "reason": "Indicators unavailable"}

        if ema_fast > ema_slow and macd_hist > 0 and rsi > 50:
            return {"action": 1, "confidence": 0.88, "reason": "Bullish trend"}
        if ema_fast < ema_slow and macd_hist < 0 and rsi < 50:
            return {"action": -1, "confidence": 0.87, "reason": "Bearish trend"}
        return {"action": 0, "confidence": 0.0, "reason": "Neutral market"}
