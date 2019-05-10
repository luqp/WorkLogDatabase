
import sys

from collections import OrderedDict

from data_handler import *
from console_ui.show_in_console import Printer

fields = ["name", "task_name", "time_work", "notes" ]




def menu_loop(options):
    while True:
            choice = input("> ").lower().strip()
            if choice == 'q':
                break
            if choice in options:
                return options[choice]


def wait_valid_input(field):
    while True:
        if field == "notes":
            Printer.show_optional_value()
        value = input(f"{field} > ")

        is_value = value if field != "notes" else True 

        if is_value and not value.isspace():
            return value
        print("Error")

def collect_value(options):
    field_to_search = menu_loop(options)
    value = input("Value > ")
    return field_to_search, value

def view_data():
    search = {
        'n': "name",
        'd': "date",
        't': "time_work",
        'o': "others"
    }
    field_to_search, value = collect_value(search)
    while True:
        try:
            employees = search_for_list(field_to_search, value)
        except TypeError:
            Printer.show_error_of_data()
        except ValueError:
            Printer.show_error_of_data()
        else:
            workers = []
            for emp in employees:
                workers.append(emp)
            if not show_and_selecte_item(workers):
                return


def edit_fields(worker):
    fields_to_edit = {
        'd': "date",
        'w': "task_name",
        't': "time_work",
        'n': "notes"
    }
    while True:
        Printer.print_one_item(worker)
        field_to_search, value = collect_value(fields_to_edit)
        try:
            update_field(worker, field_to_search, value)
        except ValueError:
            Printer.show_error_of_data()


def show_and_selecte_item(employees):
    for employee in employees:
        group = handle_employee_data(employees)
        Printer.print_information(group, employee)

        choice = input(": ")
        if choice == "q":
            return False
        elif choice == 'd':
            Printer.prompting_by_delete()
            Printer.show_result(delete_entry(employee, input(": ")))
        elif choice == 'c':
            Printer.print_one_item(employee)
            input(": ")
        elif choice == 'e':
            edit_fields(employee)
    return True


def collect_data():
    worker = {}
    for field in fields:
        worker[field] = wait_valid_input(field)
    return worker


def add_entry():
    try:
        add_to_register(collect_data())
    except ValueError:
        Printer.show_error_of_data()
    else:
        Printer.added_successfully()



def start_app():
    actions = OrderedDict([
        ('a', add_entry),
        ('v', view_data)
    ])
    Printer.print_menu()
    action = menu_loop(actions)
    action()

if __name__ == "__main__":
    init_conection()
    start_app()