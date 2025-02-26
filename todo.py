# Simple To-Do List App

def load_tasks():
    """Load tasks from a file (if any)."""
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print(f'"{task}" added!')

        elif choice == "2":
            print("\nYour Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")

        elif choice == "3":
            print("\nYour Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")

            task_no = int(input("Enter task number to remove: "))
            if 1 <= task_no <= len(tasks):
                removed_task = tasks.pop(task_no - 1)
                save_tasks(tasks)
                print(f'"{removed_task}" removed!')
            else:
                print("Invalid task number!")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
