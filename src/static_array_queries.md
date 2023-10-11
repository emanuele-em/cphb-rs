# Static array queries

We first focus on a situation where
the array is _static_, i.e.,
the array values are never updated between the queries.
In this case, it suffices to construct
a static data structure that tells us
the answer for any possible query.

## Sum queries

We can easily process
sum queries on a static array
by constructing a **prefix sum array**.
Each value in the prefix sum array equals
the sum of values in the original array up to that position,
i.e., the value at position $k$ is $sum_q(0,k)$.
The prefix sum array can be constructed in $O(n)$ time.

For example, consider the following array:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (3,0) rectangle (7,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {8};
\node at (4.5,0.5) {6};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {4};
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

The corresponding prefix sum array is as follows:
<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
%\fill[color=lightgray] (3,0) rectangle (7,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {4};
\node at (2.5,0.5) {8};
\node at (3.5,0.5) {16};
\node at (4.5,0.5) {22};
\node at (5.5,0.5) {23};
\node at (6.5,0.5) {27};
\node at (7.5,0.5) {29};


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

Since the prefix sum array contains all values
of $sum_q(0,k)$,
we can calculate any value of
$sum_q(a,b)$ in $O(1)$ time as follows:

\\[
    \\texttt{sum}_q(a,b) = \\texttt{sum}_q(0,b) - \\texttt{sum}_q(0,a-1)
\\]

By defining $sum_q(0,-1)=0$,
the above formula also holds when $a=0$.

For example, consider the range \\([3,6]\\):

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (3,0) rectangle (7,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {8};
\node at (4.5,0.5) {6};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {4};
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

In this case \\( \\texttt{sum}_q(3,6)=8+6+1+4=19 \\).
This sum can be calculated from
two values of the prefix sum array:
<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (2,0) rectangle (3,1);
\fill[color=lightgray] (6,0) rectangle (7,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {4};
\node at (2.5,0.5) {8};
\node at (3.5,0.5) {16};
\node at (4.5,0.5) {22};
\node at (5.5,0.5) {23};
\node at (6.5,0.5) {27};
\node at (7.5,0.5) {29};

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

Thus, \\( \\texttt{sum}_q(3,6)=\\texttt{sum}_q(0,6)-\\texttt{sum}_q(0,2)=27-8=19 \\)

It is also possible to generalize this idea
to higher dimensions.
For example, we can construct a two-dimensional
prefix sum array that can be used to calculate
the sum of any rectangular subarray in $O(1)$ time.
Each sum in such an array corresponds to
a subarray
that begins at the upper-left corner of the array.

The following picture illustrates the idea:
<script type="text/tikz">
\begin{tikzpicture}[scale=0.54]
\draw[fill=lightgray] (3,2) rectangle (7,5);
\draw (0,0) grid (10,7);
\node[anchor=center] at (6.5, 2.5) {A};
\node[anchor=center] at (2.5, 2.5) {B};
\node[anchor=center] at (6.5, 5.5) {C};
\node[anchor=center] at (2.5, 5.5) {D};
\end{tikzpicture}
</script>

The sum of the gray subarray can be calculated
using the formula
\\[
    S(A) - S(B) - S(C) + S(D),
\\]
where $S(X)$ denotes the sum of values
in a rectangular
subarray from the upper-left corner
to the position of $X$.

## Minimum queries

Minimum queries are more difficult to process
than sum queries.
Still, there is a quite simple 
$O(n \log n)$ time preprocessing
method after which we can answer any minimum
query in $O(1)$ time[^1].
Note that since minimum and maximum queries can
be processed similarly,
we can focus on minimum queries.

The idea is to precalculate all values of
$min_q(a,b)$ where
$b-a+1$ (the length of the range) is a power of two.
For example, for the array

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {8};
\node at (4.5,0.5) {6};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {4};
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
the following values are calculated:

| a | b | $min_q(a,b)$ |
| --- | --- | :---: |
| 0 | 0 | 1 |
| 1 | 1 | 3 |
| 2 | 2 | 4 |
| 3 | 3 | 8 |
| 4 | 4 | 6 |
| 5 | 5 | 1 |
| 6 | 6 | 4 |
| 7 | 7 | 2 |

| a | b | $min_q(a,b)$ |
| --- | --- | :---: |
| 0 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 4 |
| 3 | 4 | 6 |
| 4 | 5 | 1 |
| 5 | 6 | 1 |
| 6 | 7 | 2 |

| a | b | $min_q(a,b)$ |
| --- | --- | :---: |
| 0 | 3 | 1 |
| 1 | 4 | 3 |
| 2 | 5 | 1 |
| 3 | 6 | 1 |
| 4 | 7 | 1 |
| 0 | 7 | 1 |

The number of precalculated values is $O(n \log n)$,
because there are $O(\log n)$ range lengths
that are powers of two.
The values can be calculated efficiently
using the recursive formula

\\[
\\texttt{min}_q(a,b) = \\min(\\texttt{min}_q(a,a+w-1),\\texttt{min}_q(a+w,b)),
\\]

where $b-a+1$ is a power of two and $w=(b-a+1)/2$.
Calculating all those values takes $O(n \log n)$ time.

After this, any value of $min_q(a,b)$ can be calculated
in $O(1)$ time as a minimum of two precalculated values.
Let $k$ be the largest power of two that does not exceed $b-a+1$.
We can calculate the value of $min_q(a,b)$ using the formula

\\[
\\texttt{min}_q(a,b) = \\min(\\texttt{min}_q(a,a+k-1),\\texttt{min}_q(b-k+1,b))
\\]

In the above formula, the range \\( [a,b] \\) is represented
as the union of the ranges \\( [a,a+k-1]\\)  and \\([b-k+1,b]\\), both of length $k$.

As an example, consider the range \\([1,6]\\):

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (1,0) rectangle (7,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {8};
\node at (4.5,0.5) {6};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {4};
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

The length of the range is 6,
and the largest power of two that does
not exceed 6 is 4.
Thus the range \\([1,6]\\) is
the union of the ranges \\([1,4]\\) and \\([3,6]\\):

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (1,0) rectangle (5,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {8};
\node at (4.5,0.5) {6};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {4};
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

 

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (3,0) rectangle (7,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {8};
\node at (4.5,0.5) {6};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {4};
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

Since $min_q(1,4)=3$ and $min_q(3,6)=1$,
we conclude that $min_q(1,6)=1$.

___

[^1] This technique was introduced in [7] and sometimes called the **sparse table** method.  There are also more sophisticated techniques [22] where the preprocessing time is only $O(n)$, but such algorithms are not needed in competitive programming.
