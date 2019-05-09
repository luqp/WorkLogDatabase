from peewee import *

import datetime


db = SqliteDatabase('employees.db')


class Employee(Model):

    name = CharField(max_length=255)
    task_name = CharField(max_length=255)
    time_work = DateTimeField(default=datetime.datetime.now)
    notes = TextField(default="")

    class Meta:
        database = db
