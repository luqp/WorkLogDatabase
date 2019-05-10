from datetime import datetime

from database.employees import db, Employee
from database.registers import Register
from enum_fields import Field


register = Register(Employee)



def init_conection():
    db.connect()
    db.create_tables([Employee], safe=True)


def add_to_register(employee):
    print(len(Employee))
    minutes = int(employee["time_work"])
    employee["time_work"] = minutes
    register.add_to_database(employee)


def search_for_list(field, value):
    if not value or value.isspace():
        raise ValueError
    format_date = "%m/%d/%y"
    if field == "date":
        value = datetime.strptime(value, format_date).date()
    if field == "time_work":
        value = int(value)
    for type_field in Field:
        if field == type_field.value:
            enum_field = type_field
            break
    return register.get_workers_by(enum_field, value)
