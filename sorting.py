def sort_tasks_by_priority(tasks):
    """
    returns a new list of tasks sorted by priority:
    High > Medium > Low
    """
    priority_rank = {"High": 0, "Medium": 1, "Low": 2}

    return sorted(
        tasks,
        key=lambda t: (priority_rank.get(t.get("priority"), 999), t.get("id", 0))
    )