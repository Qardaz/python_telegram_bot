from database.database_models import Good
import os
from datetime import datetime


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

            return (
                'Ваш заказ успешно сформирован и будет доступен к выдаче в течении недели по адресу: '
                'ул. Пушкина, дом Колотушкина.\n'
                'Вы можете обсудить с продавцом альтернативный способ получить Ваш заказ, '
                'позвонив по телефону: 8 (800) 555 35-35.'
            )

    return 'Такого товара нет ☹️\nПопробуйте еще раз.'
