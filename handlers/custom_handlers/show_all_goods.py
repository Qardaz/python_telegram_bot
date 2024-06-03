from loader import bot
from utils.history_input_func import history_input_func
from utils.statistics_input_func import statistics_input_func
from utils.command_func import command_func
from database.database_models import Good


@bot.message_handler(commands=['show_all_goods'])
def show_all_goods(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, command_func(how_many=Good.select().count()))
