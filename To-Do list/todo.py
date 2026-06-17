def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

while True:
    print("\n----- TO-DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"'{removed}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Try again.")