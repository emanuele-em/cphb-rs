# Kruskal’s algorithm

In **Kruskal's algorithm**, the initial spanning tree
only contains the nodes of the graph
and does not contain any edges.
Then the algorithm goes through the edges
ordered by their weights, and always adds an edge
to the tree if it does not create a cycle.

The algorithm maintains the components
of the tree.
Initially, each node of the graph
belongs to a separate component.
Always when an edge is added to the tree,
two components are joined.
Finally, all nodes belong to the same component,
and a minimum spanning tree has been found.

## Example

Let us consider how Kruskal's algorithm processes the
following graph:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1.5,2) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (6.5,2) {4};
\node[draw, circle] (5) at (3,1) {5};
\node[draw, circle] (6) at (5,1) {6};
\path[draw,thick,-] (1) -- node[font=\small,label=above:3] {} (2);
\path[draw,thick,-] (2) -- node[font=\small,label=above:5] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=above:9] {} (4);
\path[draw,thick,-] (1) -- node[font=\small,label=below:5] {} (5);
\path[draw,thick,-] (5) -- node[font=\small,label=below:2] {} (6);
\path[draw,thick,-] (6) -- node[font=\small,label=below:7] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:6] {} (5);
\path[draw,thick,-] (3) -- node[font=\small,label=left:3] {} (6);
\end{tikzpicture}
</script>

The first step of the algorithm is to sort the
edges in increasing order of their weights.
The result is the following list:

| edge | weight |
| --- | --- |
| 5--6 | 2 |
| 1--2 | 3 |
| 3--6 | 3 |
| 1--5 | 5 |
| 2--3 | 5 |
| 2--5 | 6 |
| 4--6 | 7 |
| 3--4 | 9 |

After this, the algorithm goes through the list
and adds each edge to the tree if it joins
two separate components.

Initially, each node is in its own component:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1.5,2) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (6.5,2) {4};
\node[draw, circle] (5) at (3,1) {5};
\node[draw, circle] (6) at (5,1) {6};
\end{tikzpicture}
</script>

The first edge to be added to the tree is
the edge 5--6 that creates a component {5,6}
by joining the components {5} and {6}:


<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (1.5,2) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (6.5,2) {4};
\node[draw, circle] (5) at (3,1) {5};
\node[draw, circle] (6) at (5,1) {6};

%\path[draw,thick,-] (1) -- node[font=\small,label=above:3] {} (2);
%\path[draw,thick,-] (2) -- node[font=\small,label=above:5] {} (3);
%\path[draw,thick,-] (3) -- node[font=\small,label=above:9] {} (4);
%\path[draw,thick,-] (1) -- node[font=\small,label=below:5] {} (5);
\path[draw,thick,-] (5) -- node[font=\small,label=below:2] {} (6);
%\path[draw,thick,-] (6) -- node[font=\small,label=below:7] {} (4);
%\path[draw,thick,-] (2) -- node[font=\small,label=left:6] {} (5);
%\path[draw,thick,-] (3) -- node[font=\small,label=left:3] {} (6);
\end{tikzpicture}
</script>

After this, the edges 1--2, 3--6 and 1--5 are added in a similar way:

<script type="text/tikz">

\begin{tikzpicture}
\node[draw, circle] (1) at (1.5,2) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (6.5,2) {4};
\node[draw, circle] (5) at (3,1) {5};
\node[draw, circle] (6) at (5,1) {6};

\path[draw,thick,-] (1) -- node[font=\small,label=above:3] {} (2);
%\path[draw,thick,-] (2) -- node[font=\small,label=above:5] {} (3);
%\path[draw,thick,-] (3) -- node[font=\small,label=above:9] {} (4);
%\path[draw,thick,-] (1) -- node[font=\small,label=below:5] {} (5);
\path[draw,thick,-] (5) -- node[font=\small,label=below:2] {} (6);
%\path[draw,thick,-] (6) -- node[font=\small,label=below:7] {} (4);
%\path[draw,thick,-] (2) -- node[font=\small,label=left:6] {} (5);
%\path[draw,thick,-] (3) -- node[font=\small,label=left:3] {} (6);
\end{tikzpicture}
</script>

After those steps, most components have been joined
and there are two components in the tree:
{1,2,3,5,6} and {4}.

<script type="text/tikz">

\begin{tikzpicture}
\node[draw, circle] (1) at (1.5,2) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (6.5,2) {4};
\node[draw, circle] (5) at (3,1) {5};
\node[draw, circle] (6) at (5,1) {6};

\path[draw,thick,-] (1) -- node[font=\small,label=above:3] {} (2);
%\path[draw,thick,-] (2) -- node[font=\small,label=above:5] {} (3);
%\path[draw,thick,-] (3) -- node[font=\small,label=above:9] {} (4);
\path[draw,thick,-] (1) -- node[font=\small,label=below:5] {} (5);
\path[draw,thick,-] (5) -- node[font=\small,label=below:2] {} (6);
\path[draw,thick,-] (6) -- node[font=\small,label=below:7] {} (4);
%\path[draw,thick,-] (2) -- node[font=\small,label=left:6] {} (5);
\path[draw,thick,-] (3) -- node[font=\small,label=left:3] {} (6);
\end{tikzpicture}
</script>

After this, the algorithm will not add any
new edges, because the graph is connected
and there is a path between any two nodes.
The resulting graph is a minimum spanning tree
with weight $2+3+3+5+7=20$.

___

[^1] The algorithm was published in 1956 by J. B. Kruskal [48].
