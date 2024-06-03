from database.database_models import Good
import requests
from peewee import SQL


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
        low_lim = Good.select(Good.price).order_by(Good.price.asc()).limit(1).first().price
        high_lim = Good.select(Good.price).order_by(Good.price.desc()).limit(1).first().price

    if reverse:
        sorted_by += " desc"
    else:
        sorted_by += " asc"

    usd_api_exchange_rate = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json'

    from_currency = 'usd'
    to_currency = 'rub'

    response = requests.get(usd_api_exchange_rate)

    if response.status_code != 200:
        return 'Обменник валют не отвечает ☹️'

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
