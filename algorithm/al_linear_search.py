import doctest
from typing import Any


# Time complexity O(n)
def linear_search(lst: list[Any], element: Any) -> int:
    """
    Search the index of a element in a list, if not, return -1.

    :param lst: some list
    :param element: element to search
    :return: index of the element

    Examples:

    >>> linear_search([123, 2123, 233, 564, 215], 233)
    2
    >>> linear_search(['as', 'cs', 'app', 'no'], 'no')
    3
    """
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1


if __name__ == '__main__':
    doctest.testmod()
