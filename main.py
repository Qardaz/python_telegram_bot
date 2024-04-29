import telebot
from low import low_func
from high import high_func
from custom import custom_func
from hot import hot_func


token = '6855239878:AAEnHljJy9MjG9vfqqi8hsjnTksnEv0Bd98'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет :)')


@bot.message_handler(commands=['low', 'high', 'custom', 'hot'])
def main(message):
    if message.text.lower() == '/low':
        bot.send_message(message.chat.id, 'Сколько товаров вывести?')

        @bot.message_handler(content_types=['text'])
        def how_many(message):
            how_many = message.text
            bot.send_message(message.chat.id, f'{low_func(how_many)}')

    elif message.text.lower() == '/high':
        bot.send_message(message.chat.id, 'Сколько товаров вывести?')

        @bot.message_handler(content_types=['text'])
        def how_many(message):
            how_many = message.text
            bot.send_message(message.chat.id, f'{high_func(how_many)}')

    elif message.text.lower() == '/hot':
        bot.send_message(message.chat.id, 'Сколько товаров вывести?')

        @bot.message_handler(content_types=['text'])
        def how_many(message):
            how_many = message.text
            bot.send_message(message.chat.id, f'{hot_func(how_many)}')

    # elif message.text.lower() == '/custom':
    #     @bot.message_handler(content_types=['text'])
    #     def how_many(message):
    #         bot.send_message(message.chat.id, 'Сколько товаров вывести?')
    #         how_many = message.text
    #
    #     @bot.message_handler(content_types=['text'])
    #     def upper_limit(message):
    #         bot.send_message(message.chat.id, 'Введите нижнюю границу.')
    #         lower_limit = message.text
    #
    #     @bot.message_handler(content_types=['text'])
    #     def lower_limit(message):
    #         bot.send_message(message.chat.id, 'Введите верхнюю границу.')
    #         upper_limit = message.text
    #         bot.send_message(message.chat.id, f'{custom_func(how_many, lower_limit, upper_limit)}')


bot.polling(none_stop=True)
