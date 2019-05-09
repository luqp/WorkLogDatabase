from database.employees import db, Employee
from work.work_log import WorkLog, Field

work = WorkLog()

def print_by_name(field, value):
    
    workers = work.get_workers_by(field, value)
    work.display_group(workers)

def view_entries():
    
    field = input("Select field > ")


def edit_fields(worker):
    while True:
        for field in Field:
            work.display_group([worker])
            input_user = input(f"[S]elec {field.name}, [c]ontinue: ")
            if input_user == "q":
                return


def options_to_delete(worker):
    while True:
        input_user = input(f"[S]elec varios, or 1: ")
        if input_user == "s":
            value = input("insert value > ")
            print(work.delete_many(Field.NAME, value))
        if input_user == '1':
            print(work.delete_worker(worker))
        if input_user == "q":
            return


def prompting_to_user(worker_id):
    selection = input("[D]elete or [E]dit: ")
    worker = Employee.get_by_id(worker_id)
    if selection.upper() == "D":
        options_to_delete(worker)
    elif selection.upper() == "E":
        edit_fields(worker)

def add_entry():
    work.add_to_database(collect_data())

def collect_data():
    worker = {}
    for field in Field:
        worker[field.value] = wait_valid_input(field.value)
    
    return worker

def wait_valid_input(field):
    while True:
        value = input(f"{field} > ")
        if value and not value.isspace() or value.lower() == "quit":
            return value
        print("Error")
        
def select_an_option():
    options = {
        'A': add_entry,
        'V': view_entries,
        'D': options_to_delete,
        'E': edit_fields
    }
    print(f"[A]dd, [V]iew")
    option = input("> ")



    print(f"[D]elect, [E]dit, [M]ove:")
    option = input("> ")


def start_app():
    if not len(Employee):
        add_entry()
    select_an_option()
    print(len(Employee))
    print("There are data :P")

if __name__ == "__main__":
    db.connect()
    db.create_tables([Employee], safe=True)

    start_app()