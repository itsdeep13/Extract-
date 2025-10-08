import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "22484497"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "c38cb053916c47a97590c244663cbaef")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8260828039:AAGZDWSQyHKiTCFxP7Ub64c5IwrCU86IrFk")

OWNER_ID = int(os.environ.get("OWNER_ID", "6252997817"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS"6252997817, "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://uploaderbot:uploaderbot@cluster0.mpesxpw.mongodb.net/?retryWrites=true&w=majority"
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003120656587"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002934946350")  # Optional here you'll get all logs
