import telebot

# O'zingizning ma'lumotlaringizni kiriting
API_TOKEN = '8439338363:AAG_fpmRwdopmwel0coOPAfZJHUaHtuupss'
ADMIN_CHANNEL_ID = 3581076799 # Kanalingiz IDsi
bot = telebot.TeleBot(API_TOKEN)

# Foydalanuvchi ma'lumotlarini vaqtinchalik saqlash
users_db = {} 

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! Fayllarni saqlash uchun avval login va parol o'ylab toping.\nFormat: Login:Parol")

@bot.message_handler(func=lambda message: ":" in message.text)
def register(message):
    login_data = message.text
    users_db[message.chat.id] = login_data
    bot.send_message(message.chat.id, f"Siz tizimga kirdingiz: {login_data}. Endi fayllarni yuboring!")

@bot.message_handler(content_types=['document', 'photo', 'video', 'audio'])
def handle_docs(message):
    if message.chat.id in users_db:
        # Faylni kanalga yo'naltirish (Izohida foydalanuvchi logini bilan)
        caption = f"User: {users_db[message.chat.id]}"
        bot.forward_message(ADMIN_CHANNEL_ID, message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Fayl xavfsiz saqlandi! ✅")
    else:
        bot.send_message(message.chat.id, "Avval Login:Parol yuboring!")

bot.polling()
