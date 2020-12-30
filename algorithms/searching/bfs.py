"""
Breadth-Fist Search implementation on an undirected graph.
"""

from undirected_graph import UndirectedGraph
import queue


def bfs(graph, root, target):
    """Determines if there is a path from root to target."""

    search_queue = queue.SimpleQueue()
    searched = []

    for neighbor in graph.neighbors(root):
        search_queue.put(neighbor)

    while search_queue.qsize() > 0:
        neighbor = search_queue.get()
        if neighbor not in searched:
            if neighbor == target:
                return True
            else:
                for n in graph.neighbors(neighbor):
                    search_queue.put(n)
                    searched.append(neighbor)

    return False
