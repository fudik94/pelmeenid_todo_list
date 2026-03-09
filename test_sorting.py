'''Unit tests for the sort_tasks_by_priority function in sorting.py. US-10'''


import unittest
from sorting import sort_tasks_by_priority


class TestSortTasksByPriority(unittest.TestCase):
    def test_sorting_orders_high_medium_low(self):
        tasks = [
            {"id": 1, "description": "A", "priority": "Low", "completed": False},
            {"id": 2, "description": "B", "priority": "High", "completed": False},
            {"id": 3, "description": "C", "priority": "Medium", "completed": False},
            {"id": 4, "description": "D", "priority": "High", "completed": True},
        ]

        sorted_tasks = sort_tasks_by_priority(tasks)

        # High > High > Medium > Low
        self.assertEqual([t["id"] for t in sorted_tasks], [2, 4, 3, 1])

    def test_unknown_priority_goes_last(self):
        tasks = [
            {"id": 1, "description": "A", "priority": "Medium", "completed": False},
            {"id": 2, "description": "B", "priority": "Urgent", "completed": False},
            {"id": 3, "description": "C", "priority": "High", "completed": False},
        ]

        sorted_tasks = sort_tasks_by_priority(tasks)
        self.assertEqual([t["id"] for t in sorted_tasks], [3, 1, 2])


if __name__ == "__main__":
    unittest.main()