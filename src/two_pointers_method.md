# Two pointers method

In the **two pointers method**,
two pointers are used to
iterate through the array values.
Both pointers can move to one direction only,
which ensures that the algorithm works efficiently.
Next we discuss two problems that can be solved
using the two pointers method.

## Subarray Sum

As the first example,
consider a problem where we are
given an array of $n$ positive integers
and a target sum $x$,
and we want to find a subarray whose sum is $x$
or report that there is no such subarray.

For example, the array

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);
\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {2};
\node at (3.5,0.5) {5};
\node at (4.5,0.5) {1};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {2};
\node at (7.5,0.5) {3};
\end{tikzpicture}
</script>

contains a subarray whose sum is 8:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (2,0) rectangle (5,1);
\draw (0,0) grid (8,1);
\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {2};
\node at (3.5,0.5) {5};
\node at (4.5,0.5) {1};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {2};
\node at (7.5,0.5) {3};
\end{tikzpicture}
</script>

This problem can be solved in
$O(n)$ time by using the two pointers method.
The idea is to maintain pointers that point to the
first and last value of a subarray.
On each turn, the left pointer moves one step
to the right, and the right pointer moves to the right
as long as the resulting subarray sum is at most $x$.
If the sum becomes exactly $x$,
a solution has been found.

As an example, consider the following array
and a target sum $x=8$:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {2};
\node at (3.5,0.5) {5};
\node at (4.5,0.5) {1};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {2};
\node at (7.5,0.5) {3};
\end{tikzpicture}
</script>

The initial subarray contains the values
1, 3 and 2 whose sum is 6:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (0,0) rectangle (3,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {2};
\node at (3.5,0.5) {5};
\node at (4.5,0.5) {1};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {2};
\node at (7.5,0.5) {3};

\draw[thick,->] (0.5,-0.7) -- (0.5,-0.1);
\draw[thick,->] (2.5,-0.7) -- (2.5,-0.1);
\end{tikzpicture}
</script>

Then, the left pointer moves one step to the right.
The right pointer does not move, because otherwise
the subarray sum would exceed $x$.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (1,0) rectangle (3,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {2};
\node at (3.5,0.5) {5};
\node at (4.5,0.5) {1};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {2};
\node at (7.5,0.5) {3};

\draw[thick,->] (1.5,-0.7) -- (1.5,-0.1);
\draw[thick,->] (2.5,-0.7) -- (2.5,-0.1);
\end{tikzpicture}
</script>

Again, the left pointer moves one step to the right,
and this time the right pointer moves three
steps to the right.
The subarray sum is $2+5+1=8$, so a subarray
whose sum is $x$ has been found.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (2,0) rectangle (5,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {2};
\node at (3.5,0.5) {5};
\node at (4.5,0.5) {1};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {2};
\node at (7.5,0.5) {3};

\draw[thick,->] (2.5,-0.7) -- (2.5,-0.1);
\draw[thick,->] (4.5,-0.7) -- (4.5,-0.1);
\end{tikzpicture}
</script>

The running time of the algorithm depends on
the number of steps the right pointer moves.
While there is no useful upper bound on how many steps the
pointer can move on a _single_ turn.
we know that the pointer moves _a total of_
$O(n)$ steps during the algorithm,
because it only moves to the right.

Since both the left and right pointer
move $O(n)$ steps during the algorithm,
the algorithm works in $O(n)$ time.


## 2 Sum problem

Another problem that can be solved using
the two pointers method is the following problem,
also known as the **2 SUM proble**:
given an array of $n$ numbers and
a target sum $x$, find
two array values such that their sum is $x$,
or report that no such values exist.

To solve the problem, we first
sort the array values in increasing order.
After that, we iterate through the array using
two pointers.
The left pointer starts at the first value
and moves one step to the right on each turn.
The right pointer begins at the last value
and always moves to the left until the sum of the
left and right value is at most $x$.
If the sum is exactly $x$,
a solution has been found.

For example, consider the following array
and a target sum $x=12$:
<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {4};
\node at (2.5,0.5) {5};
\node at (3.5,0.5) {6};
\node at (4.5,0.5) {7};
\node at (5.5,0.5) {9};
\node at (6.5,0.5) {9};
\node at (7.5,0.5) {10};
\end{tikzpicture}
</script>

The initial positions of the pointers
are as follows.
The sum of the values is $1+10=11$
that is smaller than $x$.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (0,0) rectangle (1,1);
\fill[color=lightgray] (7,0) rectangle (8,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {4};
\node at (2.5,0.5) {5};
\node at (3.5,0.5) {6};
\node at (4.5,0.5) {7};
\node at (5.5,0.5) {9};
\node at (6.5,0.5) {9};
\node at (7.5,0.5) {10};

\draw[thick,->] (0.5,-0.7) -- (0.5,-0.1);
\draw[thick,->] (7.5,-0.7) -- (7.5,-0.1);
\end{tikzpicture}
</script>

Then the left pointer moves one step to the right.
The right pointer moves three steps to the left,
and the sum becomes $4+7=11$.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (1,0) rectangle (2,1);
\fill[color=lightgray] (4,0) rectangle (5,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {4};
\node at (2.5,0.5) {5};
\node at (3.5,0.5) {6};
\node at (4.5,0.5) {7};
\node at (5.5,0.5) {9};
\node at (6.5,0.5) {9};
\node at (7.5,0.5) {10};

\draw[thick,->] (1.5,-0.7) -- (1.5,-0.1);
\draw[thick,->] (4.5,-0.7) -- (4.5,-0.1);
\end{tikzpicture}
</script>

After this, the left pointer moves one step to the right again.
The right pointer does not move, and a solution
$5+7=12$ has been found.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (2,0) rectangle (3,1);
\fill[color=lightgray] (4,0) rectangle (5,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {4};
\node at (2.5,0.5) {5};
\node at (3.5,0.5) {6};
\node at (4.5,0.5) {7};
\node at (5.5,0.5) {9};
\node at (6.5,0.5) {9};
\node at (7.5,0.5) {10};

\draw[thick,->] (2.5,-0.7) -- (2.5,-0.1);
\draw[thick,->] (4.5,-0.7) -- (4.5,-0.1);
\end{tikzpicture}
</script>

The running time of the algorithm is
$O(n \log n)$, because it first sorts
the array in $O(n \log n)$ time,
and then both pointers move $O(n)$ steps.

Note that it is possible to solve the problem
in another way in $O(n \log n)$ time using binary search.
In such a solution, we iterate through the array
and for each array value, we try to find another
value that yields the sum $x$.
This can be done by performing $n$ binary searches,
each of which takes $O(\log n)$ time.

A more difficult problem is 
the **3 SUM problem** that asks to
find _three_ array values
whose sum is $x$.
Using the idea of the above algorithm,
this problem can be solved in $O(n^2)$ time[^1].
Can you see how?

___

[^1] For a long time, it was thought that solving the 3 SUM problem more efficiently than in $O(n^2)$ time would not be possible.  However, in 2014, it turned out [30] that this is not the case.
