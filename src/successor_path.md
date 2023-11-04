# Successor paths

For the rest of the chapter,
we will focus on **successor graphs**.
In those graphs,
the outdegree of each node is 1, i.e.,
exactly one edge starts at each node.
A successor graph consists of one or more
components, each of which contains
one cycle and some paths that lead to it.

Successor graphs are sometimes called
**functional graphs**.
The reason for this is that any successor graph
corresponds to a function that defines
the edges of the graph.
The parameter for the function is a node of the graph,
and the function gives the successor of that node.

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | - | - | - | - | - | - | - | - | - |
| `succ(x)` | 3 | 5 | 7 | 6 | 2 | 2 | 1 | 6 | 3 |

defines the following graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,0) {1};
\node[draw, circle] (2) at (2,0) {2};
\node[draw, circle] (3) at (-2,0) {3};
\node[draw, circle] (4) at (1,-3) {4};
\node[draw, circle] (5) at (4,0) {5};
\node[draw, circle] (6) at (2,-1.5) {6};
\node[draw, circle] (7) at (-2,-1.5) {7};
\node[draw, circle] (8) at (3,-3) {8};
\node[draw, circle] (9) at (-4,0) {9};

\path[draw,thick,->] (1) -- (3);
\path[draw,thick,->] (2)  edge [bend left=40] (5);
\path[draw,thick,->] (3) -- (7);
\path[draw,thick,->] (4) -- (6);
\path[draw,thick,->] (5)  edge [bend left=40] (2);
\path[draw,thick,->] (6) -- (2);
\path[draw,thick,->] (7) -- (1);
\path[draw,thick,->] (8) -- (6);
\path[draw,thick,->] (9) -- (3);
\end{tikzpicture}
</script>

Since each node of a successor graph has a
unique successor, we can also define a function `succ(x,k)`
that gives the node that we will reach if
we begin at node $x$ and walk $k$ steps forward.
For example, in the above graph `succ(4,6)=2`,
because we will reach node 2 by walking 6 steps from node 4:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,0) {4};
\node[draw, circle] (2) at (1.5,0) {6};
\node[draw, circle] (3) at (3,0) {2};
\node[draw, circle] (4) at (4.5,0) {5};
\node[draw, circle] (5) at (6,0) {2};
\node[draw, circle] (6) at (7.5,0) {5};
\node[draw, circle] (7) at (9,0) {2};

\path[draw,thick,->] (1) -- (2);
\path[draw,thick,->] (2) -- (3);
\path[draw,thick,->] (3) -- (4);
\path[draw,thick,->] (4) -- (5);
\path[draw,thick,->] (5) -- (6);
\path[draw,thick,->] (6) -- (7);
\end{tikzpicture}
</script>

A straightforward way to calculate a value of `succ(x,k)`
is to start at node $x$ and walk $k$ steps forward, which takes $O(k)$ time.
However, using preprocessing, any value of `succ(x,k)`
can be calculated in only $O(\log k)$ time.

The idea is to precalculate all values of `succ(x,k)` where
$k$ is a power of two and at most $u$, where $u$ is
the maximum number of steps we will ever walk.
This can be efficiently done, because
we can use the following recursion:

\\[
\\begin{equation*}
    \\texttt{succ}(x,k) = \\begin{cases}
               \\texttt{succ}(x)              & k = 1\\\\
               \\texttt{succ}(\\texttt{succ}(x,k/2),k/2)   & k > 1\\\\
           \\end{cases}
\\end{equation*}
\\]

Precalculating the values takes $O(n \log u)$ time,
because $O(\log u)$ values are calculated for each node.
In the above graph, the first values are as follows:

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | - | - | - | - | - | - | - | - | - |
| `succ(x,1)` | 3 | 5 | 7 | 6 | 2 | 2 | 1 | 6 | 3 |
| `succ(x,2)` | 7 | 2 | 1 | 2 | 5 | 5 | 3 | 2 | 7 |
| `succ(x,4)` | 3 | 2 | 7 | 2 | 5 | 5 | 1 | 2 | 3 |
| `succ(x,8)` | 7 | 2 | 1 | 2 | 5 | 5 | 3 | 2 | 7 |

After this, any value of `succ(x,k)` can be calculated
by presenting the number of steps $k$ as a sum of powers of two.
For example, if we want to calculate the value of `succ(x,11)`,
we first form the representation $11=8+2+1$.
Using that,

\\[
\\texttt{succ}(x,11)=\\texttt{succ}(\\texttt{succ}(\\texttt{succ}(x,8),2),1)
\\]

For example, in the previous graph

\\[
\\texttt{succ}(4,11)=\\texttt{succ}(\\texttt{succ}(\\texttt{succ}(4,8),2),1)=5
\\]

Such a representation always consists of
$O(\log k)$ parts, so calculating a value of `succ(x,k)`
takes $O(\log k)$ time.
