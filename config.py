from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Токен бота из @BotFather
ADMIN_ID = os.getenv("ADMIN_ID")    # Ваш ID в Telegram для уведомлений
