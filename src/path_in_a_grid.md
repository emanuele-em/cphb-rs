# Paths in a grid

Our next problem is to find a path
from the upper-left corner to
the lower-right corner
of an $n \times n$ grid, such that
we only move down and right.
Each square contains a positive integer,
and the path should be constructed so
that the sum of the values along
the path is as large as possible.

The following picture shows an optimal
path in a grid:

<script type="text/tikz">
\begin{tikzpicture}[scale=.65]
  \begin{scope}
    \fill [color=lightgray] (0, 9) rectangle (1, 8);
    \fill [color=lightgray] (0, 8) rectangle (1, 7);
    \fill [color=lightgray] (1, 8) rectangle (2, 7);
    \fill [color=lightgray] (1, 7) rectangle (2, 6);
    \fill [color=lightgray] (2, 7) rectangle (3, 6);
    \fill [color=lightgray] (3, 7) rectangle (4, 6);
    \fill [color=lightgray] (4, 7) rectangle (5, 6);
    \fill [color=lightgray] (4, 6) rectangle (5, 5);
    \fill [color=lightgray] (4, 5) rectangle (5, 4);
    \draw (0, 4) grid (5, 9);
    \node at (0.5,8.5) {3};
    \node at (1.5,8.5) {7};
    \node at (2.5,8.5) {9};
    \node at (3.5,8.5) {2};
    \node at (4.5,8.5) {7};
    \node at (0.5,7.5) {9};
    \node at (1.5,7.5) {8};
    \node at (2.5,7.5) {3};
    \node at (3.5,7.5) {5};
    \node at (4.5,7.5) {5};
    \node at (0.5,6.5) {1};
    \node at (1.5,6.5) {7};
    \node at (2.5,6.5) {9};
    \node at (3.5,6.5) {8};
    \node at (4.5,6.5) {5};
    \node at (0.5,5.5) {3};
    \node at (1.5,5.5) {8};
    \node at (2.5,5.5) {6};
    \node at (3.5,5.5) {4};
    \node at (4.5,5.5) {10};
    \node at (0.5,4.5) {6};
    \node at (1.5,4.5) {3};
    \node at (2.5,4.5) {9};
    \node at (3.5,4.5) {7};
    \node at (4.5,4.5) {8};
  \end{scope}
\end{tikzpicture}
</script>

The sum of the values on the path is 67,
and this is the largest possible sum on a path
from the
upper-left corner to the lower-right corner.

Assume that the rows and columns of the
grid are numbered from 1 to $n$,
and $\texttt{value}[y][x]$ equals the value
of square $(y,x)$.
Let $\texttt{sum}(y,x)$ denote the maximum
sum on a path from the upper-left corner
to square $(y,x)$.
Now $\texttt{sum}(n,n)$ tells us
the maximum sum
from the upper-left corner to
the lower-right corner.
For example, in the above grid,
$\texttt{sum}(5,5)=67$.

We can recursively calculate the sums
as follows:
\\[
    \texttt{sum}(y,x) = \max(\texttt{sum}(y,x-1),\texttt{sum}(y-1,x))+\texttt{value}[y][x]
\\]

The recursive formula is based on the observation
that a path that ends at square $(y,x)$
can come either from square $(y,x-1)$
or square $(y-1,x)$:

<script type="text/tikz">
\begin{tikzpicture}[scale=.65]
  \begin{scope}
    \fill [color=lightgray] (3, 7) rectangle (4, 6);
    \draw (0, 4) grid (5, 9);
    
    \node at (2.5,6.5) {$\rightarrow$};
    \node at (3.5,7.5) {$\downarrow$};
    
  \end{scope}
\end{tikzpicture}
</script>

Thus, we select the direction that maximizes
the sum.
We assume that $\texttt{sum}(y,x)=0$
if $y=0$ or $x=0$ (because no such paths exist),
so the recursive formula also works when $y=1$ or $x=1$.

Since the function \texttt{sum} has two parameters,
the dynamic programming array also has two dimensions.
For example, we can use an array

```rust
let mut sum: Vec<Vec<usize>>= vec![vec![]];
```
and calculate the sums as follows:
```rust
# use std::cmp;
# let value = vec![ vec![3, 7, 9, 2, 7],
                    # vec![9, 8, 3, 5, 5],
                    # vec![1, 7, 9, 8, 5],
                    # vec![3, 8, 6, 4, 10],
                    # vec![6, 3, 9, 7, 8],];
# let mut sum = value.clone();
# let n = value.len()-1;
for y in 1..=n{
    for x in 1..=n{
        sum[y][x] = cmp::max(sum[y][x-1], sum[y-1][x])+value[y][x];
# print!("{} ", sum[y][x]);
    }
#println!("");
}
```
