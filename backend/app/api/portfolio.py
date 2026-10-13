from fastapi import APIRouter
from app.services.trading_service import TradingService

router = APIRouter()
service = TradingService()

@router.get("/summary")
async def portfolio_summary():
    snapshot = service.get_portfolio_snapshot(balance_usdt=100.0)
    return {
        "balance_usdt": snapshot["balance_usdt"],
        "total_value": snapshot["total_value"],
        "pnl_24h": snapshot["pnl_24h"],
        "pnl_24h_percent": snapshot["pnl_24h_percent"],
        "positions": snapshot["positions"],
    }

@router.get("/positions")
async def positions():
    snapshot = service.get_portfolio_snapshot(balance_usdt=100.0)
    return snapshot["positions"]
