class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.save()
    def save(self):
        with open("/home/rahul/Visualstudio/python/python_day12/Q2/Student.txt","a") as file:
            file.write(f"{self.name} {self.roll_no} {self.course}\n")

student1 = Student("Rahul", 5248, "CSE")
student2 = Student("Amit", 5249, "IT")
student3 = Student("Aman", 5250, "ME")