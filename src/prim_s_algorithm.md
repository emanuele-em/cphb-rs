# Prim’s algorithm

Prim's algorithm[^1] is an alternative method
for finding a minimum spanning tree.
The algorithm first adds an arbitrary node
to the tree.
After this, the algorithm always chooses
a minimum-weight edge that
adds a new node to the tree.
Finally, all nodes have been added to the tree
and a minimum spanning tree has been found.

Prim's algorithm resembles Dijkstra's algorithm.
The difference is that Dijkstra's algorithm always
selects an edge whose distance from the starting
node is minimum, but Prim's algorithm simply selects
the minimum weight edge that adds a new node to the tree.

## Example

Let us consider how Prim's algorithm works
in the following graph:

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

%\path[draw=red,thick,-,line width=2pt] (5) -- (6);
\end{tikzpicture}
</script>

Initially, there are no edges between the nodes:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
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
%\path[draw,thick,-] (5) -- node[font=\small,label=below:2] {} (6);
%\path[draw,thick,-] (6) -- node[font=\small,label=below:7] {} (4);
%\path[draw,thick,-] (2) -- node[font=\small,label=left:6] {} (5);
%\path[draw,thick,-] (3) -- node[font=\small,label=left:3] {} (6);
\end{tikzpicture}
</script>

An arbitrary node can be the starting node,
so let us choose node 1.
First, we add node 2 that is connected by
an edge of weight 3:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
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
%\path[draw,thick,-] (5) -- node[font=\small,label=below:2] {} (6);
%\path[draw,thick,-] (6) -- node[font=\small,label=below:7] {} (4);
%\path[draw,thick,-] (2) -- node[font=\small,label=left:6] {} (5);
%\path[draw,thick,-] (3) -- node[font=\small,label=left:3] {} (6);
\end{tikzpicture}
</script>

After this, there are two edges with weight 5,
so we can add either node 3 or node 5 to the tree.
Let us add node 3 first:

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
%\path[draw,thick,-] (3) -- node[font=\small,label=above:9] {} (4);
%\path[draw,thick,-] (1) -- node[font=\small,label=below:5] {} (5);
%\path[draw,thick,-] (5) -- node[font=\small,label=below:2] {} (6);
%\path[draw,thick,-] (6) -- node[font=\small,label=below:7] {} (4);
%\path[draw,thick,-] (2) -- node[font=\small,label=left:6] {} (5);
%\path[draw,thick,-] (3) -- node[font=\small,label=left:3] {} (6);
\end{tikzpicture}
</script>

The process continues until all nodes have been included in the tree:

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
%\path[draw,thick,-] (3) -- node[font=\small,label=above:9] {} (4);
%\path[draw,thick,-] (1) -- node[font=\small,label=below:5] {} (5);
\path[draw,thick,-] (5) -- node[font=\small,label=below:2] {} (6);
\path[draw,thick,-] (6) -- node[font=\small,label=below:7] {} (4);
%\path[draw,thick,-] (2) -- node[font=\small,label=left:6] {} (5);
\path[draw,thick,-] (3) -- node[font=\small,label=left:3] {} (6);
\end{tikzpicture}
</script>

## Implementation

Like Dijkstra's algorithm, Prim's algorithm can be
efficiently implemented using a priority queue.
The priority queue should contain all nodes
that can be connected to the current component using
a single edge, in increasing order of the weights
of the corresponding edges.

The time complexity of Prim's algorithm is
$O(n + m \log m)$ that equals the time complexity
of Dijkstra's algorithm.
In practice, Prim's and Kruskal's algorithms
are both efficient, and the choice of the algorithm
is a matter of taste.
Still, most competitive programmers use Kruskal's algorithm.

___

[^1] The algorithm is named after R. C. Prim who published it in 1957 [54].  However, the same algorithm was discovered already in 1930 by V. Jarník.
