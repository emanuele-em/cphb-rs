# Sliding window minimum

A **sliding window** is a constant-size subarray
that moves from left to right through the array.
At each window position,
we want to calculate some information
about the elements inside the window.
In this section, we focus on the problem
of maintaining the **sliding window minimum**,
which means that
we should report the smallest value inside each window.

The sliding window minimum can be calculated
using a similar idea that we used to calculate
the nearest smaller elements.
We maintain a queue
where each element is larger than
the previous element,
and the first element
always corresponds to the minimum element inside the window.
After each window move,
we remove elements from the end of the queue
until the last queue element
is smaller than the new window element,
or the queue becomes empty.
We also remove the first queue element
if it is not inside the window anymore.
Finally, we add the new window element
to the end of the queue.

As an example, consider the following array:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {2};
\node at (1.5,0.5) {1};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {5};
\node at (4.5,0.5) {3};
\node at (5.5,0.5) {4};
\node at (6.5,0.5) {1};
\node at (7.5,0.5) {2};
\end{tikzpicture}
</script>

Suppose that the size of the sliding window is 4.
At the first window position, the smallest value is 1:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (0,0) rectangle (4,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {2};
\node at (1.5,0.5) {1};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {5};
\node at (4.5,0.5) {3};
\node at (5.5,0.5) {4};
\node at (6.5,0.5) {1};
\node at (7.5,0.5) {2};

\draw (1.2,0.2-1.2) rectangle (1.8,0.8-1.2);
\draw (2.2,0.2-1.2) rectangle (2.8,0.8-1.2);
\draw (3.2,0.2-1.2) rectangle (3.8,0.8-1.2);

\node at (1.5,0.5-1.2) {1};
\node at (2.5,0.5-1.2) {4};
\node at (3.5,0.5-1.2) {5};

\draw[->,thick] (1.8,0.5-1.2) -- (2.2,0.5-1.2);
\draw[->,thick] (2.8,0.5-1.2) -- (3.2,0.5-1.2);
\end{tikzpicture}
</script>

Then the window moves one step right.
The new element 3 is smaller than the elements
4 and 5 in the queue, so the elements 4 and 5
are removed from the queue
and the element 3 is added to the queue.
The smallest value is still 1.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (1,0) rectangle (5,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {2};
\node at (1.5,0.5) {1};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {5};
\node at (4.5,0.5) {3};
\node at (5.5,0.5) {4};
\node at (6.5,0.5) {1};
\node at (7.5,0.5) {2};

\draw (1.2,0.2-1.2) rectangle (1.8,0.8-1.2);
\draw (4.2,0.2-1.2) rectangle (4.8,0.8-1.2);

\node at (1.5,0.5-1.2) {1};
\node at (4.5,0.5-1.2) {3};

\draw[->,thick] (1.8,0.5-1.2) -- (4.2,0.5-1.2);
\end{tikzpicture}
</script>

After this, the window moves again,
and the smallest element 1
does not belong to the window anymore.
Thus, it is removed from the queue and the smallest
value is now 3. Also the new element 4
is added to the queue.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (2,0) rectangle (6,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {2};
\node at (1.5,0.5) {1};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {5};
\node at (4.5,0.5) {3};
\node at (5.5,0.5) {4};
\node at (6.5,0.5) {1};
\node at (7.5,0.5) {2};

\draw (4.2,0.2-1.2) rectangle (4.8,0.8-1.2);
\draw (5.2,0.2-1.2) rectangle (5.8,0.8-1.2);

\node at (4.5,0.5-1.2) {3};
\node at (5.5,0.5-1.2) {4};

\draw[->,thick] (4.8,0.5-1.2) -- (5.2,0.5-1.2);
\end{tikzpicture}
</script>

The next new element 1 is smaller than all elements
in the queue.
Thus, all elements are removed from the queue
and it will only contain the element 1:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (3,0) rectangle (7,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {2};
\node at (1.5,0.5) {1};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {5};
\node at (4.5,0.5) {3};
\node at (5.5,0.5) {4};
\node at (6.5,0.5) {1};
\node at (7.5,0.5) {2};

\draw (6.2,0.2-1.2) rectangle (6.8,0.8-1.2);

\node at (6.5,0.5-1.2) {1};
\end{tikzpicture}
</script>

Finally the window reaches its last position.
The element 2 is added to the queue,
but the smallest value inside the window
is still 1.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (4,0) rectangle (8,1);
    \draw (0,0) grid (8,1);

    \node at (0.5,0.5) {2};
\node at (1.5,0.5) {1};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {5};
\node at (4.5,0.5) {3};
\node at (5.5,0.5) {4};
\node at (6.5,0.5) {1};
\node at (7.5,0.5) {2};

\draw (6.2,0.2-1.2) rctangle (6.8,0.8-1.2);
\draw (7.2,0.2-1.2) rctangle (7.8,0.8-1.2);

\node at (6.5,0.5-1.2 {1};
\node at (7.5,0.5-1.2 {2};

\draw[->,thick] (6.8,0.5-1.2) -- (7.2,0.5-1.2);
\end{tikzpicture}
</script>

Since each array element
is added to the queue exactly once and
removed from the queue at most once,
the algorithm works in $O(n)$ time.
