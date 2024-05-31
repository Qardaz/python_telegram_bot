from datetime import datetime
import json

import requests

from database.database_models import *


def command_func(how_many, reverse=False, sorted_by='price', low_lim=None, high_lim=None):
    goods_quantity = Good.select().count()

    how_many = int(how_many)
    answer_string = ''

    if how_many > goods_quantity:
        how_many = goods_quantity
        answer_string += 'Введено число, превышающее общее количество товаров. Будут выведены все товары.\n'

    if low_lim and high_lim:
        low_lim, high_lim = int(low_lim), int(high_lim)

        if low_lim > high_lim:
            answer_string += 'Верхняя граница меньше нижней, значения границ будут поменяны местами.\n'
            low_lim, high_lim = high_lim, low_lim

        if low_lim == high_lim:
            return 'Верхняя и нижняя границы не могут быть равны. Повторите команду заново.'

        if high_lim - low_lim < how_many:
            how_many = high_lim - low_lim + 1

        if low_lim > Good.get(id=(goods_quantity - 1)).price:
            return 'Нижняя граница превышает стоимость самого дорогого товара. Повторите команду заново.'

        if high_lim < Good.get(id=0).price:
            return 'Верхняя граница ниже стоимости самого дешевого товара. Повторите команду заново.'

    else:
        good = Good.select(Good.price).order_by(Good.price.asc()).limit(1)
        for prices in good:
            low_lim = prices.price

        good = Good.select(Good.price).order_by(Good.price.desc()).limit(1)
        for prices in good:
            high_lim = prices.price

    if reverse:
        sorted_by += " desc"
    else:
        sorted_by += " asc"

    usd_api_exchange_rate = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json'

    from_currency = 'usd'
    to_currency = 'rub'

    response = requests.get(usd_api_exchange_rate)

    if response.status_code != 200:
        return 'Обменник валют не отвечает :('

    json_data = response.json()
    multiplier = json_data[from_currency][to_currency]

    for good in Good.select().order_by(SQL(sorted_by)).where(
            (Good.price >= low_lim) & (Good.price <= high_lim)
            ).limit(how_many):
        answer_string += (f'\nНазвание товара: {good.name}\n'
                          f'Цена товара:\n'
                          f'в usd: {good.price}$\n'
                          f'в rub: {good.price * multiplier:.2f}₽\n')

    return answer_string


def check_message_func(message):
    if not message.isdigit():
        return False
    elif int(message) == 0:
        return False
    return True


def check_good_func(message):
    for good in Good.select():
        if good.name == message.text:
            order_dir_path = os.path.abspath('orders')
            file_path = os.path.join(
                order_dir_path,
                f'{message.from_user.id} {datetime.now().strftime("%Y.%m.%d %H_%M_%S")}.txt'
            )

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(message.text)

            print(f'Пользователь с id {message.from_user.id} сделал заказ. Заказ сохранен в файле {file.name}.')

            return 'Ваш заказ сформирован. Здесь какая-то инструкция, как получить товар.'

    return 'Такого товара нет ☹️\nПопробуйте еще раз.'


def show_my_orders_func(message):
    listfiles = []
    output_message = 'Ваши заказы:\n'
    order_dir_path = os.path.abspath('orders')

    for file in os.listdir(order_dir_path):
        if file.startswith(f'{message.from_user.id}'):
            listfiles.append(file)
    for file_name in listfiles:
        file_path = os.path.join(order_dir_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                output_message += f'{line}\n'
    return output_message


def history_input_func(message):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    History.create(user_id=message.from_user.id, datetime=date, message=message.text)


def history_output_func(message):
    output_message = 'История Ваших последних 10 запросов:\n'
    for history in (History.select().order_by(History.datetime.desc())
            .where(History.user_id == message.from_user.id).limit(10)):
        output_message += f'{history.datetime} {history.message}\n'

    return output_message


def statistics_input_func(message):
    with open('request_statistics.json', 'r', encoding='utf-8') as file:
        new_dict = json.load(file)
        if message not in new_dict:
            new_dict[message] = 0
        new_dict[f'{message}'] += 1

    with open('request_statistics.json', 'w', encoding='utf-8') as file:
        json.dump(new_dict, file, indent=4, ensure_ascii=False)
