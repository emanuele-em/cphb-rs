# Additional techniques

## Index compression

A limitation in data structures that
are built upon an array is that
the elements are indexed using
consecutive integers.
Difficulties arise when large indices
are needed.
For example, if we wish to use the index $10^9$,
the array should contain $10^9$
elements which would require too much memory.

However, we can often bypass this limitation
by using **index compression**,
where the original indices are replaced
with indices $1,2,3,$ etc.
This can be done if we know all the indices
needed during the algorithm beforehand.

The idea is to replace each original index $x$
with $c(x)$ where $c$ is a function that
compresses the indices.
We require that the order of the indices
does not change, so if $a<b$, then $c(a)<c(b)$.
This allows us to conveniently perform queries
even if the indices are compressed.

For example, if the original indices are
$555$, $10^9$ and $8$, the new indices are:

\\[
\\begin{array}{lcl}
c(8) & = & 1 \\\\
c(555) & = & 2 \\\\
c(10^9) & = & 3 \\\\
\\end{array}
\\]

## Range updates

So far, we have implemented data structures
that support range queries and updates
of single values.
Let us now consider an opposite situation,
where we should update ranges and
retrieve single values.
We focus on an operation that increases all
elements in a range \\([a,b]\\) by $x$.

Surprisingly, we can use the data structures
presented in this chapter also in this situation.
To do this, we build a **difference array**
whose values indicate
the differences between consecutive values
in the original array.
Thus, the original array is the
prefix sum array of the
difference array.
For example, consider the following array:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {3};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {1};
\node at (3.5,0.5) {1};
\node at (4.5,0.5) {1};
\node at (5.5,0.5) {5};
\node at (6.5,0.5) {2};
\node at (7.5,0.5) {2};


\footnotesize
\node at (0.5,1.4) {0};
\node at (1.5,1.4) {1};
\node at (2.5,1.4) {2};
\node at (3.5,1.4) {3};
\node at (4.5,1.4) {4};
\node at (5.5,1.4) {5};
\node at (6.5,1.4) {6};
\node at (7.5,1.4) {7};
\end{tikzpicture}
</script>

The difference array for the above array is as follows:
<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {3};
\node at (1.5,0.5) {0};
\node at (2.5,0.5) {-2};
\node at (3.5,0.5) {0};
\node at (4.5,0.5) {0};
\node at (5.5,0.5) {4};
\node at (6.5,0.5) {-3};
\node at (7.5,0.5) {0};


\footnotesize
\node at (0.5,1.4) {0};
\node at (1.5,1.4) {1};
\node at (2.5,1.4) {2};
\node at (3.5,1.4) {3};
\node at (4.5,1.4) {4};
\node at (5.5,1.4) {5};
\node at (6.5,1.4) {6};
\node at (7.5,1.4) {7};
\end{tikzpicture}
</script>

For example, the value 2 at position 6 in the original array
corresponds to the sum $3-2+4-3=2$ in the difference array.

The advantage of the difference array is
that we can update a range
in the original array by changing just
two elements in the difference array.
For example, if we want to 
increase the original array 
values between positions 1 and 4 by 5,
it suffices to increase the
difference array value at position 1 by 5
and decrease the value at position 5 by 5.
The result is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {3};
\node at (1.5,0.5) {5};
\node at (2.5,0.5) {-2};
\node at (3.5,0.5) {0};
\node at (4.5,0.5) {0};
\node at (5.5,0.5) {-1};
\node at (6.5,0.5) {-3};
\node at (7.5,0.5) {0};

\footnotesize
\node at (0.5,1.4) {0};
\node at (1.5,1.4) {1};
\node at (2.5,1.4) {2};
\node at (3.5,1.4) {3};
\node at (4.5,1.4) {4};
\node at (5.5,1.4) {5};
\node at (6.5,1.4) {6};
\node at (7.5,1.4) {7};
\end{tikzpicture}
</script>

More generally, to increase the values
in range \\([a,b]\\) by $x$,
we increase the value at position $a$ by $x$
and decrease the value at position $b+1$ by $x$.
Thus, it is only needed to update single values
and process sum queries,
so we can use a binary indexed tree or a segment tree.

A more difficult problem is to support both
range queries and range updates.
In Chapter 28 we will see that even this is possible.
