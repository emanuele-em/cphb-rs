# Square root algorithms

A **square root algorithm** is an algorithm
that has a square root in its time complexity.
A square root can be seen as a ''poor man's logarithm'':
the complexity $O(\sqrt n)$ is better than $O(n)$
but worse than $O(\log n)$.
In any case, many square root algorithms are fast and usable in practice.

As an example, consider the problem of
creating a data structure that supports
two operations on an array:
modifying an element at a given position
and calculating the sum of elements in the given range.
We have previously solved the problem using
binary indexed and segment trees,
that support both operations in $O(\log n)$ time.
However, now we will solve the problem
in another way using a square root structure
that allows us to modify elements in $O(1)$ time
and calculate sums in $O(\sqrt n)$ time.

The idea is to divide the array into _blocks_
of size $\sqrt n$ so that each block contains
the sum of elements inside the block.
For example, an array of 16 elements will be
divided into blocks of 4 elements as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (16,1);

\draw (0,1) rectangle (4,2);
\draw (4,1) rectangle (8,2);
\draw (8,1) rectangle (12,2);
\draw (12,1) rectangle (16,2);

\node at (0.5, 0.5) {5};
\node at (1.5, 0.5) {8};
\node at (2.5, 0.5) {6};
\node at (3.5, 0.5) {3};
\node at (4.5, 0.5) {2};
\node at (5.5, 0.5) {7};
\node at (6.5, 0.5) {2};
\node at (7.5, 0.5) {6};
\node at (8.5, 0.5) {7};
\node at (9.5, 0.5) {1};
\node at (10.5, 0.5) {7};
\node at (11.5, 0.5) {5};
\node at (12.5, 0.5) {6};
\node at (13.5, 0.5) {2};
\node at (14.5, 0.5) {3};
\node at (15.5, 0.5) {2};

\node at (2, 1.5) {21};
\node at (6, 1.5) {17};
\node at (10, 1.5) {20};
\node at (14, 1.5) {13};

\end{tikzpicture}
</script>

In this structure,
it is easy to modify array elements,
because it is only needed to update
the sum of a single block
after each modification,
which can be done in $O(1)$ time.
For example, the following picture shows
how the value of an element and
the sum of the corresponding block change:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (5,0) rectangle (6,1);
\draw (0,0) grid (16,1);

\fill[color=lightgray] (4,1) rectangle (8,2);
\draw (0,1) rectangle (4,2);
\draw (4,1) rectangle (8,2);
\draw (8,1) rectangle (12,2);
\draw (12,1) rectangle (16,2);

\node at (0.5, 0.5) {5};
\node at (1.5, 0.5) {8};
\node at (2.5, 0.5) {6};
\node at (3.5, 0.5) {3};
\node at (4.5, 0.5) {2};
\node at (5.5, 0.5) {5};
\node at (6.5, 0.5) {2};
\node at (7.5, 0.5) {6};
\node at (8.5, 0.5) {7};
\node at (9.5, 0.5) {1};
\node at (10.5, 0.5) {7};
\node at (11.5, 0.5) {5};
\node at (12.5, 0.5) {6};
\node at (13.5, 0.5) {2};
\node at (14.5, 0.5) {3};
\node at (15.5, 0.5) {2};

\node at (2, 1.5) {21};
\node at (6, 1.5) {15};
\node at (10, 1.5) {20};
\node at (14, 1.5) {13};

\end{tikzpicture}
</script>

Then, to calculate the sum of elements in a range,
we divide the range into three parts such that 
the sum consists of values of single elements
and sums of blocks between them:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (3,0) rectangle (4,1);
\fill[color=lightgray] (12,0) rectangle (13,1);
\fill[color=lightgray] (13,0) rectangle (14,1);
\draw (0,0) grid (16,1);

\fill[color=lightgray] (4,1) rectangle (8,2);
\fill[color=lightgray] (8,1) rectangle (12,2);
\draw (0,1) rectangle (4,2);
\draw (4,1) rectangle (8,2);
\draw (8,1) rectangle (12,2);
\draw (12,1) rectangle (16,2);

\node at (0.5, 0.5) {5};
\node at (1.5, 0.5) {8};
\node at (2.5, 0.5) {6};
\node at (3.5, 0.5) {3};
\node at (4.5, 0.5) {2};
\node at (5.5, 0.5) {5};
\node at (6.5, 0.5) {2};
\node at (7.5, 0.5) {6};
\node at (8.5, 0.5) {7};
\node at (9.5, 0.5) {1};
\node at (10.5, 0.5) {7};
\node at (11.5, 0.5) {5};
\node at (12.5, 0.5) {6};
\node at (13.5, 0.5) {2};
\node at (14.5, 0.5) {3};
\node at (15.5, 0.5) {2};

\node at (2, 1.5) {21};
\node at (6, 1.5) {15};
\node at (10, 1.5) {20};
\node at (14, 1.5) {13};

\draw [decoration={brace}, decorate, line width=0.5mm] (14,-0.25) -- (3,-0.25);

\end{tikzpicture}
</script>

Since the number of single elements is $O(\sqrt n)$
and the number of blocks is also $O(\sqrt n)$,
the sum query takes $O(\sqrt n)$ time.
The purpose of the block size $\sqrt n$ is
that it _balances_ two things:
the array is divided into $\sqrt n$ blocks,
each of which contains $\sqrt n$ elements.

In practice, it is not necessary to use the
exact value of $\sqrt n$ as a parameter,
and instead we may use parameters $k$ and $n/k$ where $k$ is
different from $\sqrt n$.
The optimal parameter depends on the problem and input.
For example, if an algorithm often goes
through the blocks but rarely inspects
single elements inside the blocks,
it may be a good idea to divide the array into
$k < \sqrt n$ blocks, each of which contains $n/k > \sqrt n$
elements.
