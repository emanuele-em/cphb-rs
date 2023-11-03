# Dynamic programming

If a directed graph is acyclic,
dynamic programming can be applied to it.
For example, we can efficiently solve the following
problems concerning paths from a starting node
to an ending node:

- how many different paths are there?
- what is the shortest/longest path?
- what is the minimum/maximum number of edges in a path?
- which nodes certainly appear in any path?

## Counting the number of paths

As an example, let us calculate the number of paths
from node 1 to node 6 in the following graph:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,5) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};
\node[draw, circle] (6) at (5,3) {6};

\path[draw,thick,->,>=latex] (1) -- (2);
\path[draw,thick,->,>=latex] (2) -- (3);
\path[draw,thick,->,>=latex] (1) -- (4);
\path[draw,thick,->,>=latex] (4) -- (5);
\path[draw,thick,->,>=latex] (5) -- (2);
\path[draw,thick,->,>=latex] (5) -- (3);
\path[draw,thick,->,>=latex] (3) -- (6);
\end{tikzpicture}
</script>

There are a total of three such paths:

- $1 \rightarrow 2 \rightarrow 3 \rightarrow 6$
- $1 \rightarrow 4 \rightarrow 5 \rightarrow 2 \rightarrow 3 \rightarrow 6$
- $1 \rightarrow 4 \rightarrow 5 \rightarrow 3 \rightarrow 6$

Let `paths(x)` denote the number of paths from
node 1 to node $x$.
As a base case, `paths(1)=1`.
Then, to calculate other values of `paths(x)`,
we may use the recursion

\\[
\\texttt{paths}(x) = \\texttt{paths}(a_1)+\\texttt{paths}(a_2)+\\cdots+\\texttt{paths}(a_k)
\\]

where $a_1,a_2,\ldots,a_k$ are the nodes from which there
is an edge to $x$.
Since the graph is acyclic, the values of $\texttt{paths}(x)$
can be calculated in the order of a topological sort.
A topological sort for the above graph is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,0) {1};
\node[draw, circle] (2) at (4.5,0) {2};
\node[draw, circle] (3) at (6,0) {3};
\node[draw, circle] (4) at (1.5,0) {4};
\node[draw, circle] (5) at (3,0) {5};
\node[draw, circle] (6) at (7.5,0) {6};

\path[draw,thick,->,>=latex] (1) edge [bend left=30] (2);
\path[draw,thick,->,>=latex] (2) -- (3);
\path[draw,thick,->,>=latex] (1) -- (4);
\path[draw,thick,->,>=latex] (4) -- (5);
\path[draw,thick,->,>=latex] (5) -- (2);
\path[draw,thick,->,>=latex] (5) edge [bend right=30] (3);
\path[draw,thick,->,>=latex] (3) -- (6);
\end{tikzpicture}
</script>

Hence, the numbers of paths are as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,5) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};
\node[draw, circle] (6) at (5,3) {6};

\path[draw,thick,->,>=latex] (1) -- (2);
\path[draw,thick,->,>=latex] (2) -- (3);
\path[draw,thick,->,>=latex] (1) -- (4);
\path[draw,thick,->,>=latex] (4) -- (5);
\path[draw,thick,->,>=latex] (5) -- (2);
\path[draw,thick,->,>=latex] (5) -- (3);
\path[draw,thick,->,>=latex] (3) -- (6);

\node[color=red] at (1,2.3) {1};
\node[color=red] at (3,2.3) {1};
\node[color=red] at (5,2.3) {3};
\node[color=red] at (1,5.7) {1};
\node[color=red] at (3,5.7) {2};
\node[color=red] at (5,5.7) {3};
\end{tikzpicture}
</script>

For example, to calculate the value of `paths(3)`,
we can use the formula `paths(2)+paths(5)`,
because there are edges from nodes 2 and 5
to node 3.
Since `paths}(2)=2` and `paths}(5)=1`, we conclude that `paths}(3)=3`.

## Extending Dijkstra's algorithm

A by-product of Dijkstra's algorithm is a directed, acyclic
graph that indicates for each node of the original graph
the possible ways to reach the node using a shortest path
from the starting node.
Dynamic programming can be applied to that graph.
For example, in the graph

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (0,0) {1};
\node[draw, circle] (2) at (2,0) {2};
\node[draw, circle] (3) at (0,-2) {3};
\node[draw, circle] (4) at (2,-2) {4};
\node[draw, circle] (5) at (4,-1) {5};

\path[draw,thick,-] (1) -- node[font=\small,label=above:3] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:5] {} (3);
\path[draw,thick,-] (2) -- node[font=\small,label=right:4] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:8] {} (5);
\path[draw,thick,-] (3) -- node[font=\small,label=below:2] {} (4);
\path[draw,thick,-] (4) -- node[font=\small,label=below:1] {} (5);
\path[draw,thick,-] (2) -- node[font=\small,label=above:2] {} (3);
\end{tikzpicture}
</script>

the shortest paths from node 1 may use the following edges:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (0,0) {1};
\node[draw, circle] (2) at (2,0) {2};
\node[draw, circle] (3) at (0,-2) {3};
\node[draw, circle] (4) at (2,-2) {4};
\node[draw, circle] (5) at (4,-1) {5};

\path[draw,thick,->] (1) -- node[font=\small,label=above:3] {} (2);
\path[draw,thick,->] (1) -- node[font=\small,label=left:5] {} (3);
\path[draw,thick,->] (2) -- node[font=\small,label=right:4] {} (4);
\path[draw,thick,->] (3) -- node[font=\small,label=below:2] {} (4);
\path[draw,thick,->] (4) -- node[font=\small,label=below:1] {} (5);
\path[draw,thick,->] (2) -- node[font=\small,label=above:2] {} (3);
\end{tikzpicture}
</script>

Now we can, for example, calculate the number of
shortest paths from node 1 to node 5
using dynamic programming:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (0,0) {1};
\node[draw, circle] (2) at (2,0) {2};
\node[draw, circle] (3) at (0,-2) {3};
\node[draw, circle] (4) at (2,-2) {4};
\node[draw, circle] (5) at (4,-1) {5};

\path[draw,thick,->] (1) -- node[font=\small,label=above:3] {} (2);
\path[draw,thick,->] (1) -- node[font=\small,label=left:5] {} (3);
\path[draw,thick,->] (2) -- node[font=\small,label=right:4] {} (4);
\path[draw,thick,->] (3) -- node[font=\small,label=below:2] {} (4);
\path[draw,thick,->] (4) -- node[font=\small,label=below:1] {} (5);
\path[draw,thick,->] (2) -- node[font=\small,label=above:2] {} (3);

\node[color=red] at (0,0.7) {1};
\node[color=red] at (2,0.7) {1};
\node[color=red] at (0,-2.7) {2};
\node[color=red] at (2,-2.7) {3};
\node[color=red] at (4,-1.7) {3};
\end{tikzpicture}
</script>

## Representing problems as a graphs

Actually, any dynamic programming problem
can be represented as a directed, acyclic graph.
In such a graph, each node corresponds to a dynamic programming state
and the edges indicate how the states depend on each other.

As an example, consider the problem
of forming a sum of money $n$
using coins
\\(
\\{c_1,c_2,\\ldots,c_k\\}
\\).
In this problem, we can construct a graph where
each node corresponds to a sum of money,
and the edges show how the coins can be chosen.
For example, for coins \\(\\{1,3,4\\}\\) and $n=6$,
the graph is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (0) at (0,0) {0};
\node[draw, circle] (1) at (2,0) {1};
\node[draw, circle] (2) at (4,0) {2};
\node[draw, circle] (3) at (6,0) {3};
\node[draw, circle] (4) at (8,0) {4};
\node[draw, circle] (5) at (10,0) {5};
\node[draw, circle] (6) at (12,0) {6};

\path[draw,thick,->] (0) -- (1);
\path[draw,thick,->] (1) -- (2);
\path[draw,thick,->] (2) -- (3);
\path[draw,thick,->] (3) -- (4);
\path[draw,thick,->] (4) -- (5);
\path[draw,thick,->] (5) -- (6);

\path[draw,thick,->] (0) edge [bend right=30] (3);
\path[draw,thick,->] (1) edge [bend right=30] (4);
\path[draw,thick,->] (2) edge [bend right=30] (5);
\path[draw,thick,->] (3) edge [bend right=30] (6);

\path[draw,thick,->] (0) edge [bend left=30] (4);
\path[draw,thick,->] (1) edge [bend left=30] (5);
\path[draw,thick,->] (2) edge [bend left=30] (6);
\end{tikzpicture}
</script>

Using this representation,
the shortest path from node 0 to node $n$
corresponds to a solution with the minimum number of coins,
and the total number of paths from node 0 to node $n$
equals the total number of solutions.
