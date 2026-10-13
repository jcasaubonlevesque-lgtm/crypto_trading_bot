from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class PlaceOrderInput(BaseModel):
    symbol: str
    side: str
    quantity: float
    price: float
    paper_mode: bool = True

@router.get("/")
async def list_orders():
    return [
        {"symbol": "BTCUSDT", "side": "BUY", "quantity": 0.01, "price": 45000.0},
        {"symbol": "ETHUSDT", "side": "SELL", "quantity": 0.2, "price": 2600.0},
    ]

@router.post("/place")
async def place_order(payload: PlaceOrderInput):
    return {
        "status": "ok",
        "symbol": payload.symbol,
        "side": payload.side,
        "quantity": payload.quantity,
        "paper_mode": payload.paper_mode,
        "message": "Order recorded successfully"
    }
