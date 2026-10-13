from fastapi import APIRouter

router = APIRouter()

@router.get("/me")
async def get_current_user():
    return {
        "id": 1,
        "email": "demo@avantops.ai",
        "full_name": "Demo User",
        "is_active": True,
        "is_premium": False,
    }

@router.get("/profile")
async def get_profile():
    return {"status": "ok", "message": "Profile loaded"}
