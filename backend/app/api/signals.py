from fastapi import APIRouter
from datetime import datetime
from app.services.trading_service import TradingService

router = APIRouter()
service = TradingService()

@router.get("/current")
async def get_current_signal(symbol: str = "BTCUSDT"):
    signal = service.get_signal_for_symbol(symbol)
    return {
        "symbol": signal["symbol"],
        "action": signal["action"],
        "confidence": signal["confidence"],
        "reason": signal["reason"],
        "timestamp": datetime.utcnow().isoformat(),
        "price": signal["price"],
    }

@router.get("/history")
async def get_signal_history():
    return [
        {"symbol": "BTCUSDT", "action": 1, "confidence": 0.88, "reason": "Bullish breakout", "timestamp": "2025-01-01T12:00:00Z"},
        {"symbol": "ETHUSDT", "action": -1, "confidence": 0.74, "reason": "Weak momentum", "timestamp": "2025-01-01T11:00:00Z"},
        {"symbol": "SOLUSDT", "action": 0, "confidence": 0.0, "reason": "Neutral", "timestamp": "2025-01-01T10:00:00Z"},
    ]
