from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.db.models import User, Subscription
from app.core.security import hash_password, verify_password, create_token
from app.schemas.models import UserRegisterRequest, UserLoginRequest, UserResponse, TokenResponse

router = APIRouter()

@router.post("/register", response_model=TokenResponse)
async def register(payload: UserRegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == str(payload.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already in use")

    user = User(
        email=str(payload.email),
        full_name=payload.full_name,
        password_hash=hash_password(payload.password),
        is_active=True,
        is_premium=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_token({"sub": user.email})
    return {
        "access_token": token,
        "refresh_token": token,
        "token_type": "bearer",
        "expires_in": 3600,
    }

@router.post("/login", response_model=TokenResponse)
async def login(payload: UserLoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == str(payload.email)).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": user.email})
    return {
        "access_token": token,
        "refresh_token": token,
        "token_type": "bearer",
        "expires_in": 3600,
    }

@router.get("/me", response_model=UserResponse)
async def me():
    return {
        "id": 1,
        "email": "demo@avantops.ai",
        "full_name": "Demo User",
        "is_active": True,
        "is_premium": False,
        "created_at": "2025-01-01T00:00:00Z",
    }
