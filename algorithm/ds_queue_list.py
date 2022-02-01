from typing import Any


class Queue:
    """Queue on list: First In, First Out"""

    def __init__(self):
        self.entries = []

    def __str__(self) -> str:
        return '<'.join([str(x) for x in self.entries])

    def enqueue(self, item) -> None:
        """
        Add the given item into the queue.

        Examples:

        >>> q = Queue()
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> str(q)
        '1<2'
        """
        self.entries.append(item)

    def dequeue(self) -> Any:
        """
        Pull the front element in the queue and return its value.

        :return: value of the front element.

        Examples:

        >>> q = Queue()
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q.dequeue()
        1
        >>> str(q)
        '2'
        >>> q.dequeue()
        2
        >>> str(q)
        ''
        """
        if len(self.entries) == 0:
            return 'queue underflow'
        front = self.entries[0]
        if len(self.entries) == 1:
            self.entries = []
        else:
            self.entries = self.entries[1:]
        return front

    def get_front(self) -> Any:
        """
        Get the value of the front element.

        Examples:

        >>> q = Queue()
        >>> q.get_front()
        'empty queue'
        >>> q.enqueue('a')
        >>> str(q)
        'a'
        """
        if len(self.entries) == 0:
            return 'empty queue'
        else:
            return self.entries[0]
