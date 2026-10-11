import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY", "")
API_SECRET = os.getenv("BINANCE_API_SECRET", "")

SYMBOL = "BTCUSDT"
INTERVAL = "15m"
LIMIT = 500

INITIAL_USDT = 100.0
RISK_PERCENT = 1.0
STOP_LOSS_PERCENT = 2.5
TAKE_PROFIT_PERCENT = 5.0
PAPER_MODE = True
