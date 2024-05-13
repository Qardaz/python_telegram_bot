from telebot.types import BotCommand

default_commands = [
    # BotCommand('hello-world', 'привет, мир'),
    BotCommand('hello_world', 'привет, мир'),
    BotCommand('start', 'начало работы'),
    BotCommand('help', 'помощь'),
    BotCommand('low', 'сортировка товаров по возрастанию цены'),
    BotCommand('high', 'сортировка товаров по убыванию цены'),
    BotCommand('hot', 'сортировка товаров по убыванию количества заказов'),
    BotCommand('custom', 'сортировка товаров по возрастанию цены в интервале цен')
]
