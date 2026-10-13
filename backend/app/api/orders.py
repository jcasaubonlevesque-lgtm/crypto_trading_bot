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
    return [{"id": 1, "symbol": "BTCUSDT", "side": "BUY", "quantity": 0.01, "price": 45000.0, "status": "executed", "paper_mode": True}]

@router.post("/place")
async def place_order(payload: PlaceOrderInput):
    return {
        "id": 101,
        "symbol": payload.symbol,
        "side": payload.side,
        "quantity": payload.quantity,
        "price": payload.price,
        "status": "pending_confirmation",
        "paper_mode": payload.paper_mode,
    }
