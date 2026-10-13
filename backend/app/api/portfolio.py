from fastapi import APIRouter

router = APIRouter()

@router.get("/summary")
async def portfolio_summary():
    return {
        "balance_usdt": 100.0,
        "total_value": 120.0,
        "pnl_24h": 2.5,
        "positions": [
            {"symbol": "BTCUSDT", "quantity": 0.02, "entry_price": 45000.0, "current_price": 47000.0, "pnl": 400.0, "pnl_percent": 4.2},
            {"symbol": "ETHUSDT", "quantity": 0.5, "entry_price": 2500.0, "current_price": 2600.0, "pnl": 50.0, "pnl_percent": 2.0}
        ]
    }

@router.get("/positions")
async def get_positions():
    return [{"symbol": "BTCUSDT", "quantity": 0.02, "entry_price": 45000.0, "current_price": 47000.0, "pnl": 400.0}]
