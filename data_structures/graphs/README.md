# Graphs

A **graph** is an abstract data structure that models the relationships in a set
of objects.

## Basics

Graphs are made up of vertices and edges. **Vertices** contain data, and edges represent
a connection between vertices. Vertices that have an edge connecting them are called **adjacent**.

A **directed graph** has edges with one-way relationships, while an **undirected graph** has relationships that are bidirectional.

Some quick vocabulary:

- Loop: An edge that connects to the same vertex on both ends.
- Cycle: Path in which the only repeated vertices are the first and last ones.
- Edge Weight: Any value assigned to an edge.
- Vertex Degree: The number of edges connected to a vertex.

## Representing Graphs on Computers

### Adjacency Matrix

An **adjacency matrix** _A_ is a square _n x n_ matrix used to represent the connections
between graph vertices, where _n_ is the number of vertices in the graph.

Each element `a[i][j]` has the value `1` when there exists an edge from vertex `u[i]`
to vertex `u[j]`, and `0` when there is no edge. If the graph is undirected, then the
matrix is symmetric. In a directed graph, the rows represent source vertices and
the columns represent destination vertices.

When using an adjacency matrix, data on the edges and vertices must be stored externally.

### Adjacency List

### Common Functionality

## References

- [Aditya Y. Bhargava - Grokking Algorithms](https://www.manning.com/books/grokking-algorithms)
- [Jenny's lectures CS/IT NET&JRF - Graph representation in Data Structure(Graph Theory)|Adjacency Matrix and Adjacency List](https://www.youtube.com/watch?v=5hPfm_uqXmw)
- [Wikipedia - Degree (graph theory)](<https://en.wikipedia.org/wiki/Degree_(graph_theory)>)
- [Wikipedia - Graph (abstract data type)](<https://en.wikipedia.org/wiki/Graph_(abstract_data_type)>)
