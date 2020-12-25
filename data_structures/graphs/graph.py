"""
Basic undirected graph implementations, one using an adjacency list
and another using an adjacency matrix.
"""

# TODO: Add unit tests


class UndirectedGraph:
    """Representation of an undirected graph using an adjacency matrix.

    Attributes:
        vertices: A list of all the vertices in the graph.
        matrix: Adjacency matrix containing info about vertex connections.
    """

    def __init__(self):
        """Inits UndirectedGraph with empty matrix."""
        self.vertices = []
        self.matrix = []

    def __str__(self):
        """Prints the adjacency matrix of the graph.

        Returns:
            The string representation of the adjacency matrix.
        """
        output = ""
        for row in self.matrix:
            for column in row:
                output += str(column) + ' '
            output += '\n'

        return output

    def adjacent(self, x, y):
        """Tests whether there is an edge from vertex x to vertex y.

        Returns:
            True if there is an edge between x and y, False otherwise.
        """
        if not all(value in self.vertices for value in [x, y]):
            return False

        idx_x = self.vertices.index(x)
        idx_y = self.vertices.index(y)

        # We can check the indices in either order, since both cases
        # should have the same value in an undirected graph.
        return self.matrix[idx_x][idx_y] >= 1

    def neighbors(self, x):
        pass

    def add_vertex(self, value):
        """Adds a vertex to the graph.

        Adds a new vertex with the given value to the graph.
        Does nothing if the value already exists.
        """
        if value in self.vertices:
            return

        self.vertices.append(value)
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * len(self.vertices))

    def remove_vertex(self, x):
        pass

    def add_edge(self, x, y):
        """Adds an edge from vertex x to vertex y.

        Creates an edge between the vertices x and y. Does nothing if
        one or more of the vertices does not exist.
        """
        if not all(value in self.vertices for value in [x, y]):
            return

        idx_x = self.vertices.index(x)
        idx_y = self.vertices.index(y)

        # Here we set the value in both directions because
        # the graph is undirected.
        self.matrix[idx_x][idx_y] = 1
        self.matrix[idx_y][idx_x] = 1

    def remove_edge(self, x, y):
        pass

    def get_vertex_value(self, x):
        pass

    def set_vertex_value(self, x, v):
        pass

    def get_edge_value(self, x, y):
        pass

    def set_edge_value(self, x, y, v):
        pass


def main():
    graph = UndirectedGraph()
    for i in range(6):
        graph.add_vertex(i+1)

    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 3)
    graph.add_edge(4, 3)
    graph.add_edge(3, 6)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    print(graph)

    print(graph.adjacent(1, 2))
    print(graph.adjacent(1, 3))
    print(graph.adjacent(5, 8))


if __name__ == "__main__":
    main()
