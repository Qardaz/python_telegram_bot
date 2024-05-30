from peewee import *
import os

database_dir_path = os.path.abspath('database')
database_path = os.path.join(database_dir_path, 'database.db')

db = SqliteDatabase(database_path)


class BaseModel(Model):
    class Meta:
        database = db


class Good(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    price = FloatField()
    order_quantity = IntegerField()

    class Meta:
        db_table = 'goods'


# Good.create_table()
#
# Good.create(id=0, name='name_0', price=0, order_quantity=0)
# Good.create(id=1, name='name_1', price=1, order_quantity=1)
# Good.create(id=2, name='name_2', price=2, order_quantity=2)
# Good.create(id=3, name='name_3', price=3, order_quantity=3)
# Good.create(id=4, name='name_4', price=4, order_quantity=4)
# Good.create(id=5, name='name_5', price=5, order_quantity=5)
# Good.create(id=6, name='name_6', price=6, order_quantity=6)
# Good.create(id=7, name='name_7', price=7, order_quantity=7)
# Good.create(id=8, name='name_8', price=8, order_quantity=8)
# Good.create(id=9, name='name_9', price=9, order_quantity=9)

#############################################################


class Message(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    message = CharField()

    class Meta:
        db_table = 'messages'


# Message.create_table()
#
# Message.create(id=0,
#                name='help',
#                message='''
#                Команды:
#                /start - начало работы
#                /help - помощь
#                /history - вывод последних 10 Ваших сообщений, адресованных боту
#
#                Просмотр товаров:
#                /show_all_goods - вывод списка всех товаров;
#                /low - сортировка товаров по возрастанию цены;
#                /high - сортировка товаров по убыванию цены;
#                /hot - сортировка товаров по убыванию количества заказов;
#                /custom - сортировка товаров по возрастанию цены в интервале цен;
#
#                Работа с заказами:
#                /buy - покупка товара;
#                /show_my_orders - вывод моих заказов.
#                '''
#                )
#
# Message.create(
#     id=1,
#     name='start',
#     message='Привет! Чтобы получить полный список команд, посмотрите в меню или воспользуйтесь командой /help.'
# )
#
# Message.create(id=2,
#                name='how_many_goods',
#                message='Сколько товаров вывести?'
#                )
#
# Message.create(id=3,
#                name='low_lim',
#                message='Введите нижнюю границу цен.'
#                )
#
# Message.create(id=4,
#                name='high_lim',
#                message='Введите верхнюю границу цен.'
#                )
#
# Message.create(id=5,
#                name='buy',
#                message='Какой товар Вы хотели бы приобрести?'
#                )
#
# Message.create(id=6,
#                name='error_how_many',
#                message='Ошибка ввода. Пожалуйста, введите положительное целое число.'
#                )

#######################################################################################


class History(BaseModel):
    id = PrimaryKeyField()
    user_id = IntegerField()
    datetime = DateTimeField(formats='%Y-%m-%d %H:%M:%S')
    message = CharField()


# History.create_table()
