# Topological sorting

A topological sort is an ordering
of the nodes of a directed graph
such that if there is a path from node $a$ to node $b$,
then node $a$ appears before node $b$ in the ordering.
For example, for the graph

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
\path[draw,thick,->,>=latex] (4) -- (1);
\path[draw,thick,->,>=latex] (4) -- (5);
\path[draw,thick,->,>=latex] (5) -- (2);
\path[draw,thick,->,>=latex] (5) -- (3);
\path[draw,thick,->,>=latex] (3) -- (6);
\end{tikzpicture}
</script>

one topological sort is
`[4,1,5,2,3,6]`:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (-6,0) {1};
\node[draw, circle] (2) at (-3,0) {2};
\node[draw, circle] (3) at (-1.5,0) {3};
\node[draw, circle] (4) at (-7.5,0) {4};
\node[draw, circle] (5) at (-4.5,0) {5};
\node[draw, circle] (6) at (-0,0) {6};

\path[draw,thick,->,>=latex] (1) edge [bend right=30] (2);
\path[draw,thick,->,>=latex] (2) -- (3);
\path[draw,thick,->,>=latex] (4) -- (1);
\path[draw,thick,->,>=latex] (4) edge [bend left=30] (5);
\path[draw,thick,->,>=latex] (5) -- (2);
\path[draw,thick,->,>=latex] (5) edge [bend left=30]  (3);
\path[draw,thick,->,>=latex] (3) -- (6);
\end{tikzpicture}
</script>

An acyclic graph always has a topological sort.
However, if the graph contains a cycle,
it is not possible to form a topological sort,
because no node of the cycle can appear
before the other nodes of the cycle in the ordering.
It turns out that depth-first search can be used
to both check if a directed graph contains a cycle
and, if it does not contain a cycle, to construct a topological sort.

## Dynamic programming

The idea is to go through the nodes of the graph
and always begin a depth-first search at the current node
if it has not been processed yet.
During the searches, the nodes have three possible states:

- state 0: the node has not been processed (white)
- state 1: the node is under processing (light gray)
- state 2: the node has been processed (dark gray)

Initially, the state of each node is 0.
When a search reaches a node for the first time,
its state becomes 1.
Finally, after all successors of the node have
been processed, its state becomes 2.

If the graph contains a cycle, we will find this out
during the search, because sooner or later
we will arrive at a node whose state is 1.
In this case, it is not possible to construct a topological sort.

If the graph does not contain a cycle, we can construct
a topological sort by 
adding each node to a list when the state of the node becomes 2.
This list in reverse order is a topological sort.

## Example 1

In the example graph, the search first proceeds
from node 1 to node 6:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle,fill=gray!40] (1) at (1,5) {1};
\node[draw, circle,fill=gray!40] (2) at (3,5) {2};
\node[draw, circle,fill=gray!40] (3) at (5,5) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};
\node[draw, circle,fill=gray!80] (6) at (5,3) {6};

\path[draw,thick,->,>=latex] (4) -- (1);
\path[draw,thick,->,>=latex] (4) -- (5);
\path[draw,thick,->,>=latex] (5) -- (2);
\path[draw,thick,->,>=latex] (5) -- (3);
%\path[draw,thick,->,>=latex] (3) -- (6);

\path[draw=red,thick,->,line width=2pt] (1) -- (2);
\path[draw=red,thick,->,line width=2pt] (2) -- (3);
\path[draw=red,thick,->,line width=2pt] (3) -- (6);
\end{tikzpicture}
</script>

Now node 6 has been processed, so it is added to the list.
After this, also nodes 3, 2 and 1 are added to the list:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle,fill=gray!80] (1) at (1,5) {1};
\node[draw, circle,fill=gray!80] (2) at (3,5) {2};
\node[draw, circle,fill=gray!80] (3) at (5,5) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};
\node[draw, circle,fill=gray!80] (6) at (5,3) {6};

\path[draw,thick,->,>=latex] (1) -- (2);
\path[draw,thick,->,>=latex] (2) -- (3);
\path[draw,thick,->,>=latex] (4) -- (1);
\path[draw,thick,->,>=latex] (4) -- (5);
\path[draw,thick,->,>=latex] (5) -- (2);
\path[draw,thick,->,>=latex] (5) -- (3);
\path[draw,thick,->,>=latex] (3) -- (6);
\end{tikzpicture}
</script>

At this point, the list is `[6,3,2,1]`.
The next search begins at node 4:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle,fill=gray!80] (1) at (1,5) {1};
\node[draw, circle,fill=gray!80] (2) at (3,5) {2};
\node[draw, circle,fill=gray!80] (3) at (5,5) {3};
\node[draw, circle,fill=gray!40] (4) at (1,3) {4};
\node[draw, circle,fill=gray!80] (5) at (3,3) {5};
\node[draw, circle,fill=gray!80] (6) at (5,3) {6};

\path[draw,thick,->,>=latex] (1) -- (2);
\path[draw,thick,->,>=latex] (2) -- (3);
\path[draw,thick,->,>=latex] (4) -- (1);
%\path[draw,thick,->,>=latex] (4) -- (5);
\path[draw,thick,->,>=latex] (5) -- (2);
\path[draw,thick,->,>=latex] (5) -- (3);
\path[draw,thick,->,>=latex] (3) -- (6);

\path[draw=red,thick,->,line width=2pt] (4) -- (5);
\end{tikzpicture}
</script>

Thus, the final list is `[6,3,2,1,5,4]`.
We have processed all nodes, so a topological sort has
been found.
The topological sort is the reverse list
`[4,5,1,2,3,6]`:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (3,0) {1};
\node[draw, circle] (2) at (4.5,0) {2};
\node[draw, circle] (3) at (6,0) {3};
\node[draw, circle] (4) at (0,0) {4};
\node[draw, circle] (5) at (1.5,0) {5};
\node[draw, circle] (6) at (7.5,0) {6};

\path[draw,thick,->,>=latex] (1) -- (2);
\path[draw,thick,->,>=latex] (2) -- (3);
\path[draw,thick,->,>=latex] (4) edge [bend left=30] (1);
\path[draw,thick,->,>=latex] (4) -- (5);
\path[draw,thick,->,>=latex] (5) edge [bend right=30] (2);
\path[draw,thick,->,>=latex] (5) edge [bend right=40] (3);
\path[draw,thick,->,>=latex] (3) -- (6);
\end{tikzpicture}
</script>

Note that a topological sort is not unique,
and there can be several topological sorts for a graph.

## Example 2

Let us now consider a graph for which we
cannot construct a topological sort,
because the graph contains a cycle:

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
\path[draw,thick,->,>=latex] (4) -- (1);
\path[draw,thick,->,>=latex] (4) -- (5);
\path[draw,thick,->,>=latex] (5) -- (2);
\path[draw,thick,->,>=latex] (3) -- (5);
\path[draw,thick,->,>=latex] (3) -- (6);
\end{tikzpicture}
</script>

The search proceeds as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle,fill=gray!40] (1) at (1,5) {1};
\node[draw, circle,fill=gray!40] (2) at (3,5) {2};
\node[draw, circle,fill=gray!40] (3) at (5,5) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle,fill=gray!40] (5) at (3,3) {5};
\node[draw, circle] (6) at (5,3) {6};

\path[draw,thick,->,>=latex] (4) -- (1);
\path[draw,thick,->,>=latex] (4) -- (5);
\path[draw,thick,->,>=latex] (3) -- (6);

\path[draw=red,thick,->,line width=2pt] (1) -- (2);
\path[draw=red,thick,->,line width=2pt] (2) -- (3);
\path[draw=red,thick,->,line width=2pt] (3) -- (5);
\path[draw=red,thick,->,line width=2pt] (5) -- (2);
\end{tikzpicture}
</script>

The search reaches node 2 whose state is 1,
which means that the graph contains a cycle.
In this example, there is a cycle
$2 \rightarrow 3 \rightarrow 5 \rightarrow 2$.
