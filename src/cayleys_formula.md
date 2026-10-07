# Cayley's formula

**Cayley's formula**
states that
there are $n^{n-2}$ labeled trees
that contain $n$ nodes.
The nodes are labeled $1,2,\ldots,n$,
and two trees are different
if either their structure or
labeling is different.

For example, when $n=4$, the number of labeled
trees is $4^{4-2}=16$:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.8]
\footnotesize

\path[draw,thick,-] (0,0) -- (0-1.25,0-1.5);
\path[draw,thick,-] (0,0) -- (0,0-1.5);
\path[draw,thick,-] (0,0) -- (0+1.25,0-1.5);
\node[draw, circle, fill=white] at (0,0) {1};
\node[draw, circle, fill=white] at (0-1.25,0-1.5) {2};
\node[draw, circle, fill=white] at (0,0-1.5) {3};
\node[draw, circle, fill=white] at (0+1.25,0-1.5) {4};

\path[draw,thick,-] (4,0) -- (4-1.25,0-1.5);
\path[draw,thick,-] (4,0) -- (4,0-1.5);
\path[draw,thick,-] (4,0) -- (4+1.25,0-1.5);
\node[draw, circle, fill=white] at (4,0) {2};
\node[draw, circle, fill=white] at (4-1.25,0-1.5) {1};
\node[draw, circle, fill=white] at (4,0-1.5) {3};
\node[draw, circle, fill=white] at (4+1.25,0-1.5) {4};

\path[draw,thick,-] (8,0) -- (8-1.25,0-1.5);
\path[draw,thick,-] (8,0) -- (8,0-1.5);
\path[draw,thick,-] (8,0) -- (8+1.25,0-1.5);
\node[draw, circle, fill=white] at (8,0) {3};
\node[draw, circle, fill=white] at (8-1.25,0-1.5) {1};
\node[draw, circle, fill=white] at (8,0-1.5) {2};
\node[draw, circle, fill=white] at (8+1.25,0-1.5) {4};

\path[draw,thick,-] (12,0) -- (12-1.25,0-1.5);
\path[draw,thick,-] (12,0) -- (12,0-1.5);
\path[draw,thick,-] (12,0) -- (12+1.25,0-1.5);
\node[draw, circle, fill=white] at (12,0) {4};
\node[draw, circle, fill=white] at (12-1.25,0-1.5) {1};
\node[draw, circle, fill=white] at (12,0-1.5) {2};
\node[draw, circle, fill=white] at (12+1.25,0-1.5) {3};

\path[draw,thick,-] (0,-3) -- (0+1,-3);
\path[draw,thick,-] (0+1,-3) -- (0+2,-3);
\path[draw,thick,-] (0+2,-3) -- (0+3,-3);
\node[draw, circle, fill=white] at (0,-3) {1};
\node[draw, circle, fill=white] at (0+1,-3) {2};
\node[draw, circle, fill=white] at (0+2,-3) {3};
\node[draw, circle, fill=white] at (0+3,-3) {4};

\path[draw,thick,-] (4.5,-3) -- (4.5+1,-3);
\path[draw,thick,-] (4.5+1,-3) -- (4.5+2,-3);
\path[draw,thick,-] (4.5+2,-3) -- (4.5+3,-3);
\node[draw, circle, fill=white] at (4.5,-3) {1};
\node[draw, circle, fill=white] at (4.5+1,-3) {2};
\node[draw, circle, fill=white] at (4.5+2,-3) {4};
\node[draw, circle, fill=white] at (4.5+3,-3) {3};

\path[draw,thick,-] (9,-3) -- (9+1,-3);
\path[draw,thick,-] (9+1,-3) -- (9+2,-3);
\path[draw,thick,-] (9+2,-3) -- (9+3,-3);
\node[draw, circle, fill=white] at (9,-3) {1};
\node[draw, circle, fill=white] at (9+1,-3) {3};
\node[draw, circle, fill=white] at (9+2,-3) {2};
\node[draw, circle, fill=white] at (9+3,-3) {4};

\path[draw,thick,-] (0,-4.5) -- (0+1,-4.5);
\path[draw,thick,-] (0+1,-4.5) -- (0+2,-4.5);
\path[draw,thick,-] (0+2,-4.5) -- (0+3,-4.5);
\node[draw, circle, fill=white] at (0,-4.5) {1};
\node[draw, circle, fill=white] at (0+1,-4.5) {3};
\node[draw, circle, fill=white] at (0+2,-4.5) {4};
\node[draw, circle, fill=white] at (0+3,-4.5) {2};

\path[draw,thick,-] (4.5,-4.5) -- (4.5+1,-4.5);
\path[draw,thick,-] (4.5+1,-4.5) -- (4.5+2,-4.5);
\path[draw,thick,-] (4.5+2,-4.5) -- (4.5+3,-4.5);
\node[draw, circle, fill=white] at (4.5,-4.5) {1};
\node[draw, circle, fill=white] at (4.5+1,-4.5) {4};
\node[draw, circle, fill=white] at (4.5+2,-4.5) {2};
\node[draw, circle, fill=white] at (4.5+3,-4.5) {3};

\path[draw,thick,-] (9,-4.5) -- (9+1,-4.5);
\path[draw,thick,-] (9+1,-4.5) -- (9+2,-4.5);
\path[draw,thick,-] (9+2,-4.5) -- (9+3,-4.5);
\node[draw, circle, fill=white] at (9,-4.5) {1};
\node[draw, circle, fill=white] at (9+1,-4.5) {4};
\node[draw, circle, fill=white] at (9+2,-4.5) {3};
\node[draw, circle, fill=white] at (9+3,-4.5) {2};

\path[draw,thick,-] (0,-6) -- (0+1,-6);
\path[draw,thick,-] (0+1,-6) -- (0+2,-6);
\path[draw,thick,-] (0+2,-6) -- (0+3,-6);
\node[draw, circle, fill=white] at (0,-6) {2};
\node[draw, circle, fill=white] at (0+1,-6) {1};
\node[draw, circle, fill=white] at (0+2,-6) {3};
\node[draw, circle, fill=white] at (0+3,-6) {4};

\path[draw,thick,-] (4.5,-6) -- (4.5+1,-6);
\path[draw,thick,-] (4.5+1,-6) -- (4.5+2,-6);
\path[draw,thick,-] (4.5+2,-6) -- (4.5+3,-6);
\node[draw, circle, fill=white] at (4.5,-6) {2};
\node[draw, circle, fill=white] at (4.5+1,-6) {1};
\node[draw, circle, fill=white] at (4.5+2,-6) {4};
\node[draw, circle, fill=white] at (4.5+3,-6) {3};

\path[draw,thick,-] (9,-6) -- (9+1,-6);
\path[draw,thick,-] (9+1,-6) -- (9+2,-6);
\path[draw,thick,-] (9+2,-6) -- (9+3,-6);
\node[draw, circle, fill=white] at (9,-6) {2};
\node[draw, circle, fill=white] at (9+1,-6) {3};
\node[draw, circle, fill=white] at (9+2,-6) {1};
\node[draw, circle, fill=white] at (9+3,-6) {4};

\path[draw,thick,-] (0,-7.5) -- (0+1,-7.5);
\path[draw,thick,-] (0+1,-7.5) -- (0+2,-7.5);
\path[draw,thick,-] (0+2,-7.5) -- (0+3,-7.5);
\node[draw, circle, fill=white] at (0,-7.5) {2};
\node[draw, circle, fill=white] at (0+1,-7.5) {4};
\node[draw, circle, fill=white] at (0+2,-7.5) {1};
\node[draw, circle, fill=white] at (0+3,-7.5) {3};

\path[draw,thick,-] (4.5,-7.5) -- (4.5+1,-7.5);
\path[draw,thick,-] (4.5+1,-7.5) -- (4.5+2,-7.5);
\path[draw,thick,-] (4.5+2,-7.5) -- (4.5+3,-7.5);
\node[draw, circle, fill=white] at (4.5,-7.5) {3};
\node[draw, circle, fill=white] at (4.5+1,-7.5) {1};
\node[draw, circle, fill=white] at (4.5+2,-7.5) {2};
\node[draw, circle, fill=white] at (4.5+3,-7.5) {4};

\path[draw,thick,-] (9,-7.5) -- (9+1,-7.5);
\path[draw,thick,-] (9+1,-7.5) -- (9+2,-7.5);
\path[draw,thick,-] (9+2,-7.5) -- (9+3,-7.5);
\node[draw, circle, fill=white] at (9,-7.5) {3};
\node[draw, circle, fill=white] at (9+1,-7.5) {2};
\node[draw, circle, fill=white] at (9+2,-7.5) {1};
\node[draw, circle, fill=white] at (9+3,-7.5) {4};

\end{tikzpicture}
</script>

Next we will see how Cayley's formula can
be derived using Prüfer codes.

## Prüfer code

A **Prüfer code**
is a sequence of
$n-2$ numbers that describes a labeled tree.
The code is constructed by following a process
that removes $n-2$ leaves from the tree.
At each step, the leaf with the smallest label is removed,
and the label of its only neighbor is added to the code.

For example, let us calculate the Prüfer code
of the following graph:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (2,3) {$1$};
\node[draw, circle] (2) at (4,3) {$2$};
\node[draw, circle] (3) at (2,1) {$3$};
\node[draw, circle] (4) at (4,1) {$4$};
\node[draw, circle] (5) at (5.5,2) {$5$};

\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (2) -- (5);
\end{tikzpicture}
</script>

First we remove node 1 and add node 4 to the code:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
%\node[draw, circle] (1) at (2,3) {$1$};
\node[draw, circle] (2) at (4,3) {$2$};
\node[draw, circle] (3) at (2,1) {$3$};
\node[draw, circle] (4) at (4,1) {$4$};
\node[draw, circle] (5) at (5.5,2) {$5$};

%\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (2) -- (5);
\end{tikzpicture}
</script>

Then we remove node 3 and add node 4 to the code:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
%\node[draw, circle] (1) at (2,3) {$1$};
\node[draw, circle] (2) at (4,3) {$2$};
%\node[draw, circle] (3) at (2,1) {$3$};
\node[draw, circle] (4) at (4,1) {$4$};
\node[draw, circle] (5) at (5.5,2) {$5$};

%\path[draw,thick,-] (1) -- (4);
%\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (2) -- (5);
\end{tikzpicture}
</script>

Finally we remove node 4 and add node 2 to the code:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
%\node[draw, circle] (1) at (2,3) {$1$};
\node[draw, circle] (2) at (4,3) {$2$};
%\node[draw, circle] (3) at (2,1) {$3$};
%\node[draw, circle] (4) at (4,1) {$4$};
\node[draw, circle] (5) at (5.5,2) {$5$};

%\path[draw,thick,-] (1) -- (4);
%\path[draw,thick,-] (3) -- (4);
%\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (2) -- (5);
\end{tikzpicture}
</script>

Thus, the Prüfer code of the graph is $[4,4,2]$.

We can construct a Prüfer code for any tree,
and more importantly,
the original tree can be reconstructed
from a Prüfer code.
Hence, the number of labeled trees
of $n$ nodes equals
$n^{n-2}$, the number of Prüfer codes
of size $n$.
