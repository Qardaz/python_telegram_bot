from goods import goods


def low_func(how_many):
    new_goods_list = sorted(goods, key=lambda d: d['price'], reverse=False)

    how_many = int(how_many)

    if how_many > len(new_goods_list):
        how_many = len(new_goods_list)

    answer_string = ''

    for i in range(how_many):
        name = new_goods_list[i].get('name')
        price = new_goods_list[i].get('price')
        answer_string += (f'\nНазвание товара: {name}\n'
                          f'Цена товара: {price}$\n')

    return answer_string


# low_func()