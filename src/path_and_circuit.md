# Paths and circuits

This chapter focuses on two types of paths in graphs:

- An **Eulerian path** is a path that
goes through each edge exactly once.
- A **Hamiltonian path** is a path
that visits each node exactly once.

While Eulerian and Hamiltonian paths look like
similar concepts at first glance,
the computational problems related to them
are very different.
It turns out that there is a simple rule that
determines whether a graph contains an Eulerian path,
and there is also an efficient algorithm to
find such a path if it exists.
On the contrary, checking the existence of a Hamiltonian path is a NP-hard
problem, and no efficient algorithm is known for solving the problem.
