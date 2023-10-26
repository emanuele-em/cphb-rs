# Shortest paths

Finding a shortest path between two nodes
of a graph
is an important problem that has many
practical applications.
For example, a natural problem related to a road network
is to calculate the shortest possible length of a route
between two cities, given the lengths of the roads.

In an unweighted graph, the length of a path equals
the number of its edges, and we can
simply use breadth-first search to find
a shortest path.
However, in this chapter we focus on
weighted graphs
where more sophisticated algorithms
are needed
for finding shortest paths.
