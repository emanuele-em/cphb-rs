# Hamiltonian paths

A **Hamiltonian path**
is a path
that visits each node of the graph exactly once.
For example, the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (5);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);
\end{tikzpicture}
</script>

contains a Hamiltonian path from node 1 to node 3:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (5);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);

\path[draw=red,thick,->,line width=2pt] (1) -- node[font=\small,label={[red]left:1.}] {} (4);
\path[draw=red,thick,->,line width=2pt] (4) -- node[font=\small,label={[red]south:2.}] {} (5);
\path[draw=red,thick,->,line width=2pt] (5) -- node[font=\small,label={[red]left:3.}] {} (2);
\path[draw=red,thick,->,line width=2pt] (2) -- node[font=\small,label={[red]north:4.}] {} (3);
\end{tikzpicture}
</script>

If a Hamiltonian path begins and ends at the same node,
it is called a **Hamiltonian circuit**.
The graph above also has an Hamiltonian circuit
that begins and ends at node 1:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (5);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);

\path[draw=red,thick,->,line width=2pt] (1) -- node[font=\small,label={[red]north:1.}] {} (2);
\path[draw=red,thick,->,line width=2pt] (2) -- node[font=\small,label={[red]north:2.}] {} (3);
\path[draw=red,thick,->,line width=2pt] (3) -- node[font=\small,label={[red]south:3.}] {} (5);
\path[draw=red,thick,->,line width=2pt] (5) -- node[font=\small,label={[red]south:4.}] {} (4);
\path[draw=red,thick,->,line width=2pt] (4) -- node[font=\small,label={[red]left:5.}] {} (1);
\end{tikzpicture}
</script>

## Existence

No efficient method is known for testing if a graph
contains a Hamiltonian path, and the problem is NP-hard.
Still, in some special cases, we can be certain
that a graph contains a Hamiltonian path.

A simple observation is that if the graph is complete,
i.e., there is an edge between all pairs of nodes,
it also contains a Hamiltonian path.
Also stronger results have been achieved:

- **Dirac's theorem**: 
If the degree of each node is at least $n/2$,
the graph contains a Hamiltonian path.
- **Ore's theorem**:
If the sum of degrees of each non-adjacent pair of nodes
is at least $n$,
the graph contains a Hamiltonian path.

A common property in these theorems and other results is
that they guarantee the existence of a Hamiltonian path
if the graph has _a large number_ of edges.
This makes sense, because the more edges the graph contains,
the more possibilities there is to construct a Hamiltonian path.

## Construction

Since there is no efficient way to check if a Hamiltonian
path exists, it is clear that there is also no method
to efficiently construct the path, because otherwise
we could just try to construct the path and see
whether it exists.

A simple way to search for a Hamiltonian path is
to use a backtracking algorithm that goes through all
possible ways to construct the path.
The time complexity of such an algorithm is at least $O(n!)$,
because there are $n!$ different ways to choose the order of $n$ nodes.

A more efficient solution is based on dynamic programming
(see Chapter 10.5).
The idea is to calculate values
of a function `possible(S,x)`,
where $S$ is a subset of nodes and $x$
is one of the nodes.
The function indicates whether there is a Hamiltonian path
that visits the nodes of $S$ and ends at node $x$.
It is possible to implement this solution in $O(2^n n^2)$ time.
