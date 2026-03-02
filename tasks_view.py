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
    # temporary in-memory storage for tasks
    test_tasks = [
    {'id': 1, 'description': 'Test task', 'priority': 'High', 'completed': False},
    {'id': 2, 'description': 'Another task', 'priority': 'Low', 'completed': True}
]
    view_tasks(test_tasks)