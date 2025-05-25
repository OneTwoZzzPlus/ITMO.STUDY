from peewee import *

# База данных
db = SqliteDatabase(None, pragmas={'foreign_keys': 1})

class Experiment(Model):
    exp_id = PrimaryKeyField()
    name = CharField()
    
    class Meta:
        database = db

class Meas(Model):
    meas_id = PrimaryKeyField()
    exp_id= ForeignKeyField(Experiment, to_field="exp_id", on_delete='cascade')
    
    name = CharField(null=True)
    char = CharField(null=True)
    unit = CharField(null=True)
    value = FloatField()
    delta = FloatField(null=True)
    epsilon = FloatField(null=True)
    direct = BooleanField(default=False)

    class Meta:
        database = db

# Таблицы базы данных
db_tables = [Experiment, Meas]