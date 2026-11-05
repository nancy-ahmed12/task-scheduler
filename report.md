# Task Scheduler Project Report

## Problem
This project simulates a scheduler that selects the pending task with the highest priority. Each task stores a name, an integer priority, and an arrival time.

## Method
I implemented an array-based max-heap with `INSERT` and `EXTRACT-MAX`. The program creates 20 repeatable sample tasks with priorities from 1 to 10, inserts them into the heap, and prints their execution order. As a baseline, it also sorts a regular list after every insertion and removes tasks from the front. Unit tests cover empty extraction, a single task, and execution in descending priority order.

## Complexity Analysis
In a max-heap, the task with the largest priority is at the root. Insertion moves a new task upward by at most the height of the heap, so it takes O(log n). Extracting the maximum replaces the root and moves the replacement downward, also taking O(log n). The heap uses O(n) space. Re-sorting a regular list after every insertion requires more work as the number of tasks grows.

## Experiment and Results
Both scheduling methods produce tasks in non-increasing priority order. The max-heap repeatedly selects the largest priority from its root, while the baseline repeatedly sorts the pending list and removes its first task. If multiple tasks have the same priority, their relative order may differ between the two methods.

The program also reports elapsed times. Since the demonstration uses only 20 tasks, those timings are very small and can vary between runs and computers; they are not enough to establish a reliable speed advantage. The complexity analysis predicts that the heap will scale better for larger workloads because insertion and extraction each take O(log n).

## Conclusion and Reflection
This project demonstrates how a max-heap can support a priority queue for a task scheduler. It provides efficient insertion and selection of the highest-priority task. The comparison also shows why a simple sorted-list approach can be easier to understand while requiring more work as the task queue grows. A useful next step would be to simulate tasks arriving over time and add an aging rule so that tasks waiting longer gradually gain priority.
