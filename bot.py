import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

players = []

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Ласкаво просимо в гру 'Мафія'! Напишіть /join, щоб приєднатися.")

@bot.message_handler(commands=["join"])
def join(message):
    if message.from_user.username not in players:
        players.append(message.from_user.username)
        bot.reply_to(message, f"{message.from_user.username} приєднався до гри!")

@bot.message_handler(commands=["players"])
def show_players(message):
    bot.reply_to(message, f"Гравці: {', '.join(players) if players else 'Нікого немає'}")

bot.polling()
