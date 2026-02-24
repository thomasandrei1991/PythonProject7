def do_task(tasks):
    while True:
        task = input("\nEnter a task (or type 'quit' to go back): ").strip()
        if task.lower() in ["quit", "q", "back"]:
            print("Returning to menu...\n")
            return  # ← goes back to menu
        if task:  # ignore empty inputs
            tasks.append(task)
            print(f"Added: {task}")
        else:
            print("Please enter something or 'quit'.")

def show_task(add_tasks):
    print("\nYour tasks:")
    if not tasks:
        print("   (no tasks yet)")
    else:
        for i, t in enumerate(add_tasks, 1):
            print(f"  {i}. {t}")
    print()  # empty line for readability


# ────────────────────────────────────────────────
# Main program
# ────────────────────────────────────────────────

tasks = list() # ← important: create the list here
print("===== TO-DO LIST =====")
while True:
    print("Options:")
    print("  [1] Add Task")
    print("  [2] View Task List")
    print("  [3] Quit")

    select = input("Enter your choice (1-3): ").strip()

    if select == "1":
        do_task(tasks)

    elif select == "2":
        show_task(tasks)

    elif select == "3":
        print("\nGoodbye! See you next time.")
        break  # ← exit the whole program
    else:
        print("Invalid choice. Please enter 1, 2 or 3.")

