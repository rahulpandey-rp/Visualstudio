class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.save()
    def save(self):
        with open("/home/rahul/Visualstudio/python/python_day12/Q2/Student.txt","a") as file:
            file.write(f"{self.name} {self.roll_no} {self.course}\n")

    @classmethod
    def open_file(cls):
        with open("/home/rahul/Visualstudio/python/python_day12/Q2/Student.txt","r") as file:
            return(file.read())


file_data = Student.open_file()
print(file_data)

