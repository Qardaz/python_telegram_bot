from loader import bot
from utils.history_input_func import history_input_func
from utils.statistics_input_func import statistics_input_func
from database.database_models import Message
from utils.check_message_func import check_message_func
from utils.command_func import command_func


@bot.message_handler(commands=['low', 'high', 'hot'])
def primitive_sort_command(message):
    history_input_func(message)
    statistics_input_func(message.text)
    bot.send_message(message.chat.id, Message.get(name='how_many_goods').message)

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
        sorted_by = 'order_quantity'
    else:
        reverse = False
        sorted_by = 'price'
    if check_message_func(how_many):
        bot.send_message(message.chat.id, command_func(how_many=how_many, sorted_by=sorted_by, reverse=reverse))
    else:
        bot.send_message(message.chat.id, Message.get(name='error_how_many').message)
        message.text = "/" + coming_command
        primitive_sort_command(message=message)
