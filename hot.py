from goods import goods

new_goods_list = sorted(goods, key=lambda d: d['orders_quantity'], reverse=True)

how_many = int(input('Сколько товаров вывести? '))

if how_many > len(new_goods_list):
    how_many = len(new_goods_list)

for i in range(how_many):
    name = new_goods_list[i].get('name')
    price = new_goods_list[i].get('price')
    quantity = new_goods_list[i].get('orders_quantity')
    print(f'\nНазвание товара: {name}\n'
          f'Цена товара: {price}$\n'
          f'Количество заказов: {quantity}')
