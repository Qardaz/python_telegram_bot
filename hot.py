from goods import goods


def hot_func(how_many):
    new_goods_list = sorted(goods, key=lambda d: d['orders_quantity'], reverse=True)

    # how_many = int(input('Сколько товаров вывести? '))

    how_many = int(how_many)

    if how_many > len(new_goods_list):
        how_many = len(new_goods_list)

    answer_string = ''

    for i in range(how_many):
        name = new_goods_list[i].get('name')
        price = new_goods_list[i].get('price')
        quantity = new_goods_list[i].get('orders_quantity')
        answer_string += (f'\nНазвание товара: {name}\n'
                          f'Цена товара: {price}$\n'
                          f'Количество заказов: {quantity}\n')

    return answer_string