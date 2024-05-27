import telebot

from config import token
from core import command_func, check_message_func, history_input_func, history_output_func, statistics_input_func, \
    show_all_func, check_good_func, show_my_orders_func
from commands import default_commands
import messages

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['hello_world'])
def hello(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, 'hello-hello')


@bot.message_handler(commands=['low', 'high', 'hot'])
def primitive_sort_command(message):
    history_input_func(message)
    statistics_input_func(message.text)
    bot.send_message(message.chat.id, messages.how_many_goods)

    bot.register_next_step_handler(message, primitive_sort_output, message.text.lstrip('/'))


def primitive_sort_output(message, coming_command):
    history_input_func(message)
    statistics_input_func(message.text)
    how_many = message.text
    if coming_command == "high":
        reverse = True
        sorted_by = 'price'
    elif coming_command == "hot":
        reverse = True
        sorted_by = 'orders_quantity'
    else:
        reverse = False
        sorted_by = 'price'
    if check_message_func(how_many):
        bot.send_message(message.chat.id, command_func(how_many=how_many, sorted_by=sorted_by, reverse=reverse))
    else:
        bot.send_message(message.chat.id, messages.error_how_many_message)
        message.text = "/" + coming_command
        primitive_sort_command(message=message)


@bot.message_handler(commands=['show_all_goods'])
def show_all_command(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, show_all_func())


@bot.message_handler(commands=['buy'])
def buy_command(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, messages.buy_message)
    bot.register_next_step_handler(message, buy_good)


def buy_good(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, check_good_func(message))


@bot.message_handler(commands=['show_my_orders'])
def show_my_orders_command(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, show_my_orders_func(message))


@bot.message_handler(commands=['custom'])
def custom_command(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, messages.how_many_goods)
    bot.register_next_step_handler(message, custom_how_many)


def custom_how_many(message):
    history_input_func(message)
    statistics_input_func(message.text)

    how_many = message.text
    if check_message_func(how_many):
        bot.send_message(message.chat.id, messages.low_lim_message)
        bot.register_next_step_handler(message, custom_low_lim, how_many)
    else:
        bot.send_message(message.chat.id, messages.error_how_many_message)
        message.text = "/custom"
        custom_command(message=message)


def custom_low_lim(message, how_many):
    history_input_func(message)
    statistics_input_func(message.text)

    low_lim = message.text
    if check_message_func(low_lim):
        bot.send_message(message.chat.id, messages.high_lim_message)
        bot.register_next_step_handler(message, custom_high_lim, how_many, low_lim)
    else:
        bot.send_message(message.chat.id, messages.error_how_many_message)
        message.text = how_many
        custom_how_many(message=message)


def custom_high_lim(message, how_many, low_lim):
    history_input_func(message)
    statistics_input_func(message.text)

    high_lim = message.text
    if check_message_func(high_lim):
        bot.send_message(message.chat.id, command_func(how_many=how_many, sorted_by='price',
                                                       reverse=False, high_lim=high_lim, low_lim=low_lim))
    else:
        bot.send_message(message.chat.id, messages.error_how_many_message)
        message.text = low_lim
        custom_low_lim(message=message, how_many=how_many)


@bot.message_handler(commands=['start'])
def start_or_help_message(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, messages.start_message)


@bot.message_handler(commands=['help'])
def help_message(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, messages.help_message)


@bot.message_handler(commands=['history'])
def history_message(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, history_output_func(message))


@bot.message_handler(commands=['statistics'])
def output_statistics_message(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, statistics_output_func())


@bot.message_handler(content_types=["text"])
def echo_text(message):
    history_input_func(message)
    statistics_input_func(message.text)

    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет :)')
    else:
        bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.set_my_commands(default_commands)
    bot.infinity_polling()
