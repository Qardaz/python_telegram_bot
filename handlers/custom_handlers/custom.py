from loader import bot
from utils.history_input_func import history_input_func
from utils.statistics_input_func import statistics_input_func
from database.database_models import Message
from utils.check_message_func import check_message_func
from utils.command_func import command_func


@bot.message_handler(commands=['custom'])
def custom_command(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, Message.get(name='how_many_goods').message)
    bot.register_next_step_handler(message, custom_how_many)


def custom_how_many(message):
    history_input_func(message)
    statistics_input_func(message.text)

    how_many = message.text
    if check_message_func(how_many):
        bot.send_message(message.chat.id, Message.get(name='low_lim').message)
        bot.register_next_step_handler(message, custom_low_lim, how_many)
    else:
        bot.send_message(message.chat.id, Message.get(name='error_how_many').message)
        message.text = "/custom"
        custom_command(message=message)


def custom_low_lim(message, how_many):
    history_input_func(message)
    statistics_input_func(message.text)

    low_lim = message.text
    if check_message_func(low_lim):
        bot.send_message(message.chat.id, Message.get(name='high_lim').message)
        bot.register_next_step_handler(message, custom_high_lim, how_many, low_lim)
    else:
        bot.send_message(message.chat.id, Message.get(name='error_how_many').message)
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
        bot.send_message(message.chat.id, Message.get(name='error_how_many').message)
        message.text = low_lim
        custom_low_lim(message=message, how_many=how_many)
