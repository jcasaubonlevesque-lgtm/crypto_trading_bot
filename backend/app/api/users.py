from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.db.models import User
from app.core.security import hash_password, verify_password, create_token

router = APIRouter()

@router.get("/me")
async def me(db: Session = Depends(get_db)):
    user = db.query(User).first()
    if not user:
        return {"id": 1, "email": "demo@avantops.ai", "full_name": "Demo User", "is_active": True, "is_premium": False}
    return {"id": user.id, "email": user.email, "full_name": user.full_name, "is_active": user.is_active, "is_premium": user.is_premium}
