from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_subscriptions():
    return {"plan": "free", "status": "active"}

@router.post("/create")
async def create_subscription():
    return {"status": "ok", "message": "Subscription created"}
