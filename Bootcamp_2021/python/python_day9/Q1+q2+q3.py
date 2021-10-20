class Employee:
    raise_percentage = 10

    @classmethod
    def raise_percentage1(cls, raise_p):
        cls.raise_percentage = raise_p

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "." + last + "@tothenew.com"

    def raise_salary(self):
        self.salary = self.salary + (
            self.salary * Employee.raise_percentage) / 100


emp1 = Employee("Tim", "cook", 10000)
print(emp1.email)
Employee.raise_percentage1(5)
emp1.raise_salary()
print(emp1.salary)
