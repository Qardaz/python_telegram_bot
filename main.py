import telebot

token = '6855239878:AAEnHljJy9MjG9vfqqi8hsjnTksnEv0Bd98'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['hello-world'])
def start_message(message):
    bot.send_message(message.chat.id, 'hello-hello')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет :)')


bot.polling()
