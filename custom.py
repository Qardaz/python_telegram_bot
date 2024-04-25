from goods import goods

goods_list = sorted(goods, key=lambda d: d['price'], reverse=False)
# print(goods_list)

lower_limit = int(input('Введите нижнюю границу: '))
upper_limit = int(input('Введите верхнюю границу: '))

new_goods_list = list()

for i in range(len(goods_list)):
    price = goods_list[i].get('price')
    if price > lower_limit and price < upper_limit:
        new_goods_list.append(goods_list[i])

# print(new_goods_list)

how_many = int(input('Сколько товаров вывести? '))

if how_many > len(new_goods_list):
    how_many = len(new_goods_list)

for i in range(how_many):
    name = new_goods_list[i].get('name')
    price = new_goods_list[i].get('price')
    print(f'\nНазвание товара: {name}\n'
          f'Цена товара: {price}$')
