from datetime import datetime

from database.employees import db, Employee
from database.registers import Register
from enum_fields import Field


register = Register(Employee)



def init_conection():
    db.connect()
    db.create_tables([Employee], safe=True)


def add_to_register(employee):
    minutes = int(employee["time_work"])
    employee["time_work"] = minutes
    register.add_to_database(employee)
    print(len(Employee))

def checking_input_data(field, input_data):
    if not input_data or input_data.isspace():
        raise ValueError
    if field == "date":
        format_date = "%m/%d/%y"
        input_data = datetime.strptime(input_data, format_date)
    if field == "time_work":
        input_data = int(input_data)
    for type_field in Field:
        if field == type_field.value:
            enum_field = type_field
            break
    return enum_field, input_data

def update_field(worker, field, input_data):
    enum_field, value = checking_input_data(field, input_data)
    register.update_worker(worker, enum_field, value)


def search_for_list(field, input_data):
    enum_field, value = checking_input_data(field, input_data)
    if enum_field == Field.DATE:
        value = value.date()
    return register.get_workers_by(enum_field, value)

def handle_employee_data(employees):
    data_to_display = []
    for item in employees:
        try:
            employee = Employee.get_by_id(item.id)
        except:
            continue
        else:
            date = employee.date.strftime("%b/%d/%y")
            handle_data = employee.id, [
                employee.name,
                date,
                employee.task_name
            ]
            data_to_display.append(handle_data)
    return data_to_display


def delete_entry(item, confirmation):
    while True:
        if confirmation.lower() == "borrar":
            item.delete_instance()
            return True
        if confirmation.lower() == 'q':
            return False
        
        confirmation = input(": ")