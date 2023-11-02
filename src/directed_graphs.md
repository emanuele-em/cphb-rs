# Directed graphs

In this chapter, we focus on two classes of directed graphs:

- **Acyclic graphs**:
There are no cycles in the graph,
so there is no path from any node to itself[^1].

- **Successor graphs**:
The outdegree of each node is 1,
so each node has a unique successor.

It turns out that in both cases,
we can design efficient algorithms that are based
on the special properties of the graphs.

___

[^1] Directed acyclic graphs are sometimes called DAGs
