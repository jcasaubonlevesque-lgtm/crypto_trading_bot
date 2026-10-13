from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import auth, users, portfolio, signals, orders, subscriptions

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AVANTOPS AI - Premium crypto trading intelligence platform",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "app": settings.app_name,
        "version": settings.app_version,
        "status": "online",
        "docs": "/docs",
    }

@app.get("/health")
async def health():
    return {"status": "ok"}

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(portfolio.router, prefix="/api/v1/portfolio", tags=["portfolio"])
app.include_router(signals.router, prefix="/api/v1/signals", tags=["signals"])
app.include_router(orders.router, prefix="/api/v1/orders", tags=["orders"])
app.include_router(subscriptions.router, prefix="/api/v1/subscriptions", tags=["subscriptions"])
