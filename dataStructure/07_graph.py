from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar('T')


class Graph(Generic[T]):
    """
    Adjacency list type graph data structure that accounts for directed and undirected graphs.

    Directed graph example:
    >>> d_graph = Graph()
    >>> d_graph
    {}
    >>> d_graph.add_edge(0, 1)
    {0: [1], 1: []}
    >>> d_graph.add_edge(1, 2).add_edge(1, 4).add_edge(1, 5)
    {0: [1], 1: [2, 4, 5], 2: [], 4: [], 5: []}
    >>> d_graph.add_edge(2, 0).add_edge(2, 6).add_edge(2, 7)
    {0: [1], 1: [2, 4, 5], 2: [0, 6, 7], 4: [], 5: [], 6: [], 7: []}

    Undirected graph example:
    >>> u_graph = Graph(directed=False)
    >>> u_graph.add_edge(0, 1)
    {0: [1], 1: [0]}
    >>> u_graph.add_edge(1, 2).add_edge(1, 4).add_edge(1, 5)
    {0: [1], 1: [0, 2, 4, 5], 2: [1], 4: [1], 5: [1]}
    >>> u_graph.add_edge(2, 0).add_edge(2, 6).add_edge(2, 7)
    {0: [1, 2], 1: [0, 2, 4, 5], 2: [1, 0, 6, 7], 4: [1], 5: [1], 6: [2], 7: [2]}
    """
    def __init__(self, directed: bool = True):
        self.adj_list: dict[T, list[T]] = {}
        self.directed = directed

    def add_edge(self, s_ver: T, d_ver: T) -> Graph[T]:
        """
        Connect vertices together by adding edge between source vertex and destination vertex.
        :param s_ver: source vertex.
        :param d_ver: destination vertex.
        :return: graph.
        """
        if not self.directed:
            if s_ver in self.adj_list and d_ver in self.adj_list:
                self.adj_list[s_ver].append(d_ver)
                self.adj_list[d_ver].append(s_ver)
            elif s_ver in self.adj_list:
                self.adj_list[s_ver].append(d_ver)
                self.adj_list[d_ver] = [s_ver]
            elif d_ver in self.adj_list:
                self.adj_list[s_ver] = [d_ver]
                self.adj_list[d_ver].append(s_ver)
            else:
                self.adj_list[s_ver] = [d_ver]
                self.adj_list[d_ver] = [s_ver]

        else:
            if s_ver in self.adj_list and d_ver in self.adj_list:
                self.adj_list[s_ver].append(d_ver)
            elif s_ver in self.adj_list:
                self.adj_list[s_ver].append(d_ver)
                self.adj_list[d_ver] = []
            elif d_ver in self.adj_list:
                self.adj_list[s_ver] = [d_ver]
            else:
                self.adj_list[s_ver] = [d_ver]
                self.adj_list[d_ver] = []
        return self

    def __repr__(self) -> str:
        return str(self.adj_list)
