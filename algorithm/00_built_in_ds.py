"""
1. Dequeue
2. Heap
"""

# 1. Dequeue
print('*' * 20 + 'Dequeue' + '*' * 20)
import collections

DoubleEnded = collections.deque(["Mon", "Tue", "Wed"])
DoubleEnded.append("Thu")
print("Appended at right: " + str(DoubleEnded))

DoubleEnded.appendleft("Sun")
print("Appended at left: " + str(DoubleEnded))

DoubleEnded.pop()
print("Deleting from right: " + str(DoubleEnded))

DoubleEnded.popleft()
print("Deleting from left: " + str(DoubleEnded))

# 2. Heap
print('*' * 20 + 'Heap' + '*' * 20)
import heapq

H = [21, 1, 45, 78, 3, 5]
heapq.heapify(H)
print(H)  # the smallest in the first position.

heapq.heappush(H, 8)  # always add to the last position.
print(H)

heapq.heappop(H)
print(H)  # remove the element at the first position.

heapq.heapreplace(H, 100)  # remove the smallest and insert the given value randomly.
print(H)


def heapsort(iterable: list):
    """
    Heap sort, unstable sorting.

    :param iterable: list to sort
    :return: sorted list

    Examples:

    >>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


# Heap priority queue.
h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
heapq.heappop(h)


# Change the minHeap of heapq into maxHeap: multiply the values by -1, but only for numeric values.
class MaxHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)
