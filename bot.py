import telebot
import config

bot = telebot.TeleBot(config.TOKEN)
print(bot.get_me())
# если все в порядке, значит будем видеть параметры бота
