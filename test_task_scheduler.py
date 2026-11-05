import unittest
from task_scheduler import MaxHeapScheduler, Task, heap_schedule, sorted_list_schedule


class SchedulerTests(unittest.TestCase):
    def test_empty_extract(self):
        scheduler = MaxHeapScheduler()
        self.assertIsNone(scheduler.extract_max())

    def test_extracts_highest_priority_first(self):
        scheduler = MaxHeapScheduler()
        tasks = [Task("low", 1, 1), Task("urgent", 9, 2), Task("medium", 5, 3)]
        for task in tasks:
            scheduler.insert(task)
        self.assertEqual([scheduler.extract_max().priority for _ in range(3)], [9, 5, 1])

    def test_both_schedulers_return_descending_priorities(self):
        tasks = [Task("a", 3, 1), Task("b", 9, 2), Task("c", 5, 3), Task("d", 7, 4)]
        expected = [9, 7, 5, 3]
        self.assertEqual([t.priority for t in heap_schedule(tasks)], expected)
        self.assertEqual([t.priority for t in sorted_list_schedule(tasks)], expected)

    def test_single_task(self):
        task = Task("only", 4, 1)
        self.assertEqual(heap_schedule([task]), [task])


if __name__ == "__main__":
    unittest.main()
