import pandas as pd
from binance.client import Client
from app.config import API_KEY, API_SECRET, SYMBOLS, PRIMARY_SYMBOL, INTERVAL, LIMIT

client = Client(API_KEY, API_SECRET)


def get_klines(symbol=PRIMARY_SYMBOL, interval=INTERVAL, limit=LIMIT):
    try:
        candles = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    except Exception as exc:
        raise RuntimeError(f"Erreur de récupération des données Binance pour {symbol}: {exc}")

    df = pd.DataFrame(candles, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])

    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["timestamp"] = pd.to_datetime(df["open_time"], unit="ms")
    df = df[["timestamp", "open", "high", "low", "close", "volume"]]

    return df


def get_current_price(symbol=PRIMARY_SYMBOL):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker["price"])
