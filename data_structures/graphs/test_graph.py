import unittest
from graph import UndirectedGraph


class TestUndirectedGraphMethods(unittest.TestCase):

    def setUp(self):
        self.graph = UndirectedGraph()
        self.filled_graph = UndirectedGraph()

        for i in range(6):
            self.filled_graph.add_vertex(i+1)

        self.filled_graph.add_edge(1, 2)
        self.filled_graph.add_edge(1, 4)
        self.filled_graph.add_edge(2, 4)
        self.filled_graph.add_edge(2, 3)
        self.filled_graph.add_edge(4, 3)
        self.filled_graph.add_edge(3, 6)
        self.filled_graph.add_edge(4, 5)
        self.filled_graph.add_edge(5, 6)

    def test_adjacent(self):
        # Edge does exist.
        self.assertTrue(self.filled_graph.adjacent(1, 2))

        # Edge does not exist.
        self.assertFalse(self.filled_graph.adjacent(1, 3))

        # Vertices to test do not exist.
        self.assertFalse(self.filled_graph.adjacent(5, 8))

    def test_neighbors(self):
        self.assertCountEqual(self.filled_graph.neighbors(4), [1, 2, 3, 5])
        self.assertCountEqual(self.filled_graph.neighbors(6), [3, 5])
        self.assertEqual(self.filled_graph.neighbors(199), [])

    def test_add_vertex(self):
        old_len = len(self.graph)
        self.graph.add_vertex(0)
        self.assertEqual(len(self.graph), old_len + 1)

    def test_remove_vertex(self):
        # Remove a vertex that exists and verify its neighbors are updated.
        target = 6
        old_len = len(self.filled_graph)
        self.filled_graph.remove_vertex(target)

        self.assertEqual(len(self.filled_graph), old_len - 1)
        self.assertNotIn(target, self.filled_graph.vertices)
        self.assertNotIn(target, self.filled_graph.neighbors(3))
        self.assertNotIn(target, self.filled_graph.neighbors(5))

        # Attempt to remove a vertex that doesn't exist.
        target = 100
        old_len = len(self.filled_graph)
        self.filled_graph.remove_vertex(target)
        self.assertEqual(len(self.filled_graph), old_len)
        self.assertNotIn(target, self.filled_graph.vertices)

    def test_add_edge(self):
        # Add edge between existing vertices.
        self.assertFalse(self.filled_graph.adjacent(2, 6))
        self.filled_graph.add_edge(2, 6)
        self.assertTrue(self.filled_graph.adjacent(2, 6))

        # Attempt to add edge to vertex that doesn't exist.
        self.filled_graph.add_edge(2, 100)
        self.assertNotIn(100, self.filled_graph.neighbors(2))

    def test_remove_edge(self):
        # Remove existing edge.
        self.assertIn(3, self.filled_graph.neighbors(6))
        self.filled_graph.remove_edge(3, 6)
        self.assertNotIn(3, self.filled_graph.neighbors(6))

        # Attempt to remove non-existing edge.
        self.assertNotIn(1, self.filled_graph.neighbors(5))
        self.filled_graph.remove_edge(1, 5)
        self.assertNotIn(1, self.filled_graph.neighbors(5))


if __name__ == '__main__':
    unittest.main()
