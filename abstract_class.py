from abc import ABC, abstractmethod

class Employee(ABC):
    def emp_name(self, emp_name):
        self.emp_name

    @abstractmethod
    def emp_id(self, emp_id):
        self.emp_id


class Emp_details(Employee):
    def emp_id(self, emp_id):
        print("Employee id :", emp_id)

    def emp_name(self, emp_name):
        print("Employee Name :", emp_name)


emp1 = Emp_details()

emp1.emp_id(555)
emp1.emp_name("RAJ NANJAN")




