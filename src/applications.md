#  Applications

Using the graph traversal algorithms,
we can check many properties of graphs.
Usually, both depth-first search and
breadth-first search may be used,
but in practice, depth-first search
is a better choice, because it is
easier to implement.
In the following applications we will
assume that the graph is undirected.

## Connectivity check

A graph is connected if there is a path
between any two nodes of the graph.
Thus, we can check if a graph is connected
by starting at an arbitrary node and
finding out if we can reach all other nodes.

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (2) at (7,5) {2};
\node[draw, circle] (1) at (3,5) {1};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (5) at (7,3) {5};
\node[draw, circle] (4) at (3,3) {4};

\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (5);
\end{tikzpicture}
</script>

a depth-first search from node $1$ visits
the following nodes:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (2) at (7,5) {2};
\node[draw, circle,fill=lightgray] (1) at (3,5) {1};
\node[draw, circle,fill=lightgray] (3) at (5,4) {3};
\node[draw, circle] (5) at (7,3) {5};
\node[draw, circle,fill=lightgray] (4) at (3,3) {4};

\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (5);

\path[draw=red,thick,->,line width=2pt] (1) -- (3);
\path[draw=red,thick,->,line width=2pt] (3) -- (4);

\end{tikzpicture}
</script>

Since the search did not visit all the nodes,
we can conclude that the graph is not connected.
In a similar way, we can also find all connected components
of a graph by iterating through the nodes and always
starting a new depth-first search if the current node
does not belong to any component yet.

## Finding cycles

A graph contains a cycle if during a graph traversal,
we find a node whose neighbor (other than the
previous node in the current path) has already been
visited.
For example, the graph

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (2) at (7,5) {2};
\node[draw, circle] (1) at (3,5) {1};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (5) at (7,3) {5};
\node[draw, circle] (4) at (3,3) {4};

\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (3) -- (5);
\end{tikzpicture}
</script>

contains two cycles and we can find one
of them as follows:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle,fill=lightgray] (2) at (7,5) {2};
\node[draw, circle,fill=lightgray] (1) at (3,5) {1};
\node[draw, circle,fill=lightgray] (3) at (5,4) {3};
\node[draw, circle,fill=lightgray] (5) at (7,3) {5};
\node[draw, circle] (4) at (3,3) {4};

\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (3) -- (5);

\path[draw=red,thick,->,line width=2pt] (1) -- (3);
\path[draw=red,thick,->,line width=2pt] (3) -- (2);
\path[draw=red,thick,->,line width=2pt] (2) -- (5);

\end{tikzpicture}
</script>

After moving from node 2 to node 5 we notice that
the neighbor 3 of node 5 has already been visited.
Thus, the graph contains a cycle that goes through node 3,
for example, $3 \rightarrow 2 \rightarrow 5 \rightarrow 3$.

Another way to find out whether a graph contains a cycle
is to simply calculate the number of nodes and edges
in every component.
If a component contains $c$ nodes and no cycle,
it must contain exactly $c-1$ edges
(so it has to be a tree).
If there are $c$ or more edges, the component
surely contains a cycle.

## Bipartiteness check

A graph is bipartite if its nodes can be colored
using two colors so that there are no adjacent
nodes with the same color.
It is surprisingly easy to check if a graph
is bipartite using graph traversal algorithms.

The idea is to color the starting node blue,
all its neighbors red, all their neighbors blue, and so on.
If at some point of the search we notice that
two adjacent nodes have the same color,
this means that the graph is not bipartite.
Otherwise the graph is bipartite and one coloring
has been found.

For example, the graph

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (2) at (5,5) {2};
\node[draw, circle] (1) at (3,5) {1};
\node[draw, circle] (3) at (7,4) {3};
\node[draw, circle] (5) at (5,3) {5};
\node[draw, circle] (4) at (3,3) {4};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (5) -- (4);
\path[draw,thick,-] (4) -- (1);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (5) -- (3);
\end{tikzpicture}
</script>

is not bipartite, because a search from node 1
proceeds as follows:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle,fill=red!40] (2) at (5,5) {2};
\node[draw, circle,fill=blue!40] (1) at (3,5) {1};
\node[draw, circle,fill=blue!40] (3) at (7,4) {3};
\node[draw, circle,fill=red!40] (5) at (5,3) {5};
\node[draw, circle] (4) at (3,3) {4};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (5) -- (4);
\path[draw,thick,-] (4) -- (1);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (5) -- (3);

\path[draw=red,thick,->,line width=2pt] (1) -- (2);
\path[draw=red,thick,->,line width=2pt] (2) -- (3);
\path[draw=red,thick,->,line width=2pt] (3) -- (5);
\path[draw=red,thick,->,line width=2pt] (5) -- (2);
\end{tikzpicture}
</script>

We notice that the color of both nodes 2 and 5
is red, while they are adjacent nodes in the graph.
Thus, the graph is not bipartite.

This algorithm always works, because when there
are only two colors available,
the color of the starting node in a component
determines the colors of all other nodes in the component.
It does not make any difference whether the
starting node is red or blue.

Note that in the general case,
it is difficult to find out if the nodes
in a graph can be colored using $k$ colors
so that no adjacent nodes have the same color.
Even when $k=3$, no efficient algorithm is known
but the problem is NP-hard.
