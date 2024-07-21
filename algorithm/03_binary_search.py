from __future__ import annotations
import bisect


def binary_search(lst: list[int], value: int) -> int | None:
    """
    Search the index of a value in a list.
    Note: only work for int assceding list and no duplicate values exist.

    :param lst: some ascending list
    :param value: value to search
    :return: index of value or None if value is not found.

    Examples:

    >>> binary_search([1, 2, 3 ,4, 5, 7, 8, 9], 8)
    6
    >>> lst_test = list(range(0, 10000, 2))
    >>> binary_search(lst_test, 9000)
    4500
    >>> binary_search(lst_test, 10000)

    >>> binary_search(lst_test, 1)

    >>> binary_search(lst_test, -2)

    """
    lst.sort()
    lo = 0
    hi = len(lst) - 1

    while lo <= hi:  # Notice 1: <=, not <
        # Notice 2: using lo + (hi - lo) // 2 not (hi + lo) // 2 to avoid the value out of range.
        mid = lo + (hi - lo) // 2  # integer division: 5 // 2 == 2
        if lst[mid] == value:
            return mid
        elif lst[mid] < value:
            lo = mid + 1
        elif lst[mid] > value:
            hi = mid - 1
    return None


def bisect_left(lst: list[int], value: int, lo: int = 0, hi: int = -1) -> int:
    """
    Locates the first element in a ascending array that is >= a given value.
    Note: no duplicates in the list.

    :param lst: some ascending list.
    :param value: value to search.
    :param lo: lowest index in lst[lo:hi].
    :param hi: highest index in lst[lo:hi].
    :return: index of the first found value or the list length if the given value is out of range.

    Examples:

    >>> bisect_left([0, 1, 3, 5, 7, 9], 0)
    0
    >>> bisect_left([1, 2, 3, 5, 7, 9], 8)
    5
    >>> bisect_left([0, 1, 3, 5, 7, 9], 10)
    6
    >>> bisect_left([0, 1, 3, 5, 7, 9], 8, 1, 3)
    3
    >>> bisect_left([0, 1, 3, 5, 7, 9], 1, 2)
    2
    """
    if hi == -1:
        hi = len(lst)  # Notice 1: difference from normal binary search.

    while lo < hi:  # Notice 2: difference from normal binary search.
        mid = lo + (hi - lo) // 2
        if lst[mid] < value:
            lo = mid + 1
        else:
            hi = mid  # Notice 3: difference from normal binary search.
    return lo  # Notice 4: difference from normal binary search.


def bisect_right(lst: list[int], value: int, lo: int = 0, hi: int = -1) -> int:
    """
    Locates the first value in a ascending array that is > a given value.
    Note: no duplicates in the list.

    :param lst: some ascending list.
    :param value: value to search.
    :param lo: lowest index in lst[lo:hi].
    :param hi: highest index in lst[lo:hi].
    :return: index of the first found value or the list length if out of range.

    Examples:

    >>> bisect_right([0, 1, 3, 5, 7, 9], 0)
    1
    >>> bisect_right([1, 2, 3, 5, 7, 9], 8)
    5
    >>> bisect_right([0, 1, 3, 5, 7, 9], 10)
    6
    >>> bisect_right([0, 1, 3, 5, 7, 9], 8, 1, 3)
    3
    >>> bisect_right([0, 1, 3, 5, 7, 9], 0, 2)
    2
    """
    if hi == -1:
        hi = len(lst)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if lst[mid] <= value:
            lo = mid + 1
        else:
            hi = mid
    return lo


def binary_search_std_lib(lst: list[int], value: int) -> int | None:
    """
    Implementation of binary search in Python stdlib.

    :param lst: some ascending list
    :param value: value to search
    :return: index of value or None if not found.

    Examples:

    >>> binary_search([1, 2, 3 ,4, 5, 6, 7, 8], 2)
    1
    >>> lst_test = list(range(0, 10000, 2))
    >>> binary_search(lst_test, 9000)
    4500
    >>> binary_search(lst_test, 10000)

    >>> binary_search(lst_test, 1)

    >>> binary_search(lst_test, -2)

    """
    index = bisect.bisect_left(lst, value)
    if index != len(lst) and lst[index] == value:
        return index
    return None


def insort_left(lst: list[int], value: int, lo: int = 0, hi: int = -1) -> None:
    """
    Insert a given value into a sorted list. If same values exist, insert in the first position.

    :param lst: some ascending list.
    :param value: value to insert.
    :param lo: lowest index of the list.
    :param hi: highest index of the list.

    Examples:

    >>> lst_test = [2, 3, 8, 10, 20]
    >>> insort_left(lst_test, 15)
    >>> lst_test
    [2, 3, 8, 10, 15, 20]
    >>> insort_left(lst_test, 1)
    >>> lst_test
    [1, 2, 3, 8, 10, 15, 20]
    >>> insort_left(lst_test, 10)
    >>> lst_test
    [1, 2, 3, 8, 10, 10, 15, 20]
    """
    index = bisect_left(lst, value, lo, hi)
    lst.insert(index, value)


def insort_right(lst: list[int], value: int, lo: int = 0, hi: int = -1) -> None:
    """
    Insert a given value into a sorted list. If same values exist, insert in the last position.

    :param lst: some ascending list.
    :param value: value to insert.
    :param lo: lowest index.
    :param hi: highest index.

    Examples:
    >>> lst_test = [2, 3, 8, 10, 20]
    >>> insort_left(lst_test, 15)
    >>> lst_test
    [2, 3, 8, 10, 15, 20]
    >>> insort_left(lst_test, 1)
    >>> lst_test
    [1, 2, 3, 8, 10, 15, 20]
    >>> insort_left(lst_test, 10)
    >>> lst_test
    [1, 2, 3, 8, 10, 10, 15, 20]
    """
    index = bisect_right(lst, value, lo, hi)
    lst.insert(index, value)


def binary_search_by_recursion(lst: list[int], value: int, lo: int = 0, hi: int = -1) -> int | None:
    """
    Binary search by recursion.

    :param lst: some ascending list.
    :param value: value to search.
    :param lo: lowest index of the search list.
    :param hi: highest index of the search list.
    :return: index of the given value or None if not found.

    Examples:

    >>> binary_search([1, 2, 3 ,4, 5, 7, 8, 9], 8)
    6
    >>> lst_test = list(range(0, 10000, 2))
    >>> binary_search(lst_test, 9000)
    4500
    >>> binary_search(lst_test, 10000)

    >>> binary_search(lst_test, 1)

    >>> binary_search(lst_test, -2)

    """
    if hi == -1:
        hi = len(lst) - 1

    if lo > hi:
        return None

    mid = lo + (hi - lo) // 2
    if lst[mid] == value:
        return mid
    elif lst[mid] < value:
        return binary_search_by_recursion(lst, value, mid + 1, hi)
    else:
        return binary_search_by_recursion(lst, value, lo, mid - 1)