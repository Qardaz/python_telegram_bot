from loader import bot
from utils.history_input_func import history_input_func
from utils.statistics_input_func import statistics_input_func


@bot.message_handler(commands=['hello_world'])
def hello(message):
    history_input_func(message)
    statistics_input_func(message.text)

    bot.send_message(message.chat.id, 'hello-hello')
