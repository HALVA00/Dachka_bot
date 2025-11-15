import telebot
import webbrowser
import dotenv
from os import getenv

dotenv.load_dotenv()

bot = telebot.TeleBot(getenv("TELEGRAM_BOT_TOKEN"))

# COMMANDS


@bot.message_handler(commands=["wishlist", "website"])
def site(message):
    webbrowser.open(getenv("LINK_WISHLIST"))


@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, f"Здарова, {message.from_user.first_name}!")


@bot.message_handler(commands=["help"])
def main(message):
    bot.send_message(message.chat.id, "<b>Help information</b>", parse_mode="html")


@bot.message_handler()
def info(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, f"Здарова, {message.from_user.first_name}!")
    elif message.text.lower() == "id":
        bot.reply_to(message, f"ID: {message.from_user.id}")


bot.polling(none_stop=True)
