# Knight’s tours

A **knight's tour** is a sequence of moves
of a knight on an $n \times n$ chessboard
following the rules of chess such that the knight
visits each square exactly once.
A knight's tour is called a _closed_ tour
if the knight finally returns to the starting square and
otherwise it is called an _open_ tour.

For example, here is an open knight's tour on a $5 \times 5$ board:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (5,5);
\node at (0.5,4.5) {1};
\node at (1.5,4.5) {4};
\node at (2.5,4.5) {11};
\node at (3.5,4.5) {16};
\node at (4.5,4.5) {25};
\node at (0.5,3.5) {12};
\node at (1.5,3.5) {17};
\node at (2.5,3.5) {2};
\node at (3.5,3.5) {5};
\node at (4.5,3.5) {10};
\node at (0.5,2.5) {3};
\node at (1.5,2.5) {20};
\node at (2.5,2.5) {7};
\node at (3.5,2.5) {24};
\node at (4.5,2.5) {15};
\node at (0.5,1.5) {18};
\node at (1.5,1.5) {13};
\node at (2.5,1.5) {22};
\node at (3.5,1.5) {9};
\node at (4.5,1.5) {6};
\node at (0.5,0.5) {21};
\node at (1.5,0.5) {8};
\node at (2.5,0.5) {19};
\node at (3.5,0.5) {14};
\node at (4.5,0.5) {23};
\end{tikzpicture}
</script>

A knight's tour corresponds to a Hamiltonian path in a graph
whose nodes represent the squares of the board,
and two nodes are connected with an edge if a knight
can move between the squares according to the rules of chess.

A natural way to construct a knight's tour is to use backtracking.
The search can be made more efficient by using
_heuristics_ that attempt to guide the knight so that
a complete tour will be found quickly.

## Warnsdorf's rule

**Warnsdorf's rule** is a simple and effective heuristic
for finding a knight's tour[^1].
Using the rule, it is possible to efficiently construct a tour
even on a large board.
The idea is to always move the knight so that it ends up
in a square where the number of possible moves is as
_small_ as possible.

For example, in the following situation, there are five
possible squares to which the knight can move (squares $a \ldots e$):

___

[^1] This heuristic was proposed in Warnsdorf's book [69] in 1823. There are also polynomial algorithms for finding knight's tours [52], but they are more complicated.
