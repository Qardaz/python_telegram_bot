from goods import goods

def custom_func(how_many, lower_limit, upper_limit):
    goods_list = sorted(goods, key=lambda d: d['price'], reverse=False)
    # print(goods_list)

    # lower_limit = int(input('Введите нижнюю границу: '))
    # upper_limit = int(input('Введите верхнюю границу: '))

    new_goods_list = list()

    for i in range(len(goods_list)):
        price = goods_list[i].get('price')
        if price > int(lower_limit) and price < int(upper_limit):
            new_goods_list.append(goods_list[i])

    # print(new_goods_list)

    # how_many = int(input('Сколько товаров вывести? '))

    how_many = int(how_many)

    if how_many > len(new_goods_list):
        how_many = len(new_goods_list)

    answer_string = ''

    for i in range(how_many):
        name = new_goods_list[i].get('name')
        price = new_goods_list[i].get('price')
        answer_string += (f'\nНазвание товара: {name}\n'
                          f'Цена товара: {price}$')

    return answer_string