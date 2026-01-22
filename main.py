import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command

# Sizning doimiy tokeningiz
TOKEN = "8312097068:AAFHC0j59aA1bncScbmyYdMs6_evjoweOzA"

# Loglarni sozlash (xatoliklarni ko'rish uchun)
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start buyrug'i
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_name = message.from_user.full_name
    text = (f"Salom {user_name}!\n\n"
            "Bu bot sizning maxsus loyihangiz uchun tayyorlandi.\n"
            "Qanday yordam bera olaman?")
    
    # Tugmalar yaratish
    kb = [
        [types.KeyboardButton(text="🚀 Loyihani boshlash")],
        [types.KeyboardButton(text="👤 Profil"), types.KeyboardButton(text="ℹ️ Ma'lumot")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    
    await message.answer(text, reply_markup=keyboard)

# /help buyrug'i
@dp.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer("Yordam bo'limi: Bot orqali turli xizmatlardan foydalanishingiz mumkin.")

# Tugmalar uchun handler
@dp.message(F.text == "🚀 Loyihani boshlash")
async def start_project(message: types.Message):
    await message.answer("Loyiha yuklanmoqda... Kuting.")

# Har qanday matnli xabarga javob
@dp.message(F.text)
async def text_handler(message: types.Message):
    await message.reply(f"Siz yozdingiz: {message.text}")

async def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")
