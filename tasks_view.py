from us_01_add_task import tasks

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print(f'{"ID":<5} {"Description":<30} {"Priority":<10} {"Completed":<10}')
    print('-' * 60)
    for task in tasks:
        completed_status = 'Yes' if task['completed'] else 'No'
        print(f"{task['id']:<5} {task['description']:<30} {task['priority']:<10} {completed_status:<10}")

if __name__ == "__main__":
    view_tasks(tasks)