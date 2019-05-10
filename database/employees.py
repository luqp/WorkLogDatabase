from peewee import *

import datetime


db = SqliteDatabase('employees.db')


class Employee(Model):

    date = DateTimeField(default=datetime.datetime.now)
    name = CharField(max_length=255)
    notes = TextField(default="")
    task_name = CharField(max_length=255)
    time_work = IntegerField()

    class Meta:
        database = db
