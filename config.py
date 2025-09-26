import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "22849789"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "0fc127c6055acd59f00ec6c229e1e3c4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8325258009:AAGY9-XEq1kI0xDhGWkbOHkysiPSvSYenv8")

OWNER_ID = int(os.environ.get("OWNER_ID", "7296271316"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://autoappx750:Yash2835P@autoappx.drvhbnu.mongodb.net/?retryWrites=true&w=majority&appName=Autoappx")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
