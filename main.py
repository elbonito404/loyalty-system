import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN, ADMIN_ID

# Инициализация бота
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# "База данных"
users_db = {}
promo_codes = {"WELCOME10": 10, "SUMMER20": 20}  # Промокоды: код > баллы

# Команда /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user_id = message.from_user.id
    if user_id not in users_db:
        users_db[user_id] = {"balance": 0, "history": []}
        await message.answer("🎉 Добро пожаловать в программу лояльности!\n"
                           "🔹 /balance — проверить баллы\n"
                           "🔹 /promo — активировать промокод\n"
                           "🔹 /gift — обменять баллы на подарки")
    else:
        await message.answer("С возвращением! Используйте меню команд.")

# Проверка баланса
@dp.message_handler(commands=["balance"])
async def balance(message: types.Message):
    user_id = message.from_user.id
    balance = users_db.get(user_id, {}).get("balance", 0)
    await message.answer(f"💰 Ваш баланс: {balance} баллов.")

# Активация промокода
@dp.message_handler(commands=["promo"])
async def promo(message: types.Message):
    await message.answer("Введите промокод (например, WELCOME10):")

@dp.message_handler(lambda msg: msg.text.upper() in promo_codes)
async def apply_promo(message: types.Message):
    user_id = message.from_user.id
    promo_code = message.text.upper()
    points = promo_codes[promo_code]
    
    if user_id not in users_db:
        users_db[user_id] = {"balance": 0, "history": []}
    
    users_db[user_id]["balance"] += points
    users_db[user_id]["history"].append(f"+{points} за промокод {promo_code}")
    
    await message.answer(f"✅ Промокод активирован! +{points} баллов.")

# Обмен баллов на подарки (пример)
@dp.message_handler(commands=["gift"])
async def gift_menu(message: types.Message):
    gifts = {
        "1": {"name": "Скидка 10%", "cost": 50},
        "2": {"name": "Бесплатная доставка", "cost": 30},
    }
    text = "🎁 Выберите подарок:\n" + "\n".join(
        f"{id}. {gift['name']} — {gift['cost']} баллов" 
        for id, gift in gifts.items()
    )
    await message.answer(text)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
