from loader import bot
from utils.history_input_func import history_input_func
from utils.statistics_input_func import statistics_input_func
from utils.history_output_func import history_output_func


@bot.message_handler(commands=['history'])
def history_message(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, history_output_func(message))
