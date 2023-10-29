# Diameter

The **diameter** of a tree
is the maximum length of a path between two nodes.
For example, consider the following tree:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (2,3) {4};
\node[draw, circle] (3) at (0,1) {2};
\node[draw, circle] (4) at (2,1) {3};
\node[draw, circle] (5) at (4,1) {7};
\node[draw, circle] (6) at (-2,3) {5};
\node[draw, circle] (7) at (-2,1) {6};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);
\end{tikzpicture}
</script>

The diameter of this tree is 4,
which corresponds to the following path:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (2,3) {4};
\node[draw, circle] (3) at (0,1) {2};
\node[draw, circle] (4) at (2,1) {3};
\node[draw, circle] (5) at (4,1) {7};
\node[draw, circle] (6) at (-2,3) {5};
\node[draw, circle] (7) at (-2,1) {6};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);

\path[draw,thick,-,color=red,line width=2pt] (7) -- (3);
\path[draw,thick,-,color=red,line width=2pt] (3) -- (1);
\path[draw,thick,-,color=red,line width=2pt] (1) -- (2);
\path[draw,thick,-,color=red,line width=2pt] (2) -- (5);
\end{tikzpicture}
</script>

Note that there may be several maximum-length paths.
In the above path, we could replace node 6 with node 5
to obtain another path with length 4.

Next we will discuss two $O(n)$ time algorithms
for calculating the diameter of a tree.
The first algorithm is based on dynamic programming,
and the second algorithm uses two depth-first searches.

## Algorithm 1

A general way to approach many tree problems
is to first root the tree arbitrarily.
After this, we can try to solve the problem
separately for each subtree.
Our first algorithm for calculating the diameter
is based on this idea.

An important observation is that every path
in a rooted tree has a _highest point_:
the highest node that belongs to the path.
Thus, we can calculate for each node the length
of the longest path whose highest point is the node.
One of those paths corresponds to the diameter of the tree.

For example, in the following tree,
node 1 is the highest point on the path
that corresponds to the diameter:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (2,1) {4};
\node[draw, circle] (3) at (-2,1) {2};
\node[draw, circle] (4) at (0,1) {3};
\node[draw, circle] (5) at (2,-1) {7};
\node[draw, circle] (6) at (-3,-1) {5};
\node[draw, circle] (7) at (-1,-1) {6};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);

\path[draw,thick,-,color=red,line width=2pt] (7) -- (3);
\path[draw,thick,-,color=red,line width=2pt] (3) -- (1);
\path[draw,thick,-,color=red,line width=2pt] (1) -- (2);
\path[draw,thick,-,color=red,line width=2pt] (2) -- (5);
\end{tikzpicture}
</script>

We calculate for each node $x$ two values:

- `to_leaf(x)`: the maximum length of a path from `x` to any leaf
- `max_length(x)`: the maximum length of a path whose highest point is $x$

For example, in the above tree,
`to_leaf(1)=2`, because there is a path
$1 \rightarrow 2 \rightarrow 6$,
and `max_length(1)=4`,
because there is a path
$6 \rightarrow 2 \rightarrow 1 \rightarrow 4 \rightarrow 7$.
In this case, `max_length(1)` equals the diameter.

Dynamic programming can be used to calculate the above
values for all nodes in $O(n)$ time.
First, to calculate `to_leaf(x)`,
we go through the children of $x$,
choose a child $c$ with maximum `to_leaf(c)`
and add one to this value.
Then, to calculate `max_length(x)`,
we choose two distinct children $a$ and $b$
such that the sum `to_leaf(a)+to_leaf(b)`
is maximum and add two to this sum.

## Algorithm 2

Another efficient way to calculate the diameter
of a tree is based on two depth-first searches.
First, we choose an arbitrary node $a$ in the tree
and find the farthest node $b$ from $a$.
Then, we find the farthest node $c$ from $b$.
The diameter of the tree is the distance between $b$ and $c$.

In the following graph, $a$, $b$ and $c$ could be:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (2,3) {4};
\node[draw, circle] (3) at (0,1) {2};
\node[draw, circle] (4) at (2,1) {3};
\node[draw, circle] (5) at (4,1) {7};
\node[draw, circle] (6) at (-2,3) {5};
\node[draw, circle] (7) at (-2,1) {6};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);
\node[color=red] at (2,1.6) {a};
\node[color=red] at (-2,1.6) {b};
\node[color=red] at (4,1.6) {c};

\path[draw,thick,-,color=red,line width=2pt] (7) -- (3);
\path[draw,thick,-,color=red,line width=2pt] (3) -- (1);
\path[draw,thick,-,color=red,line width=2pt] (1) -- (2);
\path[draw,thick,-,color=red,line width=2pt] (2) -- (5);
\end{tikzpicture}
</script>

This is an elegant method, but why does it work?

It helps to draw the tree differently so that
the path that corresponds to the diameter
is horizontal, and all other
nodes hang from it:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (2,1) {1};
\node[draw, circle] (2) at (4,1) {4};
\node[draw, circle] (3) at (0,1) {2};
\node[draw, circle] (4) at (2,-1) {3};
\node[draw, circle] (5) at (6,1) {7};
\node[draw, circle] (6) at (0,-1) {5};
\node[draw, circle] (7) at (-2,1) {6};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);
\node[color=red] at (2,-1.6) {a};
\node[color=red] at (-2,1.6) {b};
\node[color=red] at (6,1.6) {c};
\node[color=red] at (2,1.6) {x};

\path[draw,thick,-,color=red,line width=2pt] (7) -- (3);
\path[draw,thick,-,color=red,line width=2pt] (3) -- (1);
\path[draw,thick,-,color=red,line width=2pt] (1) -- (2);
\path[draw,thick,-,color=red,line width=2pt] (2) -- (5);
\end{tikzpicture}
</script>

Node $x$ indicates the place where the path
from node $a$ joins the path that corresponds
to the diameter.
The farthest node from $a$
is node $b$, node $c$ or some other node
that is at least as far from node $x$.
Thus, this node is always a valid choice for
an endpoint of a path that corresponds to the diameter.

