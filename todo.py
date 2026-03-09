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

# ===== Task Summary (NEW) =====
def task_summary(tasks):
    """
    US-07 task
    """
    total = len(tasks)
    completed = sum(1 for t in tasks if t.get("completed") is True)
    pending = total - completed
    return {
        "total": total,
        "completed": completed,
        "pending": pending,
    }

def print_task_summary(tasks):
    s = task_summary(tasks)
    print("\n=== TASK SUMMARY ===")
    print(f"Total: {s['total']}")
    print(f"Completed: {s['completed']}")
    print(f"Pending: {s['pending']}")

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

# ----- View tasks -----
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print(f'{"ID":<5} {"Description":<30} {"Priority":<10} {"Completed":<10}')
    print('-' * 60)
    for task in tasks:
        completed_status = 'Yes' if task['completed'] else 'No'
        print(f"{task['id']:<5} {task['description']:<30} {task['priority']:<10} {completed_status:<10}")

# ----- Simple Menu for Testing -----
def main_menu():
    while True:
        print("\n=== TODO LIST MANAGER ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        print("4. Mark Task Complete")
        print("5. Task Summary")  # NEW
        print("6. Edit Task")  #new option for editing tasks
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
        elif choice == "5":  # NEW
            print_task_summary(tasks)
        elif choice == "6":  # Edit task option
            try:
                task_id = int(input("Enter task ID to edit: "))
                new_description = input("Enter new task description: ")
                edit_task(task_id, new_description)
            except ValueError:
                print("Invalid ID. Please enter a number.")
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

# === US-09: edit_task ===
def edit_task(task_id, new_description):
    if not new_description.strip():
        print("Error: Task description cannot be empty!")
        return

    for task in tasks:
        if task['id'] == task_id:
            old_description = task['description']
            task['description'] = new_description
            save_tasks(tasks)
            print(f"Task {task_id} description changed from '{old_description}' to '{new_description}'")
            return
    print(f"Task with id {task_id} not found.")

if __name__ == "__main__":
    main_menu() #start menu

