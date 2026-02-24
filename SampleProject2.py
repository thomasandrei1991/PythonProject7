class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Name : {self.name} \nAge : {self.age}")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
    def info(self):
        super().info()
        print(f"Course : {self.course}")



student = Student("Bryan", 45, "BSCS")
student.info()
