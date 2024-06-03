from loader import bot
from utils.history_input_func import history_input_func
from utils.statistics_input_func import statistics_input_func
from database.database_models import Message
from utils.check_good_func import check_good_func


@bot.message_handler(commands=['buy'])
def buy_command(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, Message.get(name='buy').message)
    bot.register_next_step_handler(message, buy_good)


def buy_good(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, check_good_func(message))
