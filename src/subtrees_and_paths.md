# Subtrees and paths

A **tree traversal array** contains the nodes of a rooted tree
in the order in which a depth-first search
from the root node visits them.
For example, in the tree

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (-3,1) {2};
\node[draw, circle] (3) at (-1,1) {3};
\node[draw, circle] (4) at (1,1) {4};
\node[draw, circle] (5) at (3,1) {5};
\node[draw, circle] (6) at (-3,-1) {6};
\node[draw, circle] (7) at (-0.5,-1) {7};
\node[draw, circle] (8) at (1,-1) {8};
\node[draw, circle] (9) at (2.5,-1) {9};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (1) -- (5);
\path[draw,thick,-] (2) -- (6);
\path[draw,thick,-] (4) -- (7);
\path[draw,thick,-] (4) -- (8);
\path[draw,thick,-] (4) -- (9);
\end{tikzpicture}
</script>

a depth-first search proceeds as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (-3,1) {2};
\node[draw, circle] (3) at (-1,1) {3};
\node[draw, circle] (4) at (1,1) {4};
\node[draw, circle] (5) at (3,1) {5};
\node[draw, circle] (6) at (-3,-1) {6};
\node[draw, circle] (7) at (-0.5,-1) {7};
\node[draw, circle] (8) at (1,-1) {8};
\node[draw, circle] (9) at (2.5,-1) {9};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (1) -- (5);
\path[draw,thick,-] (2) -- (6);
\path[draw,thick,-] (4) -- (7);
\path[draw,thick,-] (4) -- (8);
\path[draw,thick,-] (4) -- (9);


\path[draw=red,thick,->,line width=2pt] (1) edge [bend right=15] (2);
\path[draw=red,thick,->,line width=2pt] (2) edge [bend right=15] (6);
\path[draw=red,thick,->,line width=2pt] (6) edge [bend right=15] (2);
\path[draw=red,thick,->,line width=2pt] (2) edge [bend right=15] (1);
\path[draw=red,thick,->,line width=2pt] (1) edge [bend right=15] (3);
\path[draw=red,thick,->,line width=2pt] (3) edge [bend right=15] (1);
\path[draw=red,thick,->,line width=2pt] (1) edge [bend right=15] (4);
\path[draw=red,thick,->,line width=2pt] (4) edge [bend right=15] (7);
\path[draw=red,thick,->,line width=2pt] (7) edge [bend right=15] (4);
\path[draw=red,thick,->,line width=2pt] (4) edge [bend right=15] (8);
\path[draw=red,thick,->,line width=2pt] (8) edge [bend right=15] (4);
\path[draw=red,thick,->,line width=2pt] (4) edge [bend right=15] (9);
\path[draw=red,thick,->,line width=2pt] (9) edge [bend right=15] (4);
\path[draw=red,thick,->,line width=2pt] (4) edge [bend right=15] (1);
\path[draw=red,thick,->,line width=2pt] (1) edge [bend right=15] (5);
\path[draw=red,thick,->,line width=2pt] (5) edge [bend right=15] (1);

\end{tikzpicture}
</script>

Hence, the corresponding tree traversal array is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (9,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {2};
\node at (2.5,0.5) {6};
\node at (3.5,0.5) {3};
\node at (4.5,0.5) {4};
\node at (5.5,0.5) {7};
\node at (6.5,0.5) {8};
\node at (7.5,0.5) {9};
\node at (8.5,0.5) {5};
% 
% \footnotesize
% \node at (0.5,1.4) {1};
% \node at (1.5,1.4) {2};
% \node at (2.5,1.4) {3};
% \node at (3.5,1.4) {4};
% \node at (4.5,1.4) {5};
% \node at (5.5,1.4) {6};
% \node at (6.5,1.4) {7};
% \node at (7.5,1.4) {8};
% \node at (8.5,1.4) {9};
\end{tikzpicture}
</script>

## Subtree queries

Each subtree of a tree corresponds to a subarray
of the tree traversal array such that
the first element of the subarray is the root node.
For example, the following subarray contains the
nodes of the subtree of node $4$:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (4,0) rectangle (8,1);
\draw (0,0) grid (9,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {2};
\node at (2.5,0.5) {6};
\node at (3.5,0.5) {3};
\node at (4.5,0.5) {4};
\node at (5.5,0.5) {7};
\node at (6.5,0.5) {8};
\node at (7.5,0.5) {9};
\node at (8.5,0.5) {5};
% 
% \footnotesize
% \node at (0.5,1.4) {1};
% \node at (1.5,1.4) {2};
% \node at (2.5,1.4) {3};
% \node at (3.5,1.4) {4};
% \node at (4.5,1.4) {5};
% \node at (5.5,1.4) {6};
% \node at (6.5,1.4) {7};
% \node at (7.5,1.4) {8};
% \node at (8.5,1.4) {9};
\end{tikzpicture}
</script>

Using this fact, we can efficiently process queries
that are related to subtrees of a tree.
As an example, consider a problem where each node
is assigned a value, and our task is to support
the following queries:

- update the value of a node
- calculate the sum of values in the subtree of a node

Consider the following tree where the blue numbers
are the values of the nodes.
For example, the sum of the subtree of node $4$
is $3+4+3+1=11$.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (-3,1) {2};
\node[draw, circle] (3) at (-1,1) {3};
\node[draw, circle] (4) at (1,1) {4};
\node[draw, circle] (5) at (3,1) {5};
\node[draw, circle] (6) at (-3,-1) {6};
\node[draw, circle] (7) at (-0.5,-1) {7};
\node[draw, circle] (8) at (1,-1) {8};
\node[draw, circle] (9) at (2.5,-1) {9};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (1) -- (5);
\path[draw,thick,-] (2) -- (6);
\path[draw,thick,-] (4) -- (7);
\path[draw,thick,-] (4) -- (8);
\path[draw,thick,-] (4) -- (9);

\node[color=blue] at (0,3+0.65) {2};
\node[color=blue] at (-3-0.65,1) {3};
\node[color=blue] at (-1-0.65,1) {5};
\node[color=blue] at (1+0.65,1) {3};
\node[color=blue] at (3+0.65,1) {1};
\node[color=blue] at (-3,-1-0.65) {4};
\node[color=blue] at (-0.5,-1-0.65) {4};
\node[color=blue] at (1,-1-0.65) {3};
\node[color=blue] at (2.5,-1-0.65) {1};
\end{tikzpicture}
</script>

The idea is to construct a tree traversal array that contains
three values for each node: the identifier of the node,
the size of the subtree, and the value of the node.
For example, the array for the above tree is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,1) grid (9,-2);

\node[left] at (-1,0.5) {node id};
\node[left] at (-1,-0.5) {subtree size};
\node[left] at (-1,-1.5) {node value};

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {2};
\node at (2.5,0.5) {6};
\node at (3.5,0.5) {3};
\node at (4.5,0.5) {4};
\node at (5.5,0.5) {7};
\node at (6.5,0.5) {8};
\node at (7.5,0.5) {9};
\node at (8.5,0.5) {5};

\node at (0.5,-0.5) {9};
\node at (1.5,-0.5) {2};
\node at (2.5,-0.5) {1};
\node at (3.5,-0.5) {1};
\node at (4.5,-0.5) {4};
\node at (5.5,-0.5) {1};
\node at (6.5,-0.5) {1};
\node at (7.5,-0.5) {1};
\node at (8.5,-0.5) {1};

\node at (0.5,-1.5) {2};
\node at (1.5,-1.5) {3};
\node at (2.5,-1.5) {4};
\node at (3.5,-1.5) {5};
\node at (4.5,-1.5) {3};
\node at (5.5,-1.5) {4};
\node at (6.5,-1.5) {3};
\node at (7.5,-1.5) {1};
\node at (8.5,-1.5) {1};
% 
% \footnotesize
% \node at (0.5,1.4) {1};
% \node at (1.5,1.4) {2};
% \node at (2.5,1.4) {3};
% \node at (3.5,1.4) {4};
% \node at (4.5,1.4) {5};
% \node at (5.5,1.4) {6};
% \node at (6.5,1.4) {7};
% \node at (7.5,1.4) {8};
% \node at (8.5,1.4) {9};
\end{tikzpicture}
</script>

Using this array, we can calculate the sum of values
in any subtree by first finding out the size of the subtree
and then the values of the corresponding nodes.
For example, the values in the subtree of node $4$
can be found as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (4,1) rectangle (5,0);
\fill[color=lightgray] (4,0) rectangle (5,-1);
\fill[color=lightgray] (4,-1) rectangle (8,-2);
\draw (0,1) grid (9,-2);

\node[left] at (-1,0.5) {node id};
\node[left] at (-1,-0.5) {subtree size};
\node[left] at (-1,-1.5) {node value};

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {2};
\node at (2.5,0.5) {6};
\node at (3.5,0.5) {3};
\node at (4.5,0.5) {4};
\node at (5.5,0.5) {7};
\node at (6.5,0.5) {8};
\node at (7.5,0.5) {9};
\node at (8.5,0.5) {5};

\node at (0.5,-0.5) {9};
\node at (1.5,-0.5) {2};
\node at (2.5,-0.5) {1};
\node at (3.5,-0.5) {1};
\node at (4.5,-0.5) {4};
\node at (5.5,-0.5) {1};
\node at (6.5,-0.5) {1};
\node at (7.5,-0.5) {1};
\node at (8.5,-0.5) {1};

\node at (0.5,-1.5) {2};
\node at (1.5,-1.5) {3};
\node at (2.5,-1.5) {4};
\node at (3.5,-1.5) {5};
\node at (4.5,-1.5) {3};
\node at (5.5,-1.5) {4};
\node at (6.5,-1.5) {3};
\node at (7.5,-1.5) {1};
\node at (8.5,-1.5) {1};
% 
% \footnotesize
% \node at (0.5,1.4) {1};
% \node at (1.5,1.4) {2};
% \node at (2.5,1.4) {3};
% \node at (3.5,1.4) {4};
% \node at (4.5,1.4) {5};
% \node at (5.5,1.4) {6};
% \node at (6.5,1.4) {7};
% \node at (7.5,1.4) {8};
% \node at (8.5,1.4) {9};
\end{tikzpicture}
</script>

To answer the queries efficiently,
it suffices to store the values of the
nodes in a binary indexed or segment tree.
After this, we can both update a value
and calculate the sum of values in $O(\log n)$ time.
