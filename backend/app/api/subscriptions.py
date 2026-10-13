from fastapi import APIRouter

router = APIRouter()

@router.get("/plans")
async def get_plan_catalog():
    return [
        {"id": "free", "name": "Free", "price": 0.0, "interval": "month", "features": ["Paper trading", "Limited signals"]},
        {"id": "premium_monthly", "name": "Premium Monthly", "price": 9.99, "interval": "month", "features": ["Live alerts", "Portfolio analytics", "Backtesting", "Premium signals"]},
        {"id": "premium_yearly", "name": "Premium Yearly", "price": 79.0, "interval": "year", "features": ["Everything premium", "Discounted billing"]},
    ]

@router.get("/status")
async def subscription_status():
    return {"plan": "free", "status": "active", "active": True}

@router.post("/checkout")
async def create_checkout():
    return {"status": "ok", "message": "Stripe checkout not configured yet"}
