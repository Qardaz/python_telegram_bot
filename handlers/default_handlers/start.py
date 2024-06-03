from loader import bot
from utils.history_input_func import history_input_func
from utils.statistics_input_func import statistics_input_func
from database.database_models import Message


@bot.message_handler(commands=['start'])
def start_message(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, Message.get(name='start').message)
