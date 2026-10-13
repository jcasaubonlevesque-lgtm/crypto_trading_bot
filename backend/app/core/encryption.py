from cryptography.fernet import Fernet
from app.core.config import settings

cipher = Fernet(settings.cipher_key.encode())


def encrypt_value(value: str) -> str:
    return cipher.encrypt(value.encode()).decode()


def decrypt_value(token: str) -> str:
    return cipher.decrypt(token.encode()).decode()
