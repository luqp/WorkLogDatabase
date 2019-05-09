import datetime

from enum import Enum

from database.employees import Employee


class Field(Enum):
    NAME = "name"
    TASK_NAME = "task_name"
    TIME_WORK = "time_work"
    DATE = "date"
    NOTES = "notes"
    TERM = "term"

class WorkLog():

    def add_to_database(self, data):
        Employee.create(**data)
        return len(Employee)

    def get_workers_by(self, parameter, value):
        workers = Employee.select()
        if parameter == Field.NAME:
            workers_group = workers.where(Employee.name.contains(value))
        if parameter == Field.DATE:
            workers_group = workers.where(Employee.date.contains(value))
        if parameter == Field.TIME_WORK:
            workers_group = workers.where(Employee.time_work.contains(value))
        if parameter == Field.TERM:
            workers_group = workers.where(
                                Employee.task_name.contains(value),
                                Employee.notes.contains(value)
                            )
        return workers_group

    def display_group(self, group):
        for worker in group:
            date = worker.time_work.strftime('%A %B %d, %Y %I:%M%p')
            print(f"name: {worker.name}")
            print(f"date: {date}")
            print(f"notes: {worker.notes}")
            print("-"*20)

    def delete_worker(self, worker):
        try:
            que = worker.delete_instance()
        except:
            return None
        else:
            return que.execute()
        
        

    def delete_many(self, parameter, value):
        group_deleted = None
        if parameter == Field.NAME:
            group_deleted = Employee.delete().where(Employee.name.contains(value))
        if parameter == Field.DATE:
            group_deleted = Employee.delete().where(Employee.date.contains(value))
        if parameter == Field.TIME_WORK:
            group_deleted = Employee.delete().where(Employee.time_work.contains(value))
        if parameter == Field.TERM:
            group_deleted = Employee.delete().where(
                                Employee.task_name.contains(value),
                                Employee.notes.contains(value)
                            )
        return group_deleted.execute()

    def update_worker(self, worker, parameter, value):
        if parameter == Field.NAME:
            worker.name = value
        if parameter == Field.DATE:
            worker.date = value
        if parameter == Field.TIME_WORK:
            worker.time_work = value
        if parameter == Field.TERM:
            worker.notes = value

        