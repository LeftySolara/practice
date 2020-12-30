# Dijkstra's Algorithm

- used to find the fastest path (i.e., used on weighted graphs)
- basic procedure
  1. Find the cheapest node.
  2. Check if there's a cheaper path to the neighbors. If yes, update their costs.
  3. Repeat until this is done for every node in the graph.
  4. Calculate the final path.
- Does not work on graphs with cycles, which means it also doesn't work on undirected graphs
- Does not work on graphs with negative-weight edges.

## References

- [Aditya Y. Bhargava - Grokking Algorithms](https://www.manning.com/books/grokking-algorithms)
- [Computerphile - Dijkstra's Algorithm](https://www.youtube.com/watch?v=GazC3A4OQTE)
