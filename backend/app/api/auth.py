from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.db.models import User
from app.core.security import hash_password, verify_password, create_token

router = APIRouter()

class RegisterInput(BaseModel):
    email: EmailStr
    full_name: str
    password: str

class LoginInput(BaseModel):
    email: EmailStr
    password: str

@router.post("/register")
async def register(payload: RegisterInput, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

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

@router.post("/login")
async def login(payload: LoginInput, db: Session = Depends(get_db)):
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
