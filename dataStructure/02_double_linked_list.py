from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self) -> str:
        return f'{self.data}'


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        Examples:

        >>> linked_list = DoubleLinkedList()
        >>> linked_list.insert_head('b')
        >>> linked_list.insert_head('a')
        >>> linked_list.insert_tail('c')
        >>> tuple(linked_list)
        ('a', 'b', 'c')
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __str__(self) -> str:
        """
        Examples:

        >>> linked_list = DoubleLinkedList()
        >>> linked_list.insert_tail('a')
        >>> linked_list.insert_tail('b')
        >>> linked_list.insert_tail('c')
        >>> str(linked_list)
        'a->b->c'
        """
        return '->'.join([str(item) for item in self])

    def __len__(self) -> int:
        """
        Examples:

        >>> linked_list = DoubleLinkedList()
        >>> for i in range(0, 5):
        ...    linked_list.insert_tail(i)
        >>> len(linked_list) == 5
        True
        """
        return len(tuple(iter(self)))

    def insert_head(self, data: Any) -> None:
        """
        Add data into the begining of the list.

        Examples:

        >>> linked_list = DoubleLinkedList()
        >>> linked_list.insert_head('a')
        >>> linked_list.insert_head('b')
        >>> linked_list.insert_head('c')
        >>> str(linked_list)
        'c->b->a'
        """
        return self.insert_nth(0, data)

    def insert_tail(self, data: Any) -> None:
        """
        Add data into the end of the list.

        Examples:

        >>> linked_list = DoubleLinkedList()
        >>> linked_list.insert_tail('a')
        >>> linked_list.insert_tail('b')
        >>> linked_list.insert_tail('c')
        >>> str(linked_list)
        'a->b->c'
        """
        return self.insert_nth(len(self), data)

    def insert_nth(self, index: int, data: Any) -> None:
        """
        Insert data into the nth node of the list

        :param index: index of node to insert
        :param data: data to insert

        Examples:

        >>> linked_list = DoubleLinkedList()
        >>> for i in range(0, 5):
        ...    linked_list.insert_tail(i)
        >>> str(linked_list)
        '0->1->2->3->4'
        >>> linked_list.insert_nth(2, 'second')
        >>> str(linked_list)
        '0->1->second->2->3->4'
        """
        if not 0 <= index <= len(self):
            raise IndexError('List index out of range.')

        new_node = Node(data)
        if self.head is None:  # Notice: remember to assign both head and tail.
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        elif index == len(self):
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.previous.next = new_node
            new_node.previous = temp.previous
            temp.previous = new_node
            new_node.next = temp

    def delete_head(self) -> Any:
        """
        Delete the head node and return the data.
        :return: data of the head node.

        Examples:

        >>> linked_list = DoubleLinkedList()
        >>> linked_list.insert_tail('a')
        >>> linked_list.insert_tail('b')
        >>> linked_list.insert_tail('c')
        >>> linked_list.delete_head()
        'a'
        """
        return self.delete_nth(0)

    def delete_tail(self) -> Any:
        """
        Delete the tail node and return the data.
        :return: data of the tail node.

        Examples:

        >>> linked_list = DoubleLinkedList()
        >>> linked_list.insert_tail('a')
        >>> linked_list.insert_tail('b')
        >>> linked_list.insert_tail('c')
        >>> linked_list.delete_tail()
        'c'
        """
        return self.delete_nth(len(self) - 1)

    def delete_nth(self, index: int) -> Any:
        """
        Delete the node at the given index.

        :param index: index of node to delete.
        :return: data of the deleted node.

        Examples:

        >>> linked_list = DoubleLinkedList()
        >>> linked_list.insert_tail('a')
        >>> linked_list.insert_tail('b')
        >>> linked_list.insert_tail('c')
        >>> linked_list.delete_nth(1)
        'b'
        >>> str(linked_list)
        'a->c'
        """
        if not 0 <= index <= len(self) - 1:
            raise IndexError('List index out of range')

        delete_node = self.head
        if len(self) == 1:
            self.tail = self.head = None
        elif index == 0:
            self.head = delete_node.next
            self.head.previous = None
        elif index == len(self) - 1:
            delete_node = self.tail
            self.tail = delete_node.previous
            self.tail.next = None
        else:
            for _ in range(index):
                delete_node = delete_node.next
            delete_node.previous.next = delete_node.next
            delete_node.next.previous = delete_node.previous
        return delete_node.data

    def delete(self, data: Any) -> str:
        """
        Delete the node having the given data.

        :param data: data of the node to delete.
        :return: string of the node's data or error if not found.

        Examples:

        >>> linked_list = DoubleLinkedList()
        >>> linked_list.insert_tail('a')
        >>> linked_list.insert_tail('b')
        >>> linked_list.insert_tail('c')
        >>> linked_list.delete('b')
        'b'
        >>> str(linked_list)
        'a->c'
        """
        current = self.head

        while current.data != data:
            if current.next is not None:
                current = current.next
            else:
                return "No data matching the given value"

        if current == self.head:
            self.delete_head()
        elif current == self.tail:
            self.delete_tail()
        else:
            current.previous.next = current.next
            current.next.precious = current.previous
        return str(current.data)

    def is_empty(self) -> bool:
        """
        Determine if the list is empty.
        :return: true when empty.

        Examples:

        >>> linked_list = DoubleLinkedList()
        >>> linked_list.is_empty()
        True
        >>> linked_list.insert_tail('a')
        >>> linked_list.is_empty()
        False
        """
        return len(self) == 0
