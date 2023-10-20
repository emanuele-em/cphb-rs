#  Graph terminology

A **graph** consists of **nodes**
and **edges**. In this book,
the variable $n$ denotes the number of nodes
in a graph, and the variable $m$ denotes
the number of edges.
The nodes are numbered
using integers $1,2,\ldots,n$.

For example, the following graph consists of 5 nodes and 7 edges:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\node[draw, circle] (5) at (6,2) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);
\end{tikzpicture}
</script>

A **path** leads from node $a$ to node $b$
through edges of the graph.
The **length** of a path is the number of
edges in it.
For example, the above graph contains
a path $1 \rightarrow 3 \rightarrow 4 \rightarrow 5$
of length 3
from node 1 to node 5:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\node[draw, circle] (5) at (6,2) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);

\path[draw=red,thick,->,line width=2pt] (1) -- (3);
\path[draw=red,thick,->,line width=2pt] (3) -- (4);
\path[draw=red,thick,->,line width=2pt] (4) -- (5);
\end{tikzpicture}
</script>

A path is a **cycle** if the first and last
node is the same.
For example, the above graph contains
a cycle $1 \rightarrow 3 \rightarrow 4 \rightarrow 1$.
A path is **simple** if each node appears
at most once in the path.

## Connectivity

A graph is **connected** if there is a path
between any two nodes.
For example, the following graph is connected:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\end{tikzpicture}
</script>

The following graph is not connected,
because it is not possible to get
from node 4 to any other node:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (2) -- (3);
\end{tikzpicture}
</script>

The connected parts of a graph are
called its **components**.
For example, the following graph
contains three components:
{$1,2,3$},
{$4,5,6,7$} and
{$8$}.


<script type="text/tikz">
\begin{tikzpicture}[scale=0.8]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};

\node[draw, circle] (6) at (6,1) {6};
\node[draw, circle] (7) at (9,1) {7};
\node[draw, circle] (4) at (6,3) {4};
\node[draw, circle] (5) at (9,3) {5};

\node[draw, circle] (8) at (11,2) {8};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (4) -- (5);
\path[draw,thick,-] (5) -- (7);
\path[draw,thick,-] (6) -- (7);
\path[draw,thick,-] (6) -- (4);
\end{tikzpicture}
</script>

A **tree** is a connected graph
that consists of $n$ nodes and $n-1$ edges.
There is a unique path
between any two nodes of a tree.
For example, the following graph is a tree:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\node[draw, circle] (5) at (6,2) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
%\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (2) -- (4);
%\path[draw,thick,-] (4) -- (5);
\end{tikzpicture}
</script>

## Edge directions

A graph is **directed**
if the edges can be traversed
in one direction only.
For example, the following graph is directed:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\node[draw, circle] (5) at (6,2) {5};
\path[draw,thick,->,>=latex] (1) -- (2);
\path[draw,thick,->,>=latex] (2) -- (4);
\path[draw,thick,->,>=latex] (2) -- (5);
\path[draw,thick,->,>=latex] (4) -- (5);
\path[draw,thick,->,>=latex] (4) -- (1);
\path[draw,thick,->,>=latex] (3) -- (1);
\end{tikzpicture}
</script>

The above graph contains
a path $3 \rightarrow 1 \rightarrow 2 \rightarrow 5$
from node $3$ to node $5$,
but there is no path from node $5$ to node $3$.

## Edge weights

In a **weighted** graph, each edge is assigned
a **weight**.
The weights are often interpreted as edge lengths.
For example, the following graph is weighted:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\node[draw, circle] (5) at (6,2) {5};
\path[draw,thick,-] (1) -- node[font=\small,label=above:5] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:1] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:7] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:6] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:7] {} (5);
\path[draw,thick,-] (4) -- node[font=\small,label=below:3] {} (5);
\end{tikzpicture}
</script>

The length of a path in a weighted graph
is the sum of the edge weights on the path.
For example, in the above graph,
the length of the path
$1 \rightarrow 2 \rightarrow 5$ is $12$,
and the length of the path
$1 \rightarrow 3 \rightarrow 4 \rightarrow 5$ is $11$.
The latter path is the \key{shortest} path from node $1$ to node $5$.

## Neighbors and degrees

Two nodes are **neighbors** or **adjacent**
if there is an edge between them.
The **degree** of a node
is the number of its neighbors.
For example, in the following graph,
the neighbors of node 2 are 1, 4 and 5,
so its degree is 3.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\node[draw, circle] (5) at (6,2) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (2) -- (5);
%\path[draw,thick,-] (4) -- (5);
\end{tikzpicture}
</script>

The sum of degrees in a graph is always $2m$,
where $m$ is the number of edges,
because each edge
increases the degree of exactly two nodes by one.
For this reason, the sum of degrees is always even.

A graph is **regular** if the
degree of every node is a constant $d$.
A graph is **complete** if the
degree of every node is $n-1$, i.e.,
the graph contains all possible edges
between the nodes.

In a directed graph, the **indegree**
of a node is the number of edges
that end at the node,
and the **outdegree** of a node
is the number of edges that start at the node.
For example, in the following graph,
the indegree of node 2 is 2,
and the outdegree of node 2 is 1.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\node[draw, circle] (5) at (6,2) {5};

\path[draw,thick,->,>=latex] (1) -- (2);
\path[draw,thick,->,>=latex] (1) -- (3);
\path[draw,thick,->,>=latex] (1) -- (4);
\path[draw,thick,->,>=latex] (3) -- (4);
\path[draw,thick,->,>=latex] (2) -- (4);
\path[draw,thick,<-,>=latex] (2) -- (5);
\end{tikzpicture}
</script>

## Colorings

In a **coloring** of a graph,
each node is assigned a color so that
no adjacent nodes have the same color.

A graph is **bipartite** if
it is possible to color it using two colors.
It turns out that a graph is bipartite
exactly when it does not contain a cycle
with an odd number of edges.
For example, the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {2};
\node[draw, circle] (2) at (4,3) {3};
\node[draw, circle] (3) at (1,1) {5};
\node[draw, circle] (4) at (4,1) {6};
\node[draw, circle] (5) at (-2,1) {4};
\node[draw, circle] (6) at (-2,3) {1};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (5) -- (6);
\end{tikzpicture}
</script>

is bipartite, because it can be colored as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle, fill=blue!40] (1) at (1,3) {2};
\node[draw, circle, fill=red!40] (2) at (4,3) {3};
\node[draw, circle, fill=red!40] (3) at (1,1) {5};
\node[draw, circle, fill=blue!40] (4) at (4,1) {6};
\node[draw, circle, fill=red!40] (5) at (-2,1) {4};
\node[draw, circle, fill=blue!40] (6) at (-2,3) {1};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (5) -- (6);
\end{tikzpicture}
</script>

However, the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {2};
\node[draw, circle] (2) at (4,3) {3};
\node[draw, circle] (3) at (1,1) {5};
\node[draw, circle] (4) at (4,1) {6};
\node[draw, circle] (5) at (-2,1) {4};
\node[draw, circle] (6) at (-2,3) {1};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (5) -- (6);
\path[draw,thick,-] (1) -- (6);
\end{tikzpicture}
</script>

is not bipartite, because it is not possible to color
the following cycle of three nodes using two colors:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {2};
\node[draw, circle] (2) at (4,3) {3};
\node[draw, circle] (3) at (1,1) {5};
\node[draw, circle] (4) at (4,1) {6};
\node[draw, circle] (5) at (-2,1) {4};
\node[draw, circle] (6) at (-2,3) {1};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (5) -- (6);
\path[draw,thick,-] (1) -- (6);

\path[draw=red,thick,-,line width=2pt] (1) -- (3);
\path[draw=red,thick,-,line width=2pt] (3) -- (6);
\path[draw=red,thick,-,line width=2pt] (6) -- (1);
\end{tikzpicture}
</script>

## Simplicity

A graph is **simple**
if no edge starts and ends at the same node,
and there are no multiple
edges between two nodes.
Often we assume that graphs are simple.
For example, the following graph is _not_ simple:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {2};
\node[draw, circle] (2) at (4,3) {3};
\node[draw, circle] (3) at (1,1) {5};
\node[draw, circle] (4) at (4,1) {6};
\node[draw, circle] (5) at (-2,1) {4};
\node[draw, circle] (6) at (-2,3) {1};

\path[draw,thick,-] (1) edge [bend right=20] (2);
\path[draw,thick,-] (2) edge [bend right=20] (1);
%\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (5) -- (6);

\tikzset{every loop/.style={in=135,out=190}}
\path[draw,thick,-] (5) edge [loop left] (5);
\end{tikzpicture}
</script>
