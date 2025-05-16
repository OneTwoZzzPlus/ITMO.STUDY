from peewee import *

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

class DMM(Model):
    dmm_id = PrimaryKeyField()
    exp_id= ForeignKeyField(Experiment, to_field="exp_id", on_delete='cascade')
    x = ForeignKeyField(Meas, to_field='meas_id')
    delta_instrument = FloatField()

    class Meta:
        database = db
        
class LMM(Model):
    lmm_id = PrimaryKeyField()
    exp_id= ForeignKeyField(Experiment, to_field="exp_id", on_delete='cascade')
    a = ForeignKeyField(Meas, to_field='meas_id')
    b = ForeignKeyField(Meas, to_field='meas_id')

    class Meta:
        database = db

class ListMeas(Model):
    dmm_id = ForeignKeyField(DMM, to_field='dmm_id', null=True, on_delete='cascade')
    lmm_x_id = ForeignKeyField(LMM, to_field='lmm_id', null=True, on_delete='cascade')
    lmm_y_id = ForeignKeyField(LMM, to_field='lmm_id', null=True, on_delete='cascade')
    meas_id = ForeignKeyField(Meas, to_field='meas_id')
    
    class Meta:
        database = db
        
tables = [Experiment, Meas, DMM, LMM]