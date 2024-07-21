"""
Time complexity
worst case: O(n^2)
best case: O(n log n)
average case: O(n log n)
"""


def quick_sort(lst: list[int]) -> list:
    """
    Sort a given unsorted list in ascending order.

    :param lst: some unsorted list.
    :return: the same list in ascending order.

    Examples:

    >>> quick_sort([3, 4, 2, 5, 1])
    [1, 2, 3, 4, 5]
    >>> quick_sort([3, 4, 2, 5, 5, 4, 2, 2, 1])
    [1, 2, 2, 2, 3, 4, 4, 5, 5]
    >>> quick_sort([1])
    [1]
    >>> quick_sort([])
    []
    """
    if len(lst) < 2:
        return lst

    pivot = lst.pop()
    greater: list[int] = []
    smaller: list[int] = []
    for value in lst:
        if value > pivot:
            greater.append(value)
        else:
            smaller.append(value)
    return quick_sort(smaller) + [pivot] + quick_sort(greater)
