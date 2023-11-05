# Strong connectivity

In a directed graph,
the edges can be traversed in one direction only,
so even if the graph is connected,
this does not guarantee that there would be
a path from a node to another node.
For this reason, it is meaningful to define a new concept
that requires more than connectivity.

A graph is **strongly connected**
if there is a path from any node to all
other nodes in the graph.
For example, in the following picture,
the left graph is strongly connected
while the right graph is not.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,1) {1};
\node[draw, circle] (2) at (3,1) {2};
\node[draw, circle] (3) at (1,-1) {3};
\node[draw, circle] (4) at (3,-1) {4};

\path[draw,thick,->] (1) -- (2);
\path[draw,thick,->] (2) -- (4);
\path[draw,thick,->] (4) -- (3);
\path[draw,thick,->] (3) -- (1);

\node[draw, circle] (1b) at (6,1) {1};
\node[draw, circle] (2b) at (8,1) {2};
\node[draw, circle] (3b) at (6,-1) {3};
\node[draw, circle] (4b) at (8,-1) {4};

\path[draw,thick,->] (1b) -- (2b);
\path[draw,thick,->] (2b) -- (4b);
\path[draw,thick,->] (4b) -- (3b);
\path[draw,thick,->] (1b) -- (3b);
\end{tikzpicture}

</script>

The right graph is not strongly connected
because, for example, there is no path
from node 2 to node 1.

The **strongly connected components**
of a graph divide the graph into strongly connected
parts that are as large as possible.
The strongly connected components form an
acyclic **component graph** that represents
the deep structure of the original graph.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9,label distance=-2mm]
\node[draw, circle] (1) at (-1,1) {7};
\node[draw, circle] (2) at (-3,2) {3};
\node[draw, circle] (4) at (-5,2) {2};
\node[draw, circle] (6) at (-7,2) {1};
\node[draw, circle] (3) at (-3,0) {6};
\node[draw, circle] (5) at (-5,0) {5};
\node[draw, circle] (7) at (-7,0) {4};

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

the strongly connected components are as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (-1,1) {7};
\node[draw, circle] (2) at (-3,2) {3};
\node[draw, circle] (4) at (-5,2) {2};
\node[draw, circle] (6) at (-7,2) {1};
\node[draw, circle] (3) at (-3,0) {6};
\node[draw, circle] (5) at (-5,0) {5};
\node[draw, circle] (7) at (-7,0) {4};

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

\draw [red,thick,dashed,line width=2pt] (-0.5,2.5) rectangle (-3.5,-0.5);
\draw [red,thick,dashed,line width=2pt] (-4.5,2.5) rectangle (-7.5,1.5);
\draw [red,thick,dashed,line width=2pt] (-4.5,0.5) rectangle (-5.5,-0.5);
\draw [red,thick,dashed,line width=2pt] (-6.5,0.5) rectangle (-7.5,-0.5);
\end{tikzpicture}
</script>

The corresponding component graph is as follows:


<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (-3,1) {B};
\node[draw, circle] (2) at (-6,2) {A};
\node[draw, circle] (3) at (-5,0) {D};
\node[draw, circle] (4) at (-7,0) {C};

\path[draw,thick,->] (1) -- (2);
\path[draw,thick,->] (1) -- (3);
\path[draw,thick,->] (2) -- (3);
\path[draw,thick,->] (2) -- (4);
\path[draw,thick,->] (3) -- (4);
\end{tikzpicture}
</script>

The components are \(A=\\{1,2\\}\),
\(B=\\{3,6,7\\}\), \(C=\\{4\\}\) and \(D=\\{5\\}\).

A component graph is an acyclic, directed graph,
so it is easier to process than the original graph.
Since the graph does not contain cycles,
we can always construct a topological sort and
use dynamic programming techniques like those
presented in Chapter 16.
