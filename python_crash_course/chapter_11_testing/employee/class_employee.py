class Employee:
    """Describe an employee"""

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_salary = 5000):
        self.salary += raise_salary