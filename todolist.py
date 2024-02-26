def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        file.writelines(tasks)

def add_task(tasks, task):
    tasks.append(task)

def remove_task(tasks, task_index):
    del tasks[task_index]

def print_tasks(tasks):
    if not tasks:
        print("No tasks")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task.strip()}")
def mark_task_as_completed(tasks, task_index):
    if task_index < len(tasks):
        tasks[task_index] = f"COMPLETED: {tasks[task_index].strip()}\n"
    else:
        print("Invalid task number.")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\nTODO LIST")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(tasks, task + "\n")
        elif choice == "2":
            print_tasks(tasks)
            task_index = int(input("Enter the task number to remove: ")) - 1
            remove_task(tasks, task_index)
        elif choice == "3":
            print_tasks(tasks)
        elif choice == "4":
            print_tasks(tasks)
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            mark_task_as_completed(tasks, task_index)
        elif choice == "5":
            save_tasks(filename, tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
