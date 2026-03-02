from mark_complete import mark_complete
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
        print("3. Exit")
        print("4. Mark Task Complete")
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
            print("Exiting...")
            break
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark complete: "))
                mark_complete(tasks, task_id, save_tasks)
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

if __name__ == "__main__":
    add_task("Task 1")            # Medium by default
    add_task("Task 2", "High")    # High
    add_task("Task 3", "Low")     # Low

    set_priority(1, "Low")        # Task 1 → Low
    set_priority(2, "Medium")     # Task 2 → Medium
    set_priority(4, "High")       # ID 4 doesn't exist
    set_priority(2, "Urgent")     # Invalid priority