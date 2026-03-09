def filter_tasks_by_priority(tasks, priority):
    filtered_tasks = []

    for task in tasks:
        if task["priority"] == priority:
            filtered_tasks.append(task)

    return filtered_tasks
