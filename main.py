import telebot
from config import token
from functions import command_func
from commands import default_commands
import messages

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['low'])
def low(message):
    bot.send_message(message.chat.id, messages.how_many_goods_message)
    # как-то получить аргументы
    bot.send_message(message.chat.id, command_func('аргументы'))


@bot.message_handler(commands=['start', 'help'])
def start_or_help_message(message):
    bot.send_message(message.chat.id, messages.help_message)


@bot.message_handler(content_types=["text"])
def echo_text(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.set_my_commands(default_commands)
    bot.infinity_polling()
