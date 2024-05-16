from datetime import datetime
import json
from operator import itemgetter

from goods import goods


def command_func(how_many, reverse=False, sorted_by='price', low_lim=None, high_lim=None):
    goods_list = sorted(goods, key=lambda d: d[sorted_by], reverse=reverse)

    if low_lim != None and high_lim != None:
        new_goods_list = list()

        for i in range(len(goods_list)):
            price = goods_list[i].get('price')
            if price > int(low_lim) and price < int(high_lim):
                new_goods_list.append(goods_list[i])

        goods_list = new_goods_list

    how_many = int(how_many)

    if how_many > len(goods_list):
        how_many = len(goods_list)

    answer_string = ''

    for i in range(how_many):
        name = goods_list[i].get('name')
        price = goods_list[i].get('price')
        answer_string += (f'\nНазвание товара: {name}\n'
                          f'Цена товара: {price}$\n')

    return answer_string


def history_input_func(message):
    with open('history.txt', 'a', encoding='utf-8') as file:
        date = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
        file.write(f'{date}: {message.text}\n')


def history_output_func():
    with open('history.txt', 'r', encoding='utf-8') as file:
        output_message = ''
        lines = [line.rstrip() for line in file]
        lines.sort(reverse=True)
        print(lines)
        for i in range(10):
            output_message += f'{lines[i]}\n'

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


def statistics_output_func():
    with open('request_statistics.json', 'r', encoding='utf-8') as file:
        input_dict = json.load(file)
        sorted_dict = dict(sorted(input_dict.items(), key=lambda x: x[1], reverse=True))
        output_message = ''
        for key, value in sorted_dict.items():
            output_message += f'{key}: {value}\n'
        return output_message

# statistics_output_func()