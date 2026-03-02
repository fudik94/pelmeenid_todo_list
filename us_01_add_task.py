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
def add_task(description, priority):
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
        else:
            print("Invalid option. Try again.")

# ----- Optional: quick test -----
if __name__ == "__main__":
    main_menu()