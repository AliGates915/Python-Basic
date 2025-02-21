import os

# Show tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\n=====> All Tasks <====== \n")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Add task
def add_task(tasks, new_task):
    tasks.append(new_task)
    print("Task added successfully.")

# Update task
def update_task(tasks, index, updated_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = updated_task
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

# Delete task
def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task '{deleted_task}' deleted successfully.")
    else:
        print("Invalid task number.")

# Save tasks to a file
def save_task_file(file_path, tasks):
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

# Load tasks from a file
def load_task(file_path):
    tasks = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            tasks = file.read().splitlines()
    return tasks

def main():
    file_path = 'todo_list.txt'
    tasks = load_task(file_path)
    
    while True:
        print("\n======> To-Do List <=======")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Exit")

        # Choice from the user
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter the task number to update: "))
                updated_task = input("Enter the updated task: ")
                update_task(tasks, index, updated_task)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            show_tasks(tasks)
            try:
                index = int(input("Enter the task number to delete: "))
                delete_task(tasks, index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "5":
            save_task_file(file_path, tasks)
            print("Tasks saved successfully. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
    
