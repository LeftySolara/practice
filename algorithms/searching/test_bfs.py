import unittest
from undirected_graph import UndirectedGraph
from bfs import bfs


class TestBFS(unittest.TestCase):

    def setUp(self):
        self.graph = UndirectedGraph()

        for i in range(6):
            self.graph.add_vertex(i+1)

        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 4)
        self.graph.add_edge(2, 4)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(4, 3)
        self.graph.add_edge(3, 6)
        self.graph.add_edge(4, 5)
        self.graph.add_edge(5, 6)

    def test_search(self):
        self.assertTrue(bfs(self.graph, 1, 6))
        self.assertFalse(bfs(self.graph, 1, 10))
