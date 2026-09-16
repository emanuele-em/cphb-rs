# Sweep line algorithms

Many geometric problems can be solved using
**sweep line** algorithms.
The idea in such algorithms is to represent
an instance of the problem as a set of events that correspond
to points in the plane.
The events are processed in increasing order
according to their x or y coordinates.

As an example, consider the following problem:
There is a company that has $n$ employees,
and we know for each employee their arrival and
leaving times on a certain day.
Our task is to calculate the maximum number of
employees that were in the office at the same time.

The problem can be solved by modeling the situation
so that each employee is assigned two events that
correspond to their arrival and leaving times.
After sorting the events, we go through them
and keep track of the number of people in the office.
For example, the table

| person | arrival time | leaving time |
| :—: | :—: | :—: |
| John | 10 | 15 |
| Maria | 6 | 12 |
| Peter | 14 | 16 |
| Lisa | 5 | 13 |

corresponds to the following events:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.6]
\draw (0,0) rectangle (17,-6.5);
\path[draw,thick,-] (10,-1) -- (15,-1);
\path[draw,thick,-] (6,-2.5) -- (12,-2.5);
\path[draw,thick,-] (14,-4) -- (16,-4);
\path[draw,thick,-] (5,-5.5) -- (13,-5.5);

\draw[fill] (10,-1) circle [radius=0.05];
\draw[fill] (15,-1) circle [radius=0.05];
\draw[fill] (6,-2.5) circle [radius=0.05];
\draw[fill] (12,-2.5) circle [radius=0.05];
\draw[fill] (14,-4) circle [radius=0.05];
\draw[fill] (16,-4) circle [radius=0.05];
\draw[fill] (5,-5.5) circle [radius=0.05];
\draw[fill] (13,-5.5) circle [radius=0.05];

\node at (2,-1) {John};
\node at (2,-2.5) {Maria};
\node at (2,-4) {Peter};
\node at (2,-5.5) {Lisa};
\end{tikzpicture}
</script>

We go through the events from left to right
and maintain a counter.
Always when a person arrives, we increase
the value of the counter by one,
and when a person leaves,
we decrease the value of the counter by one.
The answer to the problem is the maximum
value of the counter during the algorithm.

In the example, the events are processed as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.6]
\path[draw,thick,->] (0.5,0.5) -- (16.5,0.5);
\draw (0,0) rectangle (17,-6.5);
\path[draw,thick,-] (10,-1) -- (15,-1);
\path[draw,thick,-] (6,-2.5) -- (12,-2.5);
\path[draw,thick,-] (14,-4) -- (16,-4);
\path[draw,thick,-] (5,-5.5) -- (13,-5.5);

\draw[fill] (10,-1) circle [radius=0.05];
\draw[fill] (15,-1) circle [radius=0.05];
\draw[fill] (6,-2.5) circle [radius=0.05];
\draw[fill] (12,-2.5) circle [radius=0.05];
\draw[fill] (14,-4) circle [radius=0.05];
\draw[fill] (16,-4) circle [radius=0.05];
\draw[fill] (5,-5.5) circle [radius=0.05];
\draw[fill] (13,-5.5) circle [radius=0.05];

\node at (2,-1) {John};
\node at (2,-2.5) {Maria};
\node at (2,-4) {Peter};
\node at (2,-5.5) {Lisa};

\path[draw,dashed] (10,0)--(10,-6.5);
\path[draw,dashed] (15,0)--(15,-6.5);
\path[draw,dashed] (6,0)--(6,-6.5);
\path[draw,dashed] (12,0)--(12,-6.5);
\path[draw,dashed] (14,0)--(14,-6.5);
\path[draw,dashed] (16,0)--(16,-6.5);
\path[draw,dashed] (5,0)--(5,-6.5);
\path[draw,dashed] (13,0)--(13,-6.5);

\node at (10,-7) {$+$};
\node at (15,-7) {$-$};
\node at (6,-7) {$+$};
\node at (12,-7) {$-$};
\node at (14,-7) {$+$};
\node at (16,-7) {$-$};
\node at (5,-7) {$+$};
\node at (13,-7) {$-$};

\node at (10,-8) {$3$};
\node at (15,-8) {$1$};
\node at (6,-8) {$2$};
\node at (12,-8) {$2$};
\node at (14,-8) {$2$};
\node at (16,-8) {$0$};
\node at (5,-8) {$1$};
\node at (13,-8) {$1$};
\end{tikzpicture}
</script>

The symbols $+$ and $-$ indicate whether the
value of the counter increases or decreases,
and the value of the counter is shown below.
The maximum value of the counter is 3
between John's arrival and Maria's leaving.

The running time of the algorithm is $O(n \log n)$,
because sorting the events takes $O(n \log n)$ time
and the rest of the algorithm takes $O(n)$ time.
