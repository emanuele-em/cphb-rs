#  Breadth-first search

**Breadth-first search** (BFS) visits the nodes
in increasing order of their distance
from the starting node.
Thus, we can calculate the distance
from the starting node to all other
nodes using breadth-first search.
However, breadth-first search is more difficult
to implement than depth-first search.

Breadth-first search goes through the nodes
one level after another.
First the search explores the nodes whose
distance from the starting node is 1,
then the nodes whose distance is 2, and so on.
This process continues until all nodes
have been visited.

## Example

Let us consider how breadth-first search processes
the following graph:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,5) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};
\node[draw, circle] (6) at (5,3) {6};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (5) -- (6);
\end{tikzpicture}
</script>

Suppose that the search begins at node 1.
First, we process all nodes that can be reached
from node 1 using a single edge:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle,fill=lightgray] (1) at (1,5) {1};
\node[draw, circle,fill=lightgray] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,5) {3};
\node[draw, circle,fill=lightgray] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};
\node[draw, circle] (6) at (5,3) {6};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (5) -- (6);

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);

\path[draw=red,thick,->,line width=2pt] (1) -- (2);
\path[draw=red,thick,->,line width=2pt] (1) -- (4);
\end{tikzpicture}
</script>

After this, we proceed to nodes 3 and 5:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle,fill=lightgray] (1) at (1,5) {1};
\node[draw, circle,fill=lightgray] (2) at (3,5) {2};
\node[draw, circle,fill=lightgray] (3) at (5,5) {3};
\node[draw, circle,fill=lightgray] (4) at (1,3) {4};
\node[draw, circle,fill=lightgray] (5) at (3,3) {5};
\node[draw, circle] (6) at (5,3) {6};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (5) -- (6);

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);

\path[draw=red,thick,->,line width=2pt] (2) -- (3);
\path[draw=red,thick,->,line width=2pt] (2) -- (5);
\end{tikzpicture}
</script>

Finally, we visit node 6:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle,fill=lightgray] (1) at (1,5) {1};
\node[draw, circle,fill=lightgray] (2) at (3,5) {2};
\node[draw, circle,fill=lightgray] (3) at (5,5) {3};
\node[draw, circle,fill=lightgray] (4) at (1,3) {4};
\node[draw, circle,fill=lightgray] (5) at (3,3) {5};
\node[draw, circle,fill=lightgray] (6) at (5,3) {6};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (5) -- (6);

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);

\path[draw=red,thick,->,line width=2pt] (3) -- (6);
\path[draw=red,thick,->,line width=2pt] (5) -- (6);
\end{tikzpicture}
</script>

Now we have calculated the distances
from the starting node to all nodes of the graph.
The distances are as follows:

| node | distance |
| --- | --- |
| 1 | 0 |
| 2 | 1 |
| 3 | 2 |
| 4 | 1 |
| 5 | 2 |
| 6 | 3 |

Like in depth-first search,
the time complexity of breadth-first search
is $O(n+m)$, where $n$ is the number of nodes
and $m$ is the number of edges.
