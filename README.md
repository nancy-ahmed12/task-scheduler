# Task Scheduler Using a Max-Heap

A beginner Python project that simulates a scheduler which always runs the pending task with the highest priority. It implements an array-based max-heap with `INSERT` and `EXTRACT-MAX`, then compares its output with a baseline that re-sorts a regular list after each insertion.

## Task fields

Each task has a name, an integer priority from 1 to 10, and an arrival-time field. For this simple batch simulation, all 20 sample tasks are inserted before execution begins; tasks with equal priority may appear in either order.

## Run

```bash
python task_scheduler.py
```

The program prints the 20 sample tasks, their execution order using each method, and a small timing comparison. The timing is illustrative and can vary by computer; 20 tasks is too small for a meaningful performance conclusion.

## Tests

```bash
python -m unittest test_task_scheduler.py
```

## Complexity

- Heap `INSERT`: O(log n)
- Heap `EXTRACT-MAX`: O(log n)
- Heap storage: O(n)
- Re-sorting the full list after each insertion is less efficient as the number of tasks grows.
