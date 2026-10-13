from typing import Optional, List
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserRegisterRequest(BaseModel):
    email: EmailStr
    full_name: str
    password: str

class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    is_active: bool = True
    is_premium: bool = False
    created_at: datetime

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int = 3600

class ApiKeyRequest(BaseModel):
    provider: str
    api_key: str
    api_secret: str

class SubscriptionPlan(BaseModel):
    id: str
    name: str
    price: float
    interval: str
    features: List[str]

class SubscriptionStatus(BaseModel):
    plan: str
    status: str
    active: bool
    trial_ends_at: Optional[datetime] = None

class PortfolioSummary(BaseModel):
    balance_usdt: float
    total_value: float
    pnl_24h: float
    pnl_24h_percent: float
    positions: List[dict]

class SignalResponse(BaseModel):
    symbol: str
    action: int
    confidence: float
    reason: str
    timestamp: datetime

class OrderRequest(BaseModel):
    symbol: str
    side: str
    quantity: float
    price: float
    paper_mode: bool = True

class OrderResponse(BaseModel):
    id: int
    symbol: str
    side: str
    quantity: float
    price: float
    status: str
    paper_mode: bool
    created_at: datetime
