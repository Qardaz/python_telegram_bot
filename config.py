from telebot.types import BotCommand
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

default_commands = [
    # BotCommand('hello-world', 'привет, мир'),
    BotCommand('hello_world', 'привет, мир'),

    BotCommand('start', 'начало работы'),
    BotCommand('help', 'помощь'),
    BotCommand('history', 'вывод последних Ваших сообщений, адресованных боту'),

    BotCommand('show_all_goods', 'вывод списка всех товаров'),
    BotCommand('low', 'сортировка товаров по возрастанию цены'),
    BotCommand('high', 'сортировка товаров по убыванию цены'),
    BotCommand('hot', 'сортировка товаров по убыванию количества заказов'),
    BotCommand('custom', 'сортировка товаров по возрастанию цены в интервале цен'),

    BotCommand('buy', 'покупка товара'),
    BotCommand('show_my_orders', 'вывод моих заказов'),
]
