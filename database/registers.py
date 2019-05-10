import datetime

from enum_fields import Field


class Register():

    def __init__(self, database):
        self.database = database


    def add_to_database(self, data):
        self.database.create(**data)


    def get_workers_by(self, parameter, value):
        workers = self.database.select()
        if parameter == Field.NAME:
            workers_group = workers.where(self.database.name.contains(value))
        elif parameter == Field.DATE:
            workers_group = self.contains_date(workers, value)
        elif parameter == Field.TIME_WORK:
            workers_group = workers.where(self.database.time_work.contains(value))
        elif parameter == Field.OTHERS:
            workers_group = workers.where(self.database.task_name.contains(value))
            workers_group += workers.where(self.database.notes.contains(value))
        return workers_group

    @classmethod
    def contains_date(cls, workers, value):
        for worker in workers:
            if worker.date.date() == value:
                yield worker


    def return_information_of(self, group):
        for employee in group:
            date = employee.date.strftime('%A %B %d, %Y %I:%M%p')
            yield [
                date,
                employee.name, 
                employee.task_name,
                employee.time_work,
                employee.notes
            ]

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
            group_deleted = self.database.delete().where(self.database.name.contains(value))
        if parameter == Field.DATE:
            group_deleted = self.database.delete().where(self.database.date.contains(value))
        if parameter == Field.TIME_WORK:
            group_deleted = self.database.delete().where(self.database.time_work.contains(value))
        if parameter == Field.OTHERS:
            group_deleted = self.database.delete().where(
                                self.database.task_name.contains(value),
                                self.database.notes.contains(value)
                            )
        return group_deleted.execute()

    def update_worker(self, worker, parameter, value):
        if parameter == Field.NAME:
            worker.name = value
        if parameter == Field.DATE:
            worker.date = value
        if parameter == Field.TIME_WORK:
            worker.time_work = value
        if parameter == Field.OTHERS:
            worker.notes = value

        