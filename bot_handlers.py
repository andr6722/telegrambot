from bot import bot
from config import TOKEN
from messages import *
from smart_home import SmartHomeBot

smart_home_bot = SmartHomeBot(TOKEN, "user.db")
flag = 0


@bot.message_handler(commands=['start'])
def handle_start(message):
    smart_home_bot.start(message)


@bot.message_handler(commands=['login'])
def handle_login(message):
    smart_home_bot.request_login_password(message.chat.id, message)


@bot.message_handler(commands=['show_status'])
def handle_show_status(message):
    bot.send_message(message.chat.id, START_MESSAGE)


@bot.message_handler(commands=['control'])
def handle_control(message):
    bot.send_message(message.chat.id, START_MESSAGE)


@bot.message_handler(commands=['create_automation'])
def handle_create_automation(message):
    bot.send_message(message.chat.id, START_MESSAGE)


@bot.message_handler(commands=['schedule_control'])
def handle_schedule_control(message):
    bot.send_message(message.chat.id, START_MESSAGE)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, HELP_INFO)



if __name__ == '__main__':
    bot.polling(none_stop=True)
