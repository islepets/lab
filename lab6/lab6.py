from peewee import *

db = PostgresqlDatabase('rpp_lab6', user='postgres', password='123', host='localhost', port=5433)


class BaseModel(Model):
    class Meta:
        database = db


class Data(BaseModel):
    id = IntegerField(primary_key=True)
    number = CharField()
    request = CharField()
    answer = BooleanField()


db.connect()
db.create_tables([Data], safe=True)

