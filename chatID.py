import telebot
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Seu chat ID é: {message.chat.id}")

bot.polling()