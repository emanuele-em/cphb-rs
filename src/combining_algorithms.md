# Combining algorithms

In this section we discuss two square root algorithms
that are based on combining two algorithms into one algorithm.
In both cases, we could use either of the algorithms
without the other
and solve the problem in $O(n^2)$ time.
However, by combining the algorithms, the running
time is only $O(n \sqrt n)$.

## Case processing

Suppose that we are given a two-dimensional
grid that contains $n$ cells.
Each cell is assigned a letter,
and our task is to find two cells
with the same letter whose distance is minimum,
where the distance between cells
$(x_1,y_1)$ and $(x_2,y_2)$ is $|x_1-x_2|+|y_1-y_2|$.
For example, consider the following grid:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\node at (0.5,0.5) {A};
\node at (0.5,1.5) {B};
\node at (0.5,2.5) {C};
\node at (0.5,3.5) {A};
\node at (1.5,0.5) {C};
\node at (1.5,1.5) {D};
\node at (1.5,2.5) {E};
\node at (1.5,3.5) {F};
\node at (2.5,0.5) {B};
\node at (2.5,1.5) {A};
\node at (2.5,2.5) {G};
\node at (2.5,3.5) {B};
\node at (3.5,0.5) {D};
\node at (3.5,1.5) {F};
\node at (3.5,2.5) {E};
\node at (3.5,3.5) {A};
\draw (0,0) grid (4,4);
\end{tikzpicture}
</script>

In this case, the minimum distance is 2 between the two 'E' letters.

We can solve the problem by considering each letter separately.
Using this approach, the new problem is to calculate
the minimum distance
between two cells with a _fixed_ letter $c$.
We focus on two algorithms for this:

_Algorithm 1:_ Go through all pairs of cells with letter $c$,
and calculate the minimum distance between such cells.
This will take $O(k^2)$ time where $k$ is the number of cells with letter $c$.

_Algorithm 2:_ Perform a breadth-first search that simultaneously
starts at each cell with letter $c$. The minimum distance between
two cells with letter $c$ will be calculated in $O(n)$ time.

One way to solve the problem is to choose either of the
algorithms and use it for all letters.
If we use Algorithm 1, the running time is $O(n^2)$,
because all cells may contain the same letter,
and in this case $k=n$.
Also if we use Algorithm 2, the running time is $O(n^2)$,
because all cells may have different letters,
and in this case $n$ searches are needed.

However, we can _combine_ the two algorithms and
use different algorithms for different letters
depending on how many times each letter appears in the grid.
Assume that a letter $c$ appears $k$ times.
If $k \le \sqrt n$, we use Algorithm 1, and if $k > \sqrt n$,
we use Algorithm 2.
It turns out that by doing this, the total running time
of the algorithm is only $O(n \sqrt n)$.

First, suppose that we use Algorithm 1 for a letter $c$.
Since $c$ appears at most $\sqrt n$ times in the grid,
we compare each cell with letter $c$ $O(\sqrt n)$ times
with other cells.
Thus, the time used for processing all such cells is $O(n \sqrt n)$.
Then, suppose that we use Algorithm 2 for a letter $c$.
There are at most $\sqrt n$ such letters,
so processing those letters also takes $O(n \sqrt n)$ time.

## Batch processing

Our next problem also deals with
a two-dimensional grid that contains $n$ cells.
Initially, each cell except one is white.
We perform $n-1$ operations, each of which first
calculates the minimum distance from a given white cell
to a black cell, and then paints the white cell black.

For example, consider the following operation:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=black] (1,1) rectangle (2,2);
\fill[color=black] (3,1) rectangle (4,2);
\fill[color=black] (0,3) rectangle (1,4);
\node at (2.5,3.5) {*};
\draw (0,0) grid (4,4);
\end{tikzpicture}
</script>

First, we calculate the minimum distance
from the white cell marked with * to a black cell.
The minimum distance is 2, because we can move
two steps left to a black cell.
Then, we paint the white cell black:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=black] (1,1) rectangle (2,2);
\fill[color=black] (3,1) rectangle (4,2);
\fill[color=black] (0,3) rectangle (1,4);
\fill[color=black] (2,3) rectangle (3,4);
\draw (0,0) grid (4,4);
\end{tikzpicture}
</script>

Consider the following two algorithms:

_Algorithm 1:_ Use breadth-first search
to calculate
for each white cell the distance to the nearest black cell.
This takes $O(n)$ time, and after the search,
we can find the minimum distance from any white cell
to a black cell in $O(1)$ time.

_Algorithm 2:_ Maintain a list of cells that have been
painted black, go through this list at each operation
and then add a new cell to the list.
An operation takes $O(k)$ time where $k$ is the length of the list.

We combine the above algorithms by
dividing the operations into
$O(\sqrt n)$ _batches_, each of which consists
of $O(\sqrt n)$ operations.
At the beginning of each batch,
we perform Algorithm 1.
Then, we use Algorithm 2 to process the operations
in the batch.
We clear the list of Algorithm 2 between
the batches.
At each operation,
the minimum distance to a black cell
is either the distance calculated by Algorithm 1
or the distance calculated by Algorithm 2.

The resulting algorithm works in
$O(n \sqrt n)$ time.
First, Algorithm 1 is performed $O(\sqrt n)$ times,
and each search works in $O(n)$ time.
Second, when using Algorithm 2 in a batch,
the list contains $O(\sqrt n)$ cells
(because we clear the list between the batches)
and each operation takes $O(\sqrt n)$ time.
