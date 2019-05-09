import unittest
from work.work_log import WorkLog
from database.employees import db, Employee


class WorkLogTest(unittest.TestCase):
    def setUp(self):
        self.work = WorkLog()
        self.worker1 = {"name": "Lu-1", "task_name": "task-1", "time_work": None, "notes": "Un borreguito"}
        self.worker22 = {"name": "Lu-22", "task_name": "task-22", "time_work": None, "notes": "Un borreguito"}
        db.connect()
        db.create_tables([Employee], safe=True)

    def create_test_add_data(self):
        self.work.add_to_database(Employee, self.worker22)


    def test_check_employee_table(self):
        assert Employee.table_exists()
    
    def test_create_correctly(self):
        self.create_test_add_data()
        self.task_of_emp1 = Employee.get(name="Lu-1")

        self.assertEquals(self.task_of_emp1.task_name, self.worker1['task_name'])

    def test_count_repeat_items(self):
        self.create_test_add_data()
        amout = len(Employee.select().where(Employee.name.contains(22)))
        assert amout == 9

        

if __name__ == '__main__':
    unittest.main()