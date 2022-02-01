import doctest


def my_abs(val):
    """
    Get the absolute value of a number.
    :param val: input number
    :return: abs number of the input number

    Example:
    >>> my_abs(1)
    1
    >>> my_abs(-1)
    1
    >>> my_abs(0)
    0
    """

    if val >= 0:
        return val
    else:
        return -val


if __name__ == '__main__':
    doctest.testmod()
