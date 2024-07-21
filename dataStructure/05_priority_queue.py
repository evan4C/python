class OverFlowError(Exception):
    pass


class UnderFlowError(Exception):
    pass


class FixedPriorityQueue:
    """
    Tasks can be added to a Priority Queue at any time and in any order, but when tasks are
    removed then the Task with the highest priority is removed in FIFO order.
    There are 3 levels of priority, 0(highest), 1(middle), 2(lowest).

    Examples:

    >>> fpq = FixedPriorityQueue()
    >>> fpq.enqueue(0, 10)
    >>> fpq.enqueue(1, 70)
    >>> fpq.enqueue(0, 100)
    >>> fpq.enqueue(2, 1)
    >>> fpq.enqueue(2, 5)
    >>> fpq.enqueue(1, 7)
    >>> fpq.enqueue(2, 4)
    >>> fpq.enqueue(1, 64)
    >>> fpq.enqueue(0, 128)
    >>> print(fpq)
    Priority 0: [10, 100, 128]
    Priority 1: [70, 7, 64]
    Priority 2: [1, 5, 4]
    """
    def __init__(self):
        self.queues = [
            [],
            [],
            [],
        ]

    def enqueue(self, priority: int, data: int) -> None:
        """
        Add an element to a queue based on its priority.
        """
        if len(self.queues[priority]) >= 100:
            raise OverFlowError
        self.queues[priority].append(data)

    def dequeue(self) -> int:
        """
        Return the highest priority element in FIFO order.
        """
        for queue in self.queues:
            if queue:
                return queue.pop(0)
        raise UnderFlowError

    def __str__(self) -> str:
        return '\n'.join(f'Priority {i}: {q}' for i, q in enumerate(self.queues))
