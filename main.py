import telebot
from config import token
from functions import command_func
from commands import default_commands
import messages

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['low'])
def low(message):
    bot.send_message(message.chat.id, messages.how_many_goods_message)
    # получить аргумент и передать в command_func аргументом
    bot.send_message(message.chat.id, command_func(11))


@bot.message_handler(commands=['high'])
def high(message):
    bot.send_message(message.chat.id, messages.how_many_goods_message)
    # получить аргумент и передать в command_func
    bot.send_message(message.chat.id, command_func(11, reverse=True))


@bot.message_handler(commands=['hot'])
def hot(message):
    bot.send_message(message.chat.id, messages.how_many_goods_message)
    # получить аргумент и передать в command_func
    bot.send_message(message.chat.id, command_func(11, reverse=True, sorted_by='orders_quantity'))


@bot.message_handler(commands=['custom'])
def hot(message):
    bot.send_message(message.chat.id, messages.how_many_goods_message)
    # получить количество товаров
    bot.send_message(message.chat.id, messages.low_lim_message)
    # получить нижнюю границу цен
    bot.send_message(message.chat.id, messages.high_lim_message)
    # получить верхнюю границу цен

    # передать все выше в аргументы command_func
    bot.send_message(message.chat.id, command_func(11, low_lim=3, high_lim=7))


@bot.message_handler(commands=['start', 'help'])
def start_or_help_message(message):
    bot.send_message(message.chat.id, messages.help_message)


@bot.message_handler(content_types=["text"])
def echo_text(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.set_my_commands(default_commands)
    bot.infinity_polling()
