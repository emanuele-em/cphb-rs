# Tree algorithms

A **tree** is a connected, acyclic graph
that consists of $n$ nodes and $n-1$ edges.
Removing any edge from a tree divides it
into two components,
and adding any edge to a tree creates a cycle.
Moreover, there is always a unique path between any
two nodes of a tree.

For example, the following tree consists of 8 nodes and 7 edges:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (2,3) {4};
\node[draw, circle] (3) at (0,1) {2};
\node[draw, circle] (4) at (2,1) {3};
\node[draw, circle] (5) at (4,1) {7};
\node[draw, circle] (6) at (-2,3) {5};
\node[draw, circle] (7) at (-2,1) {6};
\node[draw, circle] (8) at (-4,1) {8};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);
\path[draw,thick,-] (7) -- (8);
\end{tikzpicture}
</script>

The **leaves** of a tree are the nodes
with degree 1, i.e., with only one neighbor.
For example, the leaves of the above tree
are nodes 3, 5, 7 and 8.

In a **rooted** tree, one of the nodes
is appointed the **root** of the tree,
and all other nodes are
placed underneath the root.
For example, in the following tree,
node 1 is the root node.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (4) at (2,1) {4};
\node[draw, circle] (2) at (-2,1) {2};
\node[draw, circle] (3) at (0,1) {3};
\node[draw, circle] (7) at (2,-1) {7};
\node[draw, circle] (5) at (-3,-1) {5};
\node[draw, circle] (6) at (-1,-1) {6};
\node[draw, circle] (8) at (-1,-3) {8};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (2) -- (6);
\path[draw,thick,-] (4) -- (7);
\path[draw,thick,-] (6) -- (8);
\end{tikzpicture}
</script>

In a rooted tree, the **children** of a node
are its lower neighbors, and the **parent** of a node
is its upper neighbor.
Each node has exactly one parent,
except for the root that does not have a parent.
For example, in the above tree,
the children of node 2 are nodes 5 and 6,
and its parent is node 1.

The structure of a rooted tree is _recursive_:
each node of the tree acts as the root of a **subtree**
that contains the node itself and all nodes
that are in the subtrees of its children.
For example, in the above tree, the subtree of node 2
consists of nodes 2, 5, 6 and 8:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (2) at (-2,1) {2};
\node[draw, circle] (5) at (-3,-1) {5};
\node[draw, circle] (6) at (-1,-1) {6};
\node[draw, circle] (8) at (-1,-3) {8};
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (2) -- (6);
\path[draw,thick,-] (6) -- (8);
\end{tikzpicture}
</script>
