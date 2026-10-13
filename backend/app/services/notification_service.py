from app.core.config import settings
import requests

class NotificationService:
    @staticmethod
    def send_telegram(message: str):
        if not settings.telegram_bot_token or not settings.telegram_chat_id:
            return False
        url = f"https://api.telegram.org/bot{settings.telegram_bot_token}/sendMessage"
        data = {"chat_id": settings.telegram_chat_id, "text": message, "parse_mode": "HTML"}
        try:
            response = requests.post(url, data=data, timeout=10)
            return response.status_code == 200
        except Exception:
            return False

    @staticmethod
    def send_email(to: str, subject: str, body: str):
        return True
