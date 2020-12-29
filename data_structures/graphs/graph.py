"""
Basic undirected graph implementations, one using an adjacency list
and another using an adjacency matrix.
"""


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

    def __len__(self):
        return len(self.vertices)

    def adjacent(self, x, y):
        """Tests whether there is an edge from vertex x to vertex y.

        Returns:
            True if there is an edge between x and y, False otherwise.
        """
        # Check if vertex exists.
        if not all(value in self.vertices for value in [x, y]):
            return False

        idx_x = self.vertices.index(x)
        idx_y = self.vertices.index(y)

        # We can check the indices in either order, since both cases
        # should have the same value in an undirected graph.
        return self.matrix[idx_x][idx_y] >= 1

    def neighbors(self, x):
        """Lists all vertices that are adjacent to x.

        Returns:
            A list of all vertices adjacent to x.
        """
        return [vertex for vertex in self.vertices if self.adjacent(x, vertex)]

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
        """Removes a vertex from the graph, if it exists."""
        if x not in self.vertices:
            return

        neighbors = self.neighbors(x)
        for neighbor in neighbors:
            self.remove_edge(x, neighbor)

        self.vertices.remove(x)

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
        """Removes the egde connecting x and y."""
        idx_x = self.vertices.index(x)
        idx_y = self.vertices.index(y)

        # We have to set the value in two places because the
        # matrix is symmetric.
        self.matrix[idx_x][idx_y] = 0
        self.matrix[idx_y][idx_x] = 0
