from fastapi import APIRouter

router = APIRouter()

@router.get("/current")
async def current_signal():
    return {"symbol": "BTCUSDT", "action": 1, "confidence": 0.88, "reason": "Bullish breakout", "timestamp": "2025-01-01T12:00:00Z"}

@router.get("/history")
async def signal_history():
    return [
        {"symbol": "BTCUSDT", "action": 1, "confidence": 0.88, "reason": "Bullish breakout"},
        {"symbol": "ETHUSDT", "action": -1, "confidence": 0.74, "reason": "Weak momentum"},
        {"symbol": "SOLUSDT", "action": 0, "confidence": 0.0, "reason": "Neutral"},
    ]
