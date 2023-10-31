# Spanning trees

A **spanning tree** of a graph consists of
all nodes of the graph and some of the
edges of the graph so that there is a path
between any two nodes.
Like trees in general, spanning trees are
connected and acyclic.
Usually there are several ways to construct a spanning tree.

For example, consider the following graph:

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

One spanning tree for the graph is as follows:

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
\path[draw,thick,-] (5) -- node[font=\small,label=below:2] {} (6);
\path[draw,thick,-] (3) -- node[font=\small,label=left:3] {} (6);
\end{tikzpicture}
</script>

The weight of a spanning tree is the sum of its edge weights.
For example, the weight of the above spanning tree is
$3+5+9+3+2=22$.

A **minimum spanning tree**
is a spanning tree whose weight is as small as possible.
The weight of a minimum spanning tree for the example graph
is 20, and such a tree can be constructed as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1.5,2) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (6.5,2) {4};
\node[draw, circle] (5) at (3,1) {5};
\node[draw, circle] (6) at (5,1) {6};

\path[draw,thick,-] (1) -- node[font=\small,label=above:3] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=below:5] {} (5);
\path[draw,thick,-] (5) -- node[font=\small,label=below:2] {} (6);
\path[draw,thick,-] (6) -- node[font=\small,label=below:7] {} (4);
\path[draw,thick,-] (3) -- node[font=\small,label=left:3] {} (6);
\end{tikzpicture}
</script>

In a similar way, a **maximum spanning tree**
is a spanning tree whose weight is as large as possible.
The weight of a maximum spanning tree for the
example graph is 32:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1.5,2) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (6.5,2) {4};
\node[draw, circle] (5) at (3,1) {5};
\node[draw, circle] (6) at (5,1) {6};
\path[draw,thick,-] (2) -- node[font=\small,label=above:5] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=above:9] {} (4);
\path[draw,thick,-] (1) -- node[font=\small,label=below:5] {} (5);
\path[draw,thick,-] (6) -- node[font=\small,label=below:7] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:6] {} (5);
\end{tikzpicture}
</script>


Note that a graph may have several
minimum and maximum spanning trees,
so the trees are not unique.

It turns out that several greedy methods
can be used to construct minimum and maximum
spanning trees.
In this chapter, we discuss two algorithms
that process
the edges of the graph ordered by their weights.
We focus on finding minimum spanning trees,
but the same algorithms can find
maximum spanning trees by processing the edges in reverse order.
