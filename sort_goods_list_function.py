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

# print('\n/low', all_in_one_func(5))
# print('\n/high', all_in_one_func(3, reverse=True))
# print('\n/custom', all_in_one_func(7, low_lim= 3, high_lim=6))
# print('\n/hot', all_in_one_func(9, sorted_by='orders_quantity'))
