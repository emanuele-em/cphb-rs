# Intersection points

Given a set of $n$ line segments, each of them being either
horizontal or vertical, consider the problem of
counting the total number of intersection points.
For example, when the line segments are

<script type="text/tikz">
\begin{tikzpicture}[scale=0.5]
\path[draw,thick,-] (0,2) -- (5,2);
\path[draw,thick,-] (1,4) -- (6,4);
\path[draw,thick,-] (6,3) -- (10,3);
\path[draw,thick,-] (2,1) -- (2,6);
\path[draw,thick,-] (8,2) -- (8,5);
\end{tikzpicture}
</script>

there are three intersection points:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.5]
\path[draw,thick,-] (0,2) -- (5,2);
\path[draw,thick,-] (1,4) -- (6,4);
\path[draw,thick,-] (6,3) -- (10,3);
\path[draw,thick,-] (2,1) -- (2,6);
\path[draw,thick,-] (8,2) -- (8,5);

\draw[fill] (2,2) circle [radius=0.15];
\draw[fill] (2,4) circle [radius=0.15];
\draw[fill] (8,3) circle [radius=0.15];

\end{tikzpicture}
</script>

It is easy to solve the problem in $O(n^2)$ time,
because we can go through all possible pairs of line segments
and check if they intersect.
However, we can solve the problem more efficiently
in $O(n \log n)$ time using a sweep line algorithm
and a range query data structure.

The idea is to process the endpoints of the line
segments from left to right and 
focus on three types of events:
- (1) horizontal segment begins
- (2) horizontal segment ends
- (3) vertical segment

The following events correspond to the example:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.6]
\path[draw,dashed] (0,2) -- (5,2);
\path[draw,dashed] (1,4) -- (6,4);
\path[draw,dashed] (6,3) -- (10,3);
\path[draw,dashed] (2,1) -- (2,6);
\path[draw,dashed] (8,2) -- (8,5);

\node at (0,2) {$1$};
\node at (5,2) {$2$};
\node at (1,4) {$1$};
\node at (6,4) {$2$};
\node at (6,3) {$1$};
\node at (10,3) {$2$};

\node at (2,3.5) {$3$};
\node at (8,3.5) {$3$};
\end{tikzpicture}
</script>

We go through the events from left to right
and use a data structure that maintains a set of
y coordinates where there is an active horizontal segment.
At event 1, we add the y coordinate of the segment
to the set, and at event 2, we remove the
y coordinate from the set.

Intersection points are calculated at event 3.
When there is a vertical segment between points
$y_1$ and $y_2$, we count the number of active
horizontal segments whose y coordinate is between
$y_1$ and $y_2$, and add this number to the total
number of intersection points.

To store y coordinates of horizontal segments,
we can use a binary indexed or segment tree,
possibly with index compression.
When such structures are used, processing each event
takes $O(\log n)$ time, so the total running
time of the algorithm is $O(n \log n)$.
