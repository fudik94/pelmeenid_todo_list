from typing import List, Dict

def mark_complete(tasks: List[Dict], task_id: int, save_function):
    for task in tasks:
        if task["id"] == task_id:

            if task["completed"]:
                print(f"Task {task_id} is already completed.")
                return

            task["completed"] = True
            save_function(tasks)
            print(f"Task {task_id} marked as completed.")
            return

    print(f"Task with id {task_id} not found.")