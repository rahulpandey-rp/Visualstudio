import unittest
from OopsQ1 import Employee


class test_Employee(unittest.TestCase):
    def setUp(self):
        self.emp1 = Employee("Tim", "cook", 10000)

    def test_raisePercentage(self):
        self.assertEqual(Employee.raise_percentage,10)
        Employee.raise_percentage1(12)
        self.assertEqual(Employee.raise_percentage,12)

    def test_init(self):
        self.assertEqual(self.emp1.first, "Tim")
        self.assertEqual(self.emp1.last, "cook")
        self.assertEqual(self.emp1.salary, 10000)
        self.assertEqual(self.emp1.email, "Tim.cook@tothenew.com")

    def test_raise_salary(self):
        Employee.raise_percentage=10
        self.emp1.raise_salary()
        self.assertEqual(self.emp1.salary,11000)


if __name__ == "__main__":
    unittest.main()