from __future__ import annotations


class Tree:
    """
    A node in a tree has data variable and pointers to Nodes to its left and right.

    Examples:

    >>> tree = Tree(1)
    >>> tree.left = Tree(2)
    >>> tree.right = Tree(3)
    >>> tree.left.left = Tree(5)
    >>> tree.left.right = Tree(10)
    >>> str(tree.display())
    5 2 10 1 3 'None'
    >>> tree.depth()
    2
    """
    def __init__(self, data: int):
        self.data = data
        self.left: Tree | None = None
        self.right: Tree | None = None

    def display(self) -> None:
        """
        In order traversal of the tree.
        """
        if self.left is None:
            if self.right is None:
                print(str(self.data), end=' ')
            else:
                print(str(self.data), end=' ')
                self.right.display()
        else:
            if self.right is None:
                self.left.display()
                print(str(self.data), end=' ')
            else:
                self.left.display()
                print(str(self.data), end=' ')
                self.right.display()

    def depth(self) -> int:
        """
        Return the depth of a binary tree.
        """
        if self.left is None:
            if self.right is None:
                return 0
            else:
                return 1 + self.right.depth()
        else:
            if self.right is None:
                return 1 + self.left.depth()
            else:
                return 1 + max(self.left.depth(), self.right.depth())
