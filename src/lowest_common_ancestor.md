# Lowest common ancestor

The **lowest common ancestor**
of two nodes of a rooted tree is the lowest node
whose subtree contains both the nodes.
A typical problem is to efficiently process
queries that ask to find the lowest
common ancestor of two nodes.

For example, in the following tree,
the lowest common ancestor of nodes 5 and 8
is node 2:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (2,1) {4};
\node[draw, circle] (3) at (-2,1) {2};
\node[draw, circle] (4) at (0,1) {3};
\node[draw, circle] (5) at (2,-1) {7};
\node[draw, circle, fill=lightgray] (6) at (-3,-1) {5};
\node[draw, circle] (7) at (-1,-1) {6};
\node[draw, circle, fill=lightgray] (8) at (-1,-3) {8};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);
\path[draw,thick,-] (7) -- (8);

\path[draw=red,thick,->,line width=2pt] (6) edge [bend left] (3);
\path[draw=red,thick,->,line width=2pt] (8) edge [bend right=40] (3);
\end{tikzpicture}
</script>

Next we will discuss two efficient techniques for
finding the lowest common ancestor of two nodes.

## Method 1

One way to solve the problem is to use the fact
that we can efficiently find the $k$th
ancestor of any node in the tree.
Using this, we can divide the problem of
finding the lowest common ancestor into two parts.

We use two pointers that initially point to the
two nodes whose lowest common ancestor we should find.
First, we move one of the pointers upwards
so that both pointers point to nodes at the same level.

In the example scenario, we move the second pointer one
level up so that it points to node 6
which is at the same level with node 5:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (2,1) {4};
\node[draw, circle] (3) at (-2,1) {2};
\node[draw, circle] (4) at (0,1) {3};
\node[draw, circle] (5) at (2,-1) {7};
\node[draw, circle,fill=lightgray] (6) at (-3,-1) {5};
\node[draw, circle,fill=lightgray] (7) at (-1,-1) {6};
\node[draw, circle] (8) at (-1,-3) {8};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);
\path[draw,thick,-] (7) -- (8);

\path[draw=red,thick,->,line width=2pt] (8) edge [bend right] (7);
\end{tikzpicture}
</script>

After this, we determine the minimum number of steps
needed to move both pointers upwards so that
they will point to the same node.
The node to which the pointers point after this
is the lowest common ancestor.

In the example scenario, it suffices to move both pointers
one step upwards to node 2,
which is the lowest common ancestor:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (2,1) {4};
\node[draw, circle,fill=lightgray] (3) at (-2,1) {2};
\node[draw, circle] (4) at (0,1) {3};
\node[draw, circle] (5) at (2,-1) {7};
\node[draw, circle] (6) at (-3,-1) {5};
\node[draw, circle] (7) at (-1,-1) {6};
\node[draw, circle] (8) at (-1,-3) {8};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);
\path[draw,thick,-] (7) -- (8);

\path[draw=red,thick,->,line width=2pt] (6) edge [bend left] (3);
\path[draw=red,thick,->,line width=2pt] (7) edge [bend right] (3);
\end{tikzpicture}
</script>

Since both parts of the algorithm can be performed in
$O(\log n)$ time using precomputed information,
we can find the lowest common ancestor of any two
nodes in $O(\log n)$ time.

## Method 2

Another way to solve the problem is based on
a tree traversal array\footnote{}.
Once again, the idea is to traverse the nodes
using a depth-first search:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (2,1) {4};
\node[draw, circle] (3) at (-2,1) {2};
\node[draw, circle] (4) at (0,1) {3};
\node[draw, circle] (5) at (2,-1) {7};
\node[draw, circle] (6) at (-3,-1) {5};
\node[draw, circle] (7) at (-1,-1) {6};
\node[draw, circle] (8) at (-1,-3) {8};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);
\path[draw,thick,-] (7) -- (8);

\path[draw=red,thick,->,line width=2pt] (1) edge [bend right=15] (3);
\path[draw=red,thick,->,line width=2pt] (3) edge [bend right=15] (6);
\path[draw=red,thick,->,line width=2pt] (6) edge [bend right=15] (3);
\path[draw=red,thick,->,line width=2pt] (3) edge [bend right=15] (7);
\path[draw=red,thick,->,line width=2pt] (7) edge [bend right=15] (8);
\path[draw=red,thick,->,line width=2pt] (8) edge [bend right=15] (7);
\path[draw=red,thick,->,line width=2pt] (7) edge [bend right=15] (3);
\path[draw=red,thick,->,line width=2pt] (3) edge [bend right=15] (1);
\path[draw=red,thick,->,line width=2pt] (1) edge [bend right=15] (4);
\path[draw=red,thick,->,line width=2pt] (4) edge [bend right=15] (1);
\path[draw=red,thick,->,line width=2pt] (1) edge [bend right=15] (2);
\path[draw=red,thick,->,line width=2pt] (2) edge [bend right=15] (5);
\path[draw=red,thick,->,line width=2pt] (5) edge [bend right=15] (2);
\path[draw=red,thick,->,line width=2pt] (2) edge [bend right=15] (1);
\end{tikzpicture}
</script>

However, we use a different tree
traversal array than before:
we add each node to the array \emph{always}
when the depth-first search walks through the node,
and not only at the first visit.
Hence, a node that has $k$ children appears $k+1$ times
in the array and there are a total of $2n-1$
nodes in the array.

We store two values in the array:
the identifier of the node and the depth of the 
node in the tree.
The following array corresponds to the above tree:


<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]

\node[left] at (-1,1.5) {node id};
\node[left] at (-1,0.5) {depth};

\draw (0,1) grid (15,2);
\node at (0.5,1.5) {1};
\node at (1.5,1.5) {2};
\node at (2.5,1.5) {5};
\node at (3.5,1.5) {2};
\node at (4.5,1.5) {6};
\node at (5.5,1.5) {8};
\node at (6.5,1.5) {6};
\node at (7.5,1.5) {2};
\node at (8.5,1.5) {1};
\node at (9.5,1.5) {3};
\node at (10.5,1.5) {1};
\node at (11.5,1.5) {4};
\node at (12.5,1.5) {7};
\node at (13.5,1.5) {4};
\node at (14.5,1.5) {1};

\draw (0,0) grid (15,1);
\node at (0.5,0.5) {1};
\node at (1.5,0.5) {2};
\node at (2.5,0.5) {3};
\node at (3.5,0.5) {2};
\node at (4.5,0.5) {3};
\node at (5.5,0.5) {4};
\node at (6.5,0.5) {3};
\node at (7.5,0.5) {2};
\node at (8.5,0.5) {1};
\node at (9.5,0.5) {2};
\node at (10.5,0.5) {1};
\node at (11.5,0.5) {2};
\node at (12.5,0.5) {3};
\node at (13.5,0.5) {2};
\node at (14.5,0.5) {1};

\footnotesize
\node at (0.5,2.5) {0};
\node at (1.5,2.5) {1};
\node at (2.5,2.5) {2};
\node at (3.5,2.5) {3};
\node at (4.5,2.5) {4};
\node at (5.5,2.5) {5};
\node at (6.5,2.5) {6};
\node at (7.5,2.5) {7};
\node at (8.5,2.5) {8};
\node at (9.5,2.5) {9};
\node at (10.5,2.5) {10};
\node at (11.5,2.5) {11};
\node at (12.5,2.5) {12};
\node at (13.5,2.5) {13};
\node at (14.5,2.5) {14};
\end{tikzpicture}
</script>

Now we can find the lowest common ancestor
of nodes $a$ and $b$ by finding the node with the _minimum_ depth
between nodes $a$ and $b$ in the array.
For example, the lowest common ancestor of nodes $5$ and $8$
can be found as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\node[left] at (-1,1.5) {node id};
\node[left] at (-1,0.5) {depth};
\fill[color=lightgray] (2,1) rectangle (3,2);
\fill[color=lightgray] (5,1) rectangle (6,2);
\fill[color=lightgray] (2,0) rectangle (6,1);

\node at (3.5,-0.5) {\(\uparrow\)};
\draw (0,1) grid (15,2);
\node at (0.5,1.5) {1};
\node at (1.5,1.5) {2};
\node at (2.5,1.5) {5};
\node at (3.5,1.5) {2};
\node at (4.5,1.5) {6};
\node at (5.5,1.5) {8};
\node at (6.5,1.5) {6};
\node at (7.5,1.5) {2};
\node at (8.5,1.5) {1};
\node at (9.5,1.5) {3};
\node at (10.5,1.5) {1};
\node at (11.5,1.5) {4};
\node at (12.5,1.5) {7};
\node at (13.5,1.5) {4};
\node at (14.5,1.5) {1};
\draw (0,0) grid (15,1);
\node at (0.5,0.5) {1};
\node at (1.5,0.5) {2};
\node at (2.5,0.5) {3};
\node at (3.5,0.5) {2};
\node at (4.5,0.5) {3};
\node at (5.5,0.5) {4};
\node at (6.5,0.5) {3};
\node at (7.5,0.5) {2};
\node at (8.5,0.5) {1};
\node at (9.5,0.5) {2};
\node at (10.5,0.5) {1};
\node at (11.5,0.5) {2};
\node at (12.5,0.5) {3};
\node at (13.5,0.5) {2};
\node at (14.5,0.5) {1};

\footnotesize
\node at (0.5,2.5) {0};
\node at (1.5,2.5) {1};
\node at (2.5,2.5) {2};
\node at (3.5,2.5) {3};
\node at (4.5,2.5) {4};
\node at (5.5,2.5) {5};
\node at (6.5,2.5) {6};
\node at (7.5,2.5) {7};
\node at (8.5,2.5) {8};
\node at (9.5,2.5) {9};
\node at (10.5,2.5) {10};
\node at (11.5,2.5) {11};
\node at (12.5,2.5) {12};
\node at (13.5,2.5) {13};
\node at (14.5,2.5) {14};
\end{tikzpicture}
</script>

Node 5 is at position 2, node 8 is at position 5,
and the node with minimum depth between
positions $2 \ldots 5$ is node 2 at position 3
whose depth is 2.
Thus, the lowest common ancestor of
nodes 5 and 8 is node 2.

Thus, to find the lowest common ancestor
of two nodes it suffices to process a range
minimum query.
Since the array is static,
we can process such queries in $O(1)$ time
after an $O(n \log n)$ time preprocessing.

The distance between nodes $a$ and $b$
equals the length of the path from $a$ to $b$.
It turns out that the problem of calculating
the distance between nodes reduces to
finding their lowest common ancestor.

First, we root the tree arbitrarily.
After this, the distance of nodes $a$ and $b$
can be calculated using the formula

\\[
\\texttt{depth}(a)+\\texttt{depth}(b)-2 \\cdot \\texttt{depth}(c)
\\]

where $c$ is the lowest common ancestor of $a$ and $b$
and `depth(s)` denotes the depth of node $s$.
For example, consider the distance of nodes 5 and 8:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (2,1) {4};
\node[draw, circle] (3) at (-2,1) {2};
\node[draw, circle] (4) at (0,1) {3};
\node[draw, circle] (5) at (2,-1) {7};
\node[draw, circle, fill=lightgray] (6) at (-3,-1) {5};
\node[draw, circle] (7) at (-1,-1) {6};
\node[draw, circle, fill=lightgray] (8) at (-1,-3) {8};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);
\path[draw,thick,-] (7) -- (8);

\path[draw=red,thick,->,line width=2pt] (6) edge [bend left] (3);
\path[draw=red,thick,->,line width=2pt] (8) edge [bend right=40] (3);
\end{tikzpicture}
</script>

The lowest common ancestor of nodes 5 and 8 is node 2.
The depths of the nodes are
`depth(5)=3`, `depth(8)=4` and `depth(2)=2`,
so the distance between nodes 5 and 8 is
$3+4-2\cdot2=3$.

___

[^1] This lowest common ancestor algorithm was presented in [7].  This technique is sometimes called the **Euler tour technique** [66].
