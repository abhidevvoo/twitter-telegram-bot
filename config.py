import os

class Config:
    ADMIN_ID = os.getenv("ADMIN_ID")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    BOT_DB_URL = os.getenv("BOT_DB_URL")   # Database connection
    X_BEARER_TOKENS = [
        token for token in [
            os.getenv("X_BEARER_TOKEN_1"),
            os.getenv("X_BEARER_TOKEN_2"),
            os.getenv("X_BEARER_TOKEN_3"),
            os.getenv("X_BEARER_TOKEN_4"),
            os.getenv("X_BEARER_TOKEN_5"),
        ] if token and token != "your_x_api_bearer_token"
    ]