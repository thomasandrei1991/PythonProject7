def details(student_name, student_course, student_age):
    print(f"Name : {student_name}")
    print(f"Course : {student_course}")
    print(f"Age : {student_age}")

name = input("Enter your name: ")
course = input("Enter your course: ")
age = int(input("Enter your age: "))


details(name, course, age)