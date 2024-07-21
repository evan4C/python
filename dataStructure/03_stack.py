from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """
    Stack data structure: Last In, First Out
    """
    def __init__(self, limit: int = 10):
        """
        :param limit: number limit of elements in a stack.
        """
        self.stack: list[T] = []
        self.limit = limit

    def __str__(self) -> str:
        return '>'.join(str(x) for x in self.stack)

    def push(self, data: T) -> None | str:
        """
        Push an element to the top of the stack.

        :param data: data to push.

        Examples:

        >>> s = Stack(10)
        >>> s.push('hu')
        >>> str(s)
        'hu'
        """
        if len(self.stack) >= self.limit:
            return "stack overflow error!"
        self.stack.append(data)

    def pop(self) -> T | str:
        """
        Pop an element off of the top of the stack.

        :return: data of the element to pop.

        Examples:

        >>> s = Stack()
        >>> for i in range(10):
        ...    s.push(i)
        >>> s.pop()
        9
        >>> s.pop()
        8
        >>> str(s)
        '0>1>2>3>4>5>6>7'
        """
        if len(self.stack) == 0:
            return "stack underflow error!"
        return self.stack.pop()

    def peek(self) -> T:
        """
        Peek at the top element of the stack.
        :return:

        Examples:

        >>> s = Stack()
        >>> for i in range(10):
        ...    s.push(i)
        >>> s.peek()
        9
        """
        if len(self.stack) == 0:
            return "stack underflow error!"
        return self.stack[-1]

    def is_empty(self) -> bool:
        """Check if a stack is empty"""
        return len(self.stack) == 0

    def is_full(self) -> bool:
        """check if a stack is full"""
        return len(self.stack) == self.limit
