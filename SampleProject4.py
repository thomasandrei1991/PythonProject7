# Simple To-Do List

tasks = []
print("What would you like to do?")
print("1. Add a task")
print("2. View all tasks")
print("3. Quit")
print()
while True:
    choice = input("Enter choice : ").strip()
    if choice == "1":
        task = input("Enter task : ")
        tasks.append(task)
    elif choice == "2":
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Wrong input!")
