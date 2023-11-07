# Finding ancestors

The $k$th **ancestor** of a node $x$ in a rooted tree
is the node that we will reach if we move $k$
levels up from $x$.
Let `ancestor}(x,k)` denote the $k$th ancestor of a node $x$
(or $0$ if there is no such an ancestor).
For example, in the following tree,

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (2,1) {2};
\node[draw, circle] (3) at (-2,1) {4};
\node[draw, circle] (4) at (0,1) {5};
\node[draw, circle] (5) at (2,-1) {6};
\node[draw, circle] (6) at (-3,-1) {3};
\node[draw, circle] (7) at (-1,-1) {7};
\node[draw, circle] (8) at (-1,-3) {8};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);
\path[draw,thick,-] (7) -- (8);

\path[draw=red,thick,->,line width=2pt] (8) edge [bend left] (3);
\path[draw=red,thick,->,line width=2pt] (2) edge [bend right] (1);
\end{tikzpicture}
</script>

An easy way to calculate any value of `ancestor(x,k)`
is to perform a sequence of $k$ moves in the tree.
However, the time complexity of this method
is $O(k)$, which may be slow, because a tree of $n$
nodes may have a chain of $n$ nodes.

Fortunately, using a technique similar to that
used in Chapter 16.3, any value of `ancestor(x,k)`
can be efficiently calculated in $O(\log k)$ time
after preprocessing.
The idea is to precalculate all values `ancestor(x,k)`
where $k \le n$ is a power of two.
For example, the values for the above tree
are as follows:

| x | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| - | - | - | - | - | - | - | - | - |
| `ancestor(x,1)` | 0 | 1 | 4 | 1 | 1 | 2 | 4 | 7 |
| `ancestor(x,2)` | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 4 |
| `ancestor(x,4)` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

The preprocessing takes $O(n \log n)$ time,
because $O(\log n)$ values are calculated for each node.
After this, any value of `ancestor(x,k)` can be calculated
in $O(\log k)$ time by representing $k$
as a sum where each term is a power of two.
