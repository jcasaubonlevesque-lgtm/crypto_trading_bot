from fastapi import APIRouter

router = APIRouter()

@router.get("/current")
async def get_current_signal():
    return {
        "symbol": "BTCUSDT",
        "action": 1,
        "confidence": 0.88,
        "reason": "Bullish trend + RSI support + MACD positive",
        "timestamp": "2025-01-01T12:00:00Z"
    }

@router.get("/history")
async def get_signal_history():
    return [
        {"symbol": "BTCUSDT", "action": 1, "confidence": 0.88, "reason": "Bullish trend"},
        {"symbol": "ETHUSDT", "action": -1, "confidence": 0.72, "reason": "Bearish pressure"},
        {"symbol": "SOLUSDT", "action": 0, "confidence": 0.0, "reason": "Neutral market"},
    ]
