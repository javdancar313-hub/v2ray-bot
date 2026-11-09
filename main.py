import telebot
import requests
import time

TOKEN = '9198552167:AAHfD1PiSA9PcvQknVLzHuUhBBbLeLAT-nM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, 
        "سلام! ربات من روی سرور ابری روشن شد و بدون قطعی کار می‌کند! 🚀"
    )

if __name__ == "__main__":
    print("Cloud Bot is running...")
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=30)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)
