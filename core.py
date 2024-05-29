from datetime import datetime
import json
import os
from goods import goods


def command_func(how_many, reverse=False, sorted_by='price', low_lim=None, high_lim=None):
    goods_list = sorted(goods, key=lambda d: d[sorted_by], reverse=reverse)
    how_many = int(how_many)
    answer_string = ''
    if how_many > len(goods_list):
        how_many = len(goods_list)
        answer_string += 'Введено число, превышающее общее количество товаров. Будут выведены все товары.\n'

    if low_lim and high_lim:
        low_lim, high_lim = int(low_lim), int(high_lim)

        new_goods_list = list()

        if low_lim > high_lim:
            low_lim, high_lim = high_lim, low_lim

        if low_lim == high_lim:
            return 'Верхняя и нижняя границы не могут быть равны. Повторите команду заново.'

        if high_lim - low_lim < how_many:
            how_many = high_lim - low_lim + 1

        if low_lim > how_many:
            return 'Нижняя граница превышает стоимость самого дорогого товара. Повторите команду заново.'

        if high_lim < how_many:
            return 'Верхняя граница ниже стоимости самого дешевого товара. Повторите команду заново.'

        for i in range(len(goods_list)):
            price = goods_list[i].get('price')
            if price >= low_lim and price <= high_lim:
                new_goods_list.append(goods_list[i])

        goods_list = new_goods_list

    for i in range(how_many):
        name = goods_list[i].get('name')
        price = goods_list[i].get('price')
        answer_string += (f'\nНазвание товара: {name}\n'
                          f'Цена товара: {price}$\n')

    return answer_string


def check_message_func(message):
    if not message.isdigit():
        return False
    elif int(message) == 0:
        return False
    return True


def show_all_func():
    output_message = 'Список товаров:\n'

    for good in goods:
        output_message += (
            f'\nНаименование товара: {good["name"]}\n'
            f'Цена товара: {good["price"]}$\n'
        )

    return output_message


def check_good_func(message):
    for good_dict in goods:
        if good_dict['name'] == message.text:
            order_dir_path = os.path.abspath('orders')
            file_path = os.path.join(
                order_dir_path,
                f'{message.from_user.id}_{datetime.now().strftime("%Y.%m.%d %H:%M:%S")}.txt'
            )

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(message.text)

            print(f'Пользователь с id {message.from_user.id} сделал заказ. Заказ сохранен в файле {file.name}.')

            return 'Ваш заказ сформирован. Здесь какая-то инструкция, как получить товар.'

    return 'Такого товара нет ☹️\n Попробуйте еще раз.'


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
    with open('history.txt', 'a', encoding='utf-8') as file:
        date = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
        file.write(f'{date} {message.text} @@@{message.from_user.id}\n')


def history_output_func(message):
    with open('history.txt', 'r', encoding='utf-8') as file:
        output_message = 'История Ваших последних 10 запросов:\n'

        lines = [
            line.rstrip()[:-(len(str(message.from_user.id)) + 4)]
            for line in file
            if f'@@@{message.from_user.id}' in line.rstrip()
        ]

        lines = lines[:-11:-1]
        for line in lines:
            output_message += f'{line}\n'
    return output_message


def statistics_input_func(message):
    with open('request_statistics.json', 'r', encoding='utf-8') as file:
        new_dict = json.load(file)
        # print(new_dict)
        if message not in new_dict:
            new_dict[message] = 0
        # print(new_dict)
        new_dict[f'{message}'] += 1
        # print(new_dict)

    with open('request_statistics.json', 'w', encoding='utf-8') as file:
        json.dump(new_dict, file, indent=4, ensure_ascii=False)
