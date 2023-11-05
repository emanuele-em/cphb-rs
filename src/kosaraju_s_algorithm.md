# Kosaraju’s algorithm

**Kosaraju's algorithm**[^1] is an efficient
method for finding the strongly connected components
of a directed graph.
The algorithm performs two depth-first searches:
the first search constructs a list of nodes
according to the structure of the graph,
and the second search forms the strongly connected components.

## Search 1

The first phase of Kosaraju's algorithm constructs
a list of nodes in the order in which a
depth-first search processes them.
The algorithm goes through the nodes,
and begins a depth-first search at each 
unprocessed node.
Each node will be added to the list
after it has been processed.

In the example graph, the nodes are processed
in the following order:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9,label distance=-2mm]
\node[draw, circle] (1) at (-1,1) {7};
\node[draw, circle] (2) at (-3,2) {3};
\node[draw, circle] (4) at (-5,2) {2};
\node[draw, circle] (6) at (-7,2) {1};
\node[draw, circle] (3) at (-3,0) {6};
\node[draw, circle] (5) at (-5,0) {5};
\node[draw, circle] (7) at (-7,0) {4};

\node at (-7,2.75) {1/8};
\node at (-5,2.75) {2/7};
\node at (-3,2.75) {9/14};
\node at (-7,-0.75) {4/5};
\node at (-5,-0.75) {3/6};
\node at (-3,-0.75) {11/12};
\node at (-1,1.75) {10/13};

\path[draw,thick,->] (2) -- (1);
\path[draw,thick,->] (1) -- (3);
\path[draw,thick,->] (3) -- (2);
\path[draw,thick,->] (2) -- (4);
\path[draw,thick,->] (3) -- (5);
\path[draw,thick,->] (4) edge [bend left] (6);
\path[draw,thick,->] (6) edge [bend left] (4);
\path[draw,thick,->] (4) -- (5);
\path[draw,thick,->] (5) -- (7);
\path[draw,thick,->] (6) -- (7);
\end{tikzpicture}
</script>

The notation $x/y$ means that
processing the node started
at time $x$ and finished at time $y$.
Thus, the corresponding list is as follows:

| node | processing time |
| ---- | --------------- |
| 4 | 5 |
| 5 | 6 |
| 2 | 7 |
| 1 | 8 |
| 6 | 12 |
| 7 | 13 |
| 3 | 14 |

## Search 2

The second phase of the algorithm
forms the strongly connected components
of the graph.
First, the algorithm reverses every
edge in the graph.
This guarantees that during the second search,
we will always find strongly connected
components that do not have extra nodes.

After reversing the edges,
the example graph is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9,label distance=-2mm]
\node[draw, circle] (1) at (-1,1) {7};
\node[draw, circle] (2) at (-3,2) {3};
\node[draw, circle] (4) at (-5,2) {2};
\node[draw, circle] (6) at (-7,2) {1};
\node[draw, circle] (3) at (-3,0) {6};
\node[draw, circle] (5) at (-5,0) {5};
\node[draw, circle] (7) at (-7,0) {4};

\path[draw,thick,<-] (2) -- (1);
\path[draw,thick,<-] (1) -- (3);
\path[draw,thick,<-] (3) -- (2);
\path[draw,thick,<-] (2) -- (4);
\path[draw,thick,<-] (3) -- (5);
\path[draw,thick,<-] (4) edge [bend left] (6);
\path[draw,thick,<-] (6) edge [bend left] (4);
\path[draw,thick,<-] (4) -- (5);
\path[draw,thick,<-] (5) -- (7);
\path[draw,thick,<-] (6) -- (7);
\end{tikzpicture}
</script>

After this, the algorithm goes through
the list of nodes created by the first search,
in _reverse_ order.
If a node does not belong to a component,
the algorithm creates a new component
and starts a depth-first search
that adds all new nodes found during the search
to the new component.

In the example graph, the first component
begins at node 3:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9,label distance=-2mm]
\node[draw, circle] (1) at (-1,1) {7};
\node[draw, circle] (2) at (-3,2) {3};
\node[draw, circle] (4) at (-5,2) {2};
\node[draw, circle] (6) at (-7,2) {1};
\node[draw, circle] (3) at (-3,0) {6};
\node[draw, circle] (5) at (-5,0) {5};
\node[draw, circle] (7) at (-7,0) {4};

\path[draw,thick,<-] (2) -- (1);
\path[draw,thick,<-] (1) -- (3);
\path[draw,thick,<-] (3) -- (2);
\path[draw,thick,<-] (2) -- (4);
\path[draw,thick,<-] (3) -- (5);
\path[draw,thick,<-] (4) edge [bend left] (6);
\path[draw,thick,<-] (6) edge [bend left] (4);
\path[draw,thick,<-] (4) -- (5);
\path[draw,thick,<-] (5) -- (7);
\path[draw,thick,<-] (6) -- (7);

\draw [red,thick,dashed,line width=2pt] (-0.5,2.5) rectangle (-3.5,-0.5);
\end{tikzpicture}
</script>

Note that since all edges are reversed,
the component does not _leak_ to other parts in the graph.

The next nodes in the list are nodes 7 and 6,
but they already belong to a component,
so the next new component begins at node 1:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9,label distance=-2mm]
\node[draw, circle] (1) at (-1,1) {7};
\node[draw, circle] (2) at (-3,2) {3};
\node[draw, circle] (4) at (-5,2) {2};
\node[draw, circle] (6) at (-7,2) {1};
\node[draw, circle] (3) at (-3,0) {6};
\node[draw, circle] (5) at (-5,0) {5};
\node[draw, circle] (7) at (-7,0) {4};

\path[draw,thick,<-] (2) -- (1);
\path[draw,thick,<-] (1) -- (3);
\path[draw,thick,<-] (3) -- (2);
\path[draw,thick,<-] (2) -- (4);
\path[draw,thick,<-] (3) -- (5);
\path[draw,thick,<-] (4) edge [bend left] (6);
\path[draw,thick,<-] (6) edge [bend left] (4);
\path[draw,thick,<-] (4) -- (5);
\path[draw,thick,<-] (5) -- (7);
\path[draw,thick,<-] (6) -- (7);

\draw [red,thick,dashed,line width=2pt] (-0.5,2.5) rectangle (-3.5,-0.5);
\draw [red,thick,dashed,line width=2pt] (-4.5,2.5) rectangle (-7.5,1.5);
%\draw [red,thick,dashed,line width=2pt] (-4.5,0.5) rectangle (-5.5,-0.5);
%\draw [red,thick,dashed,line width=2pt] (-6.5,0.5) rectangle (-7.5,-0.5);
\end{tikzpicture}
</script>

Finally, the algorithm processes nodes 5 and 4
that create the remaining strongly connected components:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9,label distance=-2mm]
\node[draw, circle] (1) at (-1,1) {7};
\node[draw, circle] (2) at (-3,2) {3};
\node[draw, circle] (4) at (-5,2) {2};
\node[draw, circle] (6) at (-7,2) {1};
\node[draw, circle] (3) at (-3,0) {6};
\node[draw, circle] (5) at (-5,0) {5};
\node[draw, circle] (7) at (-7,0) {4};

\path[draw,thick,<-] (2) -- (1);
\path[draw,thick,<-] (1) -- (3);
\path[draw,thick,<-] (3) -- (2);
\path[draw,thick,<-] (2) -- (4);
\path[draw,thick,<-] (3) -- (5);
\path[draw,thick,<-] (4) edge [bend left] (6);
\path[draw,thick,<-] (6) edge [bend left] (4);
\path[draw,thick,<-] (4) -- (5);
\path[draw,thick,<-] (5) -- (7);
\path[draw,thick,<-] (6) -- (7);

\draw [red,thick,dashed,line width=2pt] (-0.5,2.5) rectangle (-3.5,-0.5);
\draw [red,thick,dashed,line width=2pt] (-4.5,2.5) rectangle (-7.5,1.5);
\draw [red,thick,dashed,line width=2pt] (-4.5,0.5) rectangle (-5.5,-0.5);
\draw [red,thick,dashed,line width=2pt] (-6.5,0.5) rectangle (-7.5,-0.5);
\end{tikzpicture}
</script>

The time complexity of the algorithm is $O(n+m)$,
because the algorithm
performs two depth-first searches.

___

[^1] According to [1], S. R. Kosaraju invented this algorithm in 1978 but did not publish it. In 1981, the same algorithm was rediscovered and published by M. Sharir [57].
