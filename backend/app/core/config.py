from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    app_name: str = "AVANTOPS AI"
    app_version: str = "1.0.0"
    debug: bool = False
    database_url: str = "postgresql://postgres:postgres@localhost:5432/avantops"
    secret_key: str = "change-this-secret-key-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    stripe_api_key: str = ""
    stripe_webhook_secret: str = ""
    binance_api_key: str = ""
    binance_api_secret: str = ""
    telegram_bot_token: str = ""
    telegram_chat_id: str = ""
    redis_url: str = "redis://localhost:6379/0"
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_password: str = ""
    sentry_dsn: str = ""
    allowed_origins: List[str] = ["*"]
    paper_mode_default: bool = True
    initial_balance: float = 100.0
    position_risk_percent: float = 1.0
    stop_loss_percent: float = 2.5
    take_profit_percent: float = 5.0

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
