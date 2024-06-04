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


class Message(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    message = CharField()

    class Meta:
        db_table = 'messages'


class History(BaseModel):
    id = PrimaryKeyField()
    user_id = IntegerField()
    datetime = DateTimeField(formats='%Y-%m-%d %H:%M:%S')
    message = CharField()
