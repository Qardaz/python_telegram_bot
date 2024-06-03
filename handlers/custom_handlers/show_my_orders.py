from loader import bot
from utils.history_input_func import history_input_func
from utils.statistics_input_func import statistics_input_func
from utils.show_my_orders_func import show_my_orders_func


@bot.message_handler(commands=['show_my_orders'])
def show_my_orders_command(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, show_my_orders_func(message))
