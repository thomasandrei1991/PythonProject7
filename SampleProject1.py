def information(student_names, student_ages, student_courses):
    print("\tINFORMATION \n======================")
    for name, age, course in zip(student_names, student_ages, student_courses):
        print(f"{name:10} {age:2} \t {course}")


names = ["Bryan", "Lloyd", "Johnson", "Carolina", "Joshua"]
ages = [35, 20, 28, 45, 21]
courses = ["BSIT", "BSCS", "BSTM", "BSBA", "BSHRM"]
information(names, ages, courses)
