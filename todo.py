import json
import os

# ----- Load / Save tasks -----
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()

# ----- US-01: add_task() -----
def add_task(description, priority="Medium"):
    if not description.strip():
        print("Error: Task description cannot be empty!")
        return
    if priority not in ["High", "Medium", "Low"]:
        print("Error: Priority must be High, Medium, or Low!")
        return
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "description": description,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{description}' added with ID {task_id} and priority {priority}.")

# ----- Simple Menu for Testing -----
def main_menu():
    while True:
        print("\n=== TODO LIST MANAGER ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        print("5. Clear Completed Tasks")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter priority (High/Medium/Low): ")
            add_task(description, priority)
        elif choice == "2":
            if not tasks:
                print("No tasks yet!")
            for t in tasks:
                status = "Done" if t["completed"] else "Pending"
                print(f"{t['id']}: {t['description']} [{t['priority']}] - {status}")
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == "4":
            print("Exiting...")
            break
        elif choice == "5":
            clear_completed_tasks()
        else:
            print("Invalid option. Try again.")

# === Set priority of a task ===
def set_priority(task_id, new_priority):
    if new_priority not in ["Low", "Medium", "High"]:
        print("Priority must be 'Low', 'Medium', or 'High'")
        return

    for task in tasks:
        if task['id'] == task_id:
            task['priority'] = new_priority
            save_tasks(tasks)
            print(f"Task {task_id} priority set to {new_priority}")
            return
    print(f"Task with id {task_id} not found.")

#=== Delete a task ===
def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} deleted.")
            return
    print(f"Task with id {task_id} is not found.")

# === Clear completed tasks ===
def clear_completed_tasks():
    any_deleted = False # Flag to check if any tasks were deleted
    for task in tasks[:]: # Iterate over a copy of the list
        if task['completed']:
            tasks.remove(task)
            any_deleted = True
    save_tasks(tasks)
    if any_deleted:
        print("All completed tasks have been cleared.")
    else:
        print("No completed tasks to clear.")

if __name__ == "__main__":
    main_menu() #start menu