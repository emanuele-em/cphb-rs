# Graphs and matrices

## Counting paths

The powers of an adjacency matrix of a graph
have an interesting property.
When $V$ is an adjacency matrix of an unweighted graph,
the matrix $V^n$ contains the numbers of paths of
$n$ edges between the nodes in the graph.

For example, for the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {$1$};
\node[draw, circle] (2) at (1,1) {$4$};
\node[draw, circle] (3) at (3,3) {$2$};
\node[draw, circle] (4) at (5,3) {$3$};
\node[draw, circle] (5) at (3,1) {$5$};
\node[draw, circle] (6) at (5,1) {$6$};

\path[draw,thick,->,>=latex] (1) -- (2);
\path[draw,thick,->,>=latex] (2) -- (3);
\path[draw,thick,->,>=latex] (3) -- (1);
\path[draw,thick,->,>=latex] (4) -- (3);
\path[draw,thick,->,>=latex] (3) -- (5);
\path[draw,thick,->,>=latex] (3) -- (6);
\path[draw,thick,->,>=latex] (6) -- (4);
\path[draw,thick,->,>=latex] (6) -- (5);
\end{tikzpicture}
</script>

the adjacency matrix is
\\[
V= \\begin{bmatrix}
  0 & 0 & 0 & 1 & 0 & 0 \\\\
  1 & 0 & 0 & 0 & 1 & 1 \\\\
  0 & 1 & 0 & 0 & 0 & 0 \\\\
  0 & 1 & 0 & 0 & 0 & 0 \\\\
  0 & 0 & 0 & 0 & 0 & 0 \\\\
  0 & 0 & 1 & 0 & 1 & 0 \\\\
 \\end{bmatrix}.
\\]
Now, for example, the matrix
\\[
V^4= \\begin{bmatrix}
  0 & 0 & 1 & 1 & 1 & 0 \\\\
  2 & 0 & 0 & 0 & 2 & 2 \\\\
  0 & 2 & 0 & 0 & 0 & 0 \\\\
  0 & 2 & 0 & 0 & 0 & 0 \\\\
  0 & 0 & 0 & 0 & 0 & 0 \\\\
  0 & 0 & 1 & 1 & 1 & 0 \\\\
 \\end{bmatrix}
\\]
contains the numbers of paths of 4 edges
between the nodes.
For example, $V^4[2,5]=2$,
because there are two paths of 4 edges
from node 2 to node 5:
$2 \rightarrow 1 \rightarrow 4 \rightarrow 2 \rightarrow 5$
and 
$2 \rightarrow 6 \rightarrow 3 \rightarrow 2 \rightarrow 5$.

## Shortest paths

Using a similar idea in a weighted graph,
we can calculate for each pair of nodes the minimum
length of a path
between them that contains exactly $n$ edges.
To calculate this, we have to define matrix multiplication
in a new way, so that we do not calculate the numbers
of paths but minimize the lengths of paths.

As an example, consider the following graph:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {$1$};
\node[draw, circle] (2) at (1,1) {$4$};
\node[draw, circle] (3) at (3,3) {$2$};
\node[draw, circle] (4) at (5,3) {$3$};
\node[draw, circle] (5) at (3,1) {$5$};
\node[draw, circle] (6) at (5,1) {$6$};

\path[draw,thick,->,>=latex] (1) -- node[font=\small,label=left:4] {} (2);
\path[draw,thick,->,>=latex] (2) -- node[font=\small,label=left:1] {} (3);
\path[draw,thick,->,>=latex] (3) -- node[font=\small,label=north:2] {} (1);
\path[draw,thick,->,>=latex] (4) -- node[font=\small,label=north:4] {} (3);
\path[draw,thick,->,>=latex] (3) -- node[font=\small,label=left:1] {} (5);
\path[draw,thick,->,>=latex] (3) -- node[font=\small,label=left:2] {} (6);
\path[draw,thick,->,>=latex] (6) -- node[font=\small,label=right:3] {} (4);
\path[draw,thick,->,>=latex] (6) -- node[font=\small,label=below:2] {} (5);
\end{tikzpicture}
</script>

Let us construct an adjacency matrix where
$\infty$ means that an edge does not exist,
and other values correspond to edge weights.
The matrix is
\\[
V= \\begin{bmatrix}
  \\infty & \\infty & \\infty & 4 & \\infty & \\infty \\\\
  2 & \\infty & \\infty & \\infty & 1 & 2 \\\\
  \\infty & 4 & \\infty & \\infty & \\infty & \\infty \\\\
  \\infty & 1 & \\infty & \\infty & \\infty & \\infty \\\\
  \\infty & \\infty & \\infty & \\infty & \\infty & \\infty \\\\
  \\infty & \\infty & 3 & \\infty & 2 & \\infty \\\\
 \\end{bmatrix}.
\\]

Instead of the formula
\\[
AB[i,j] = \\sum_{k=1}^n A[i,k] \\cdot B[k,j]
\\]
we now use the formula
\\[
AB[i,j] = \\min_{k=1}^n A[i,k] + B[k,j]
\\]
for matrix multiplication, so we calculate
a minimum instead of a sum,
and a sum of elements instead of a product.
After this modification,
matrix powers correspond to
shortest paths in the graph.

For example, as
\\[
V^4= \\begin{bmatrix}
  \\infty & \\infty & 10 & 11 & 9 & \\infty \\\\
  9 & \\infty & \\infty & \\infty & 8 & 9 \\\\
  \\infty & 11 & \\infty & \\infty & \\infty & \\infty \\\\
  \\infty & 8 & \\infty & \\infty & \\infty & \\infty \\\\
  \\infty & \\infty & \\infty & \\infty & \\infty & \\infty \\\\
  \\infty & \\infty & 12 & 13 & 11 & \\infty \\\\
 \\end{bmatrix},
\\]
we can conclude that the minimum length of a path
of 4 edges
from node 2 to node 5 is 8.
Such a path is
$2 \rightarrow 1 \rightarrow 4 \rightarrow 2 \rightarrow 5$.

## Kirchhoff's theorem

**Kirchhoff's theorem**
provides a way
to calculate the number of spanning trees
of a graph as a determinant of a special matrix.
For example, the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {$1$};
\node[draw, circle] (2) at (3,3) {$2$};
\node[draw, circle] (3) at (1,1) {$3$};
\node[draw, circle] (4) at (3,1) {$4$};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (1) -- (4);
\end{tikzpicture}
</script>

has three spanning trees:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1a) at (1,3) {$1$};
\node[draw, circle] (2a) at (3,3) {$2$};
\node[draw, circle] (3a) at (1,1) {$3$};
\node[draw, circle] (4a) at (3,1) {$4$};

\path[draw,thick,-] (1a) -- (2a);
%\path[draw,thick,-] (1a) -- (3a);
\path[draw,thick,-] (3a) -- (4a);
\path[draw,thick,-] (1a) -- (4a);

\node[draw, circle] (1b) at (1+4,3) {$1$};
\node[draw, circle] (2b) at (3+4,3) {$2$};
\node[draw, circle] (3b) at (1+4,1) {$3$};
\node[draw, circle] (4b) at (3+4,1) {$4$};

\path[draw,thick,-] (1b) -- (2b);
\path[draw,thick,-] (1b) -- (3b);
%\path[draw,thick,-] (3b) -- (4b);
\path[draw,thick,-] (1b) -- (4b);

\node[draw, circle] (1c) at (1+8,3) {$1$};
\node[draw, circle] (2c) at (3+8,3) {$2$};
\node[draw, circle] (3c) at (1+8,1) {$3$};
\node[draw, circle] (4c) at (3+8,1) {$4$};

\path[draw,thick,-] (1c) -- (2c);
\path[draw,thick,-] (1c) -- (3c);
\path[draw,thick,-] (3c) -- (4c);
%\path[draw,thick,-] (1c) -- (4c);
\end{tikzpicture}
</script>

To calculate the number of spanning trees,
we construct a **Laplacean matrix** $L$,
where $L[i,i]$ is the degree of node $i$
and $L[i,j]=-1$ if there is an edge between
nodes $i$ and $j$, and otherwise $L[i,j]=0$.
The Laplacean matrix for the above graph is as follows:
\\[
L= \\begin{bmatrix}
  3 & -1 & -1 & -1 \\\\
  -1 & 1 & 0 & 0 \\\\
  -1 & 0 & 2 & -1 \\\\
  -1 & 0 & -1 & 2 \\\\
 \\end{bmatrix}
\\]

It can be shown that
the number of spanning trees equals
the determinant of a matrix that is obtained
when we remove any row and any column from $L$.
For example, if we remove the first row
and column, the result is

\\[
\\det(
\\begin{bmatrix}
  1 & 0 & 0 \\\\
  0 & 2 & -1 \\\\
  0 & -1 & 2 \\\\
 \\end{bmatrix}
) =3.
\\]
The determinant is always the same,
regardless of which row and column we remove from $L$.

Note that Cayley's formula in Chapter 22.5 is
a special case of Kirchhoff's theorem,
because in a complete graph of $n$ nodes

\\[
\\det(
\\begin{bmatrix}
  n-1 & -1 & \\cdots & -1 \\\\
  -1 & n-1 & \\cdots & -1 \\\\
  \\vdots & \\vdots & \\ddots & \\vdots \\\\
  -1 & -1 & \\cdots & n-1 \\\\
 \\end{bmatrix}
) =n^{n-2}.
\\]
