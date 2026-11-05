from dataclasses import dataclass
import random
import time


@dataclass
class Task:
    name: str
    priority: int
    arrival_time: int

    def __str__(self):
        return f"{self.name} (priority={self.priority}, arrival={self.arrival_time})"


class MaxHeapScheduler:
    """Task scheduler backed by an array-based max-heap."""

    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def insert(self, task):
        self.heap.append(task)
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        highest = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return highest

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent].priority >= self.heap[index].priority:
                break
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def _sift_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < size and self.heap[right].priority > self.heap[largest].priority:
                largest = right
            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest


def make_sample_tasks(count=20, seed=42):
    rng = random.Random(seed)
    return [
        Task(name=f"Task-{i:02d}", priority=rng.randint(1, 10), arrival_time=i)
        for i in range(1, count + 1)
    ]


def heap_schedule(tasks):
    scheduler = MaxHeapScheduler()
    for task in tasks:
        scheduler.insert(task)

    order = []
    while len(scheduler):
        order.append(scheduler.extract_max())
    return order


def sorted_list_schedule(tasks):
    """Baseline: re-sort the pending list after each insertion."""
    pending = []
    for task in tasks:
        pending.append(task)
        pending.sort(key=lambda item: item.priority, reverse=True)

    order = []
    while pending:
        order.append(pending.pop(0))
    return order


def show_schedule(title, order):
    print(f"\n{title}")
    print("-" * len(title))
    for position, task in enumerate(order, start=1):
        print(f"{position:2}. {task}")


def compare_methods(tasks):
    start = time.perf_counter()
    heap_order = heap_schedule(tasks)
    heap_seconds = time.perf_counter() - start

    start = time.perf_counter()
    list_order = sorted_list_schedule(tasks)
    list_seconds = time.perf_counter() - start

    print("\nTiming comparison (one small sample; timings vary by computer):")
    print(f"Max-heap scheduler: {heap_seconds:.8f} seconds")
    print(f"Re-sorted list:     {list_seconds:.8f} seconds")
    print("Both methods return tasks in non-increasing priority order.")
    return heap_order, list_order


def main():
    tasks = make_sample_tasks()
    print("Tasks received:")
    for task in tasks:
        print(f"- {task}")

    heap_order, list_order = compare_methods(tasks)
    show_schedule("Execution order using max-heap", heap_order)
    show_schedule("Execution order using re-sorted list", list_order)


if __name__ == "__main__":
    main()
