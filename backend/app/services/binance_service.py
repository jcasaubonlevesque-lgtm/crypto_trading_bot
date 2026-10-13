from binance.client import Client
from app.core.config import settings
import pandas as pd

class BinanceService:
    def __init__(self):
        self.client = Client(api_key=settings.binance_api_key, api_secret=settings.binance_api_secret)

    def get_klines(self, symbol: str = "BTCUSDT", interval: str = "15m", limit: int = 100):
        candles = self.client.get_klines(symbol=symbol, interval=interval, limit=limit)
        df = pd.DataFrame(candles, columns=[
            "open_time", "open", "high", "low", "close", "volume",
            "close_time", "quote_asset_volume", "number_of_trades",
            "taker_buy_base", "taker_buy_quote", "ignore"
        ])
        for key in ["open", "high", "low", "close", "volume"]:
            df[key] = pd.to_numeric(df[key], errors="coerce")
        df["timestamp"] = pd.to_datetime(df["open_time"], unit="ms")
        return df[["timestamp", "open", "high", "low", "close", "volume"]]

    def get_price(self, symbol: str = "BTCUSDT"):
        ticker = self.client.get_symbol_ticker(symbol=symbol)
        return float(ticker["price"])
