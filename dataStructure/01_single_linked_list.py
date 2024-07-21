"""
Single linked list is a linear and connected data structure made of node,
each node is composed of a variable data where its content is stored
and a pointer to the next Node on the list.
"""
import doctest
from typing import Any


class Node:
    def __init__(self, data: Any):
        """
        Create and initialize Node class instance.
        Examples:
        >>> Node(20)
        Node(20)
        """
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        """
        Get the string representation of this node.
        Examples:
        >>> Node(10)
        Node(10)
        """
        return f'Node({self.data})'


class LinkedList:
    def __init__(self):
        """
        Create and init LinkedList class instance.
        """
        self.head = None

    def __iter__(self) -> Any:
        """
        This function is intended for iterators to access.
        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail('tail')
        >>> linked_list.insert_tail('tail_1')
        >>> linked_list.insert_tail('tail_2')
        >>> for n in linked_list:
        ...    n
        'tail'
        'tail_1'
        'tail_2'
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        """
        Return length or number of nodes.
        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail('tail')
        >>> linked_list.insert_tail('tail_1')
        >>> linked_list.insert_tail('tail_2')
        >>> len(linked_list)
        3
        """
        return len(tuple(iter(self)))  # iter() only work when __iter__() is defined in a class.

    def __repr__(self) -> str:
        """
        String representation of a linked list.
        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail('tail')
        >>> linked_list.insert_tail('tail_1')
        >>> linked_list.insert_tail('tail_2')
        >>> repr(linked_list)
        'tail->tail_1->tail_2'
        """
        return '->'.join([str(item) for item in self])

    def __getitem__(self, index: int) -> Any:
        """
        Get a node at a particular position.
        :param index: position
        :return: node data
        """
        pass

    def insert_tail(self, data: Any) -> None:
        """
        Insert data to the end of the list.
        :param data: node data
        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail('tail')
        >>> linked_list
        tail
        >>> linked_list.insert_tail('tail_1')
        >>> linked_list
        tail->tail_1
        >>> linked_list.insert_tail('tail_2')
        >>> linked_list
        tail->tail_1->tail_2
        """
        self.insert_nth(len(self), data)

    def insert_head(self, data: Any) -> None:
        """
        Insert data to the begining of the list.
        :param data: node data
        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.insert_head('head')
        >>> linked_list
        head
        >>> linked_list.insert_head('head_1')
        >>> linked_list
        head_1->head
        >>> linked_list.insert_head('head_2')
        >>> linked_list
        head_2->head_1->head
        """
        self.insert_nth(0, data)

    def insert_nth(self, index: int, data: Any) -> None:
        """
        Insert data to the nth position.
        :param index: insert position
        :param data: node data
        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail('first')
        >>> linked_list.insert_tail('second')
        >>> linked_list
        first->second
        >>> linked_list.insert_nth(1, 'third')
        >>> linked_list
        first->third->second
        >>> linked_list.insert_nth(2, 'fourth')
        >>> linked_list
        first->third->fourth->second
        """
        if not 0 <= index <= len(self):
            raise IndexError('List index out of range.')
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def print_list(self) -> None:
        """
        Print every node data.
        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail('first')
        >>> linked_list.insert_tail('second')
        >>> linked_list.insert_tail('third')
        >>> linked_list.insert_tail('fourth')
        >>> linked_list.print_list()
        first->second->third->fourth
        """
        print(self)

    def delete_head(self) -> Any:
        """
        Delete the head node and return the node's data.
        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail('first')
        >>> linked_list.insert_tail('second')
        >>> linked_list.insert_tail('third')
        >>> linked_list.insert_tail('fourth')
        >>> linked_list.delete_head()
        'first'
        """
        return self.delete_nth(0)

    def delete_tail(self) -> Any:
        """
        Delete the tail node and return the node's data.
        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail('first')
        >>> linked_list.insert_tail('second')
        >>> linked_list.insert_tail('third')
        >>> linked_list.insert_tail('fourth')
        >>> linked_list.delete_tail()
        'fourth'
        """
        return self.delete_nth(len(self)-1)

    def delete_nth(self, index: int) -> Any:
        """
        Delete the nth node and return the node's data.
        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail('first')
        >>> linked_list.insert_tail('second')
        >>> linked_list.insert_tail('third')
        >>> linked_list.insert_tail('fourth')
        >>> linked_list.delete_nth(2)
        'third'
        """
        if not 0 <= index <= len(self) - 1:
            raise IndexError('List index out of range')
        delete_node = self.head
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            delete_node = temp.next
            temp.next = delete_node.next
        return delete_node.data

    def is_empty(self) -> bool:
        """
        Check if the linked list is empty.
        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.is_empty()
        True
        >>> linked_list.insert_head('first')
        >>> linked_list.is_empty()
        False
        """
        return self.head is None

    def reverse(self) -> None:
        """
        Reverse the order of the list.
        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail('first')
        >>> linked_list.insert_tail('second')
        >>> linked_list.insert_tail('third')
        >>> linked_list.insert_tail('fourth')
        >>> linked_list.reverse()
        >>> linked_list
        fourth->third->second->first
        """
        prev = None
        current = self.head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next pointer backwards.
            current.next = prev
            # Make the previous node be the current node.
            prev = current
            # Make the current node the next node.
            current = next_node
        self.head = prev


if __name__ == '__main__':
    doctest.testmod()
