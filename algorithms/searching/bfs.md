# Breadth-First Search

**Breadth-First Search** is a search/traversal algorithm used on graphs.
Its most common application is finding the shortest path between two vertices.

The general idea is that you start by checking a vertex's neighbors, then check
those neighbors' neighbors, and so on.

## Implementation

One way to implement BFS:

1. Create a queue to keep track of which vertices to check.
2. Pop a vertex from the queue.
3. Check if the popped vertex is what's being searched for.
4. If the vertex is what you're looking for, you're done. Otherwise go to the next step.
5. Add all of the vertex's neighbors to the queue.
6. Go back to step 2.
7. If the queue is empty, then there is no path from the root to the target.

## References

- [Aditya Y. Bhargava - Grokking Algorithms](https://www.manning.com/books/grokking-algorithms)
