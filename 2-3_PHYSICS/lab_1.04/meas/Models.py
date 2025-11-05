from peewee import *

db = SqliteDatabase('test.db')


class MeasurmentDB(Model):
    name = CharField(null=False)
    value = DoubleField(null=False)
    delta = DoubleField(null=False)
    epsilon = DoubleField()

    class Meta:
        database = db


db.connect()

db.drop_tables([MeasurmentDB])
db.create_tables([MeasurmentDB])

