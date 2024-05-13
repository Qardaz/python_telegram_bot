import telebot

from config import token
from sort_goods_list_function import command_func
from commands import default_commands
import messages


bot = telebot.TeleBot(token)


# @bot.message_handler(commands=['hello-world'])

@bot.message_handler(commands=['hello_world'])
def hello(message):
    bot.send_message(message.chat.id, 'hello-hello')


@bot.message_handler(commands=['low'])
def low_command(message):
    bot.send_message(message.chat.id, messages.how_many_goods)
    bot.register_next_step_handler(message, low_command_output)


def low_command_output(message):
    how_many = message.text
    bot.send_message(message.chat.id, command_func(how_many=how_many))


@bot.message_handler(commands=['high'])
def high_command(message):
    bot.send_message(message.chat.id, messages.how_many_goods)
    bot.register_next_step_handler(message, high_command_output)


def high_command_output(message):
    how_many = message.text
    bot.send_message(message.chat.id, command_func(how_many=how_many, reverse=True))


@bot.message_handler(commands=['hot'])
def hot_command(message):
    bot.send_message(message.chat.id, messages.how_many_goods)
    bot.register_next_step_handler(message, hot_command_output)


def hot_command_output(message):
    how_many = message.text
    bot.send_message(message.chat.id, command_func(how_many=how_many, reverse=True, sorted_by='orders_quantity'))


@bot.message_handler(commands=['custom'])
def custom_command(message):
    bot.send_message(message.chat.id, messages.how_many_goods)
    bot.register_next_step_handler(message, custom_how_many)


def custom_how_many(message):
    how_many = message.text
    bot.send_message(message.chat.id, messages.low_lim_message)
    bot.register_next_step_handler(message, custom_low_lim, how_many)


def custom_low_lim(message, how_many):
    low_lim = message.text
    bot.send_message(message.chat.id, messages.high_lim_message)
    bot.register_next_step_handler(message, custom_high_lim, how_many, low_lim)


def custom_high_lim(message, how_many, low_lim):
    high_lim = message.text
    bot.send_message(message.chat.id, command_func(how_many=how_many, low_lim=low_lim, high_lim=high_lim))


@bot.message_handler(commands=['start', 'help'])
def start_or_help_message(message):
    bot.send_message(message.chat.id, messages.help_message)


@bot.message_handler(content_types=['text'])
def hello(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет :)')


# @bot.message_handler(content_types=["text"])
# def echo_text(message):
#     bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.set_my_commands(default_commands)
    bot.infinity_polling()
