from loader import bot
from utils.history_input_func import history_input_func
from utils.statistics_input_func import statistics_input_func


@bot.message_handler(content_types=["text"])
def echo_text(message):
    history_input_func(message)
    statistics_input_func(message.text)

    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет :)')
    else:
        bot.send_message(message.chat.id, message.text)
