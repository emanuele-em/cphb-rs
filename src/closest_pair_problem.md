# Closest pair problem

Given a set of $n$ points, our next problem is
to find two points whose Euclidean distance is minimum.
For example, if the points are

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0)--(12,0)--(12,4)--(0,4)--(0,0);

\draw (1,2) circle [radius=0.1];
\draw (3,1) circle [radius=0.1];
\draw (4,3) circle [radius=0.1];
\draw (5.5,1.5) circle [radius=0.1];
\draw (6,2.5) circle [radius=0.1];
\draw (7,1) circle [radius=0.1];
\draw (9,1.5) circle [radius=0.1];
\draw (10,2) circle [radius=0.1];
\draw (1.5,3.5) circle [radius=0.1];
\draw (1.5,1) circle [radius=0.1];
\draw (2.5,3) circle [radius=0.1];
\draw (4.5,1.5) circle [radius=0.1];
\draw (5.25,0.5) circle [radius=0.1];
\draw (6.5,2) circle [radius=0.1];
\end{tikzpicture}
</script>

we should find the following points:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0)--(12,0)--(12,4)--(0,4)--(0,0);

\draw (1,2) circle [radius=0.1];
\draw (3,1) circle [radius=0.1];
\draw (4,3) circle [radius=0.1];
\draw (5.5,1.5) circle [radius=0.1];
\draw[fill] (6,2.5) circle [radius=0.1];
\draw (7,1) circle [radius=0.1];
\draw (9,1.5) circle [radius=0.1];
\draw (10,2) circle [radius=0.1];
\draw (1.5,3.5) circle [radius=0.1];
\draw (1.5,1) circle [radius=0.1];
\draw (2.5,3) circle [radius=0.1];
\draw (4.5,1.5) circle [radius=0.1];
\draw (5.25,0.5) circle [radius=0.1];
\draw[fill] (6.5,2) circle [radius=0.1];
\end{tikzpicture}
</script>

This is another example of a problem
that can be solved in $O(n \log n)$ time
using a sweep line algorithm[^1].
We go through the points from left to right
and maintain a value $d$: the minimum distance
between two points seen so far.
At each point, we find the nearest point to the left.
If the distance is less than $d$, it is the
new minimum distance and we update
the value of $d$.

If the current point is $(x,y)$
and there is a point to the left
within a distance of less than $d$,
the x coordinate of such a point must
be between $[x-d,x]$ and the y coordinate
must be between $[y-d,y+d]$.
Thus, it suffices to only consider points
that are located in those ranges,
which makes the algorithm efficient.

For example, in the following picture, the
region marked with dashed lines contains
the points that can be within a distance of $d$
from the active point:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0)--(12,0)--(12,4)--(0,4)--(0,0);

\draw (1,2) circle [radius=0.1];
\draw (3,1) circle [radius=0.1];
\draw (4,3) circle [radius=0.1];
\draw (5.5,1.5) circle [radius=0.1];
\draw (6,2.5) circle [radius=0.1];
\draw (7,1) circle [radius=0.1];
\draw (9,1.5) circle [radius=0.1];
\draw (10,2) circle [radius=0.1];
\draw (1.5,3.5) circle [radius=0.1];
\draw (1.5,1) circle [radius=0.1];
\draw (2.5,3) circle [radius=0.1];
\draw (4.5,1.5) circle [radius=0.1];
\draw (5.25,0.5) circle [radius=0.1];
\draw[fill] (6.5,2) circle [radius=0.1];

\draw[dashed] (6.5,0.75)--(6.5,3.25);
\draw[dashed] (5.25,0.75)--(5.25,3.25);
\draw[dashed] (5.25,0.75)--(6.5,0.75);
\draw[dashed] (5.25,3.25)--(6.5,3.25);

\draw [decoration={brace}, decorate, line width=0.3mm] (5.25,3.5) -- (6.5,3.5);
\node at (5.875,4) {$d$};
\draw [decoration={brace}, decorate, line width=0.3mm] (6.75,3.25) -- (6.75,2);
\node at (7.25,2.625) {$d$};
\end{tikzpicture}
</script>

The efficiency of the algorithm is based on the fact
that the region always contains
only $O(1)$ points.
We can go through those points in $O(\log n)$ time
by maintaining a set of points whose x coordinate
is between $[x-d,x]$, in increasing order according
to their y coordinates.

The time complexity of the algorithm is $O(n \log n)$,
because we go through $n$ points and
find for each point the nearest point to the left
in $O(\log n)$ time.

___

[^1]: Besides this approach,
there is also an
$O(n \log n)$ time divide-and-conquer algorithm [64]
that divides the points into two sets and recursively
solves the problem for both sets.
