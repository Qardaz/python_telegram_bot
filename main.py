import telebot
from all_in_one import all_in_one_func


token = '6855239878:AAEnHljJy9MjG9vfqqi8hsjnTksnEv0Bd98'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет :)')


@bot.message_handler(commands=['low', 'high', 'hot', 'custom'])
def main(message):
    if message.text.lower() == '/low':
        bot.send_message(message.chat.id, 'Сколько товаров вывести?')

        @bot.message_handler(content_types=['text'])
        def how_many(message):
            user_input = message.text
            bot.send_message(message.chat.id, f'{all_in_one_func(user_input)}')

    elif message.text.lower() == '/high':
        bot.send_message(message.chat.id, 'Сколько товаров вывести?')

        @bot.message_handler(content_types=['text'])
        def how_many(message):
            user_input = message.text
            bot.send_message(message.chat.id, f'{all_in_one_func(how_many=user_input, reverse=True)}')

    elif message.text.lower() == '/hot':
        bot.send_message(message.chat.id, 'Сколько товаров вывести?')

        @bot.message_handler(content_types=['text'])
        def how_many(message):
            user_input = message.text
            bot.send_message(message.chat.id, all_in_one_func(how_many=user_input, sorted_by='orders_quantity'))

    elif message.text.lower() == '/custom':
        bot.send_message(
            message.chat.id,
            'Напишите через пробел, сколько товаров вывести, нижнюю границу и верхнюю границу цен.'
        )

        @bot.message_handler(content_types=['text'])
        def how_many(message):
            user_input = message.text.split()

            how_many = int(user_input[0])
            low_lim = int(user_input[1])
            high_lim = int(user_input[2])

            bot.send_message(
                message.chat.id,
                f'{all_in_one_func(how_many=how_many, low_lim=low_lim, high_lim=high_lim)}'
            )


bot.polling(none_stop=True)
