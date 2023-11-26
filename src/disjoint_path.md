# Disjoint paths

Many graph problems can be solved by reducing
them to the maximum flow problem.
Our first example of such a problem is
as follows: we are given a directed graph
with a source and a sink,
and our task is to find the maximum number
of disjoint paths from the source to the sink.

## Edge-disjoint paths

We will first focus on the problem of
finding the maximum number of
**edge-disjoint paths** from the source to the sink.
This means that we should construct a set of paths
such that each edge appears in at most one path.

For example, consider the following graph:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,2) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (3,1) {4};
\node[draw, circle] (5) at (5,1) {5};
\node[draw, circle] (6) at (7,2) {6};
\path[draw,thick,->] (1) -- (2);
\path[draw,thick,->] (1) -- (4);
\path[draw,thick,->] (2) -- (4);
\path[draw,thick,->] (3) -- (2);
\path[draw,thick,->] (3) -- (5);
\path[draw,thick,->] (3) -- (6);
\path[draw,thick,->] (4) -- (3);
\path[draw,thick,->] (4) -- (5);
\path[draw,thick,->] (5) -- (6);
\end{tikzpicture}
</script>

In this graph, the maximum number of edge-disjoint
paths is 2.
We can choose the paths
$1 \rightarrow 2 \rightarrow 4 \rightarrow 3 \rightarrow 6$
and $1 \rightarrow 4 \rightarrow 5 \rightarrow 6$ as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,2) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (3,1) {4};
\node[draw, circle] (5) at (5,1) {5};
\node[draw, circle] (6) at (7,2) {6};
\path[draw,thick,->] (1) -- (2);
\path[draw,thick,->] (1) -- (4);
\path[draw,thick,->] (2) -- (4);
\path[draw,thick,->] (3) -- (2);
\path[draw,thick,->] (3) -- (5);
\path[draw,thick,->] (3) -- (6);
\path[draw,thick,->] (4) -- (3);
\path[draw,thick,->] (4) -- (5);
\path[draw,thick,->] (5) -- (6);

\path[draw=green,thick,->,line width=2pt] (1) -- (2);
\path[draw=green,thick,->,line width=2pt] (2) -- (4);
\path[draw=green,thick,->,line width=2pt] (4) -- (3);
\path[draw=green,thick,->,line width=2pt] (3) -- (6);

\path[draw=blue,thick,->,line width=2pt] (1) -- (4);
\path[draw=blue,thick,->,line width=2pt] (4) -- (5);
\path[draw=blue,thick,->,line width=2pt] (5) -- (6);
\end{tikzpicture}
</script>

It turns out that the maximum number of
edge-disjoint paths
equals the maximum flow of the graph,
assuming that the capacity of each edge is one.
After the maximum flow has been constructed,
the edge-disjoint paths can be found greedily
by following paths from the source to the sink.

## Node-disjoint paths

Let us now consider another problem:
finding the maximum number of
**node-disjoint paths** from the source
to the sink.
In this problem, every node,
except for the source and sink,
may appear in at most one path.
The number of node-disjoint paths
may be smaller than the number of
edge-disjoint paths.

For example, in the previous graph,
the maximum number of node-disjoint paths is 1:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (1,2) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (3,1) {4};
\node[draw, circle] (5) at (5,1) {5};
\node[draw, circle] (6) at (7,2) {6};
\path[draw,thick,->] (1) -- (2);
\path[draw,thick,->] (1) -- (4);
\path[draw,thick,->] (2) -- (4);
\path[draw,thick,->] (3) -- (2);
\path[draw,thick,->] (3) -- (5);
\path[draw,thick,->] (3) -- (6);
\path[draw,thick,->] (4) -- (3);
\path[draw,thick,->] (4) -- (5);
\path[draw,thick,->] (5) -- (6);

\path[draw=green,thick,->,line width=2pt] (1) -- (2);
\path[draw=green,thick,->,line width=2pt] (2) -- (4);
\path[draw=green,thick,->,line width=2pt] (4) -- (3);
\path[draw=green,thick,->,line width=2pt] (3) -- (6);
\end{tikzpicture}
</script>

We can reduce also this problem to the maximum flow problem.
Since each node can appear in at most one path,
we have to limit the flow that goes through the nodes.
A standard method for this is to divide each node into
two nodes such that the first node has the incoming edges
of the original node, the second node has the outgoing
edges of the original node, and
there is a new edge from the first node
to the second node.

In our example, the graph becomes as follows:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (1,2) {1};
\node[draw, circle] (2a) at (3,3) {2};
\node[draw, circle] (3a) at (6,3) {3};
\node[draw, circle] (4a) at (3,1) {4};
\node[draw, circle] (5a) at (6,1) {5};
\node[draw, circle] (2b) at (4,3) {2};
\node[draw, circle] (3b) at (7,3) {3};
\node[draw, circle] (4b) at (4,1) {4};
\node[draw, circle] (5b) at (7,1) {5};
\node[draw, circle] (6) at (9,2) {6};

\path[draw,thick,->] (2a) -- (2b);
\path[draw,thick,->] (3a) -- (3b);
\path[draw,thick,->] (4a) -- (4b);
\path[draw,thick,->] (5a) -- (5b);

\path[draw,thick,->] (1) -- (2a);
\path[draw,thick,->] (1) -- (4a);
\path[draw,thick,->] (2b) -- (4a);
\path[draw,thick,->] (3b) edge [bend right=30] (2a);
\path[draw,thick,->] (3b) -- (5a);
\path[draw,thick,->] (3b) -- (6);
\path[draw,thick,->] (4b) -- (3a);
\path[draw,thick,->] (4b) -- (5a);
\path[draw,thick,->] (5b) -- (6);
\end{tikzpicture}
</script>

The maximum flow for the graph is as follows:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (1,2) {1};

\node[draw, circle] (2a) at (3,3) {2};
\node[draw, circle] (3a) at (6,3) {3};
\node[draw, circle] (4a) at (3,1) {4};
\node[draw, circle] (5a) at (6,1) {5};

\node[draw, circle] (2b) at (4,3) {2};
\node[draw, circle] (3b) at (7,3) {3};
\node[draw, circle] (4b) at (4,1) {4};
\node[draw, circle] (5b) at (7,1) {5};

\node[draw, circle] (6) at (9,2) {6};

\path[draw,thick,->] (2a) -- (2b);
\path[draw,thick,->] (3a) -- (3b);
\path[draw,thick,->] (4a) -- (4b);
\path[draw,thick,->] (5a) -- (5b);

\path[draw,thick,->] (1) -- (2a);
\path[draw,thick,->] (1) -- (4a);
\path[draw,thick,->] (2b) -- (4a);
\path[draw,thick,->] (3b) edge [bend right=30] (2a);
\path[draw,thick,->] (3b) -- (5a);
\path[draw,thick,->] (3b) -- (6);
\path[draw,thick,->] (4b) -- (3a);
\path[draw,thick,->] (4b) -- (5a);
\path[draw,thick,->] (5b) -- (6);

\path[draw=red,thick,->,line width=2pt] (1) -- (2a);
\path[draw=red,thick,->,line width=2pt] (2a) -- (2b);
\path[draw=red,thick,->,line width=2pt] (2b) -- (4a);
\path[draw=red,thick,->,line width=2pt] (4a) -- (4b);
\path[draw=red,thick,->,line width=2pt] (4b) -- (3a);
\path[draw=red,thick,->,line width=2pt] (3a) -- (3b);
\path[draw=red,thick,->,line width=2pt] (3b) -- (6);
\end{tikzpicture}
</script>

Thus, the maximum number of node-disjoint paths
from the source to the sink is 1.
