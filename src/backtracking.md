# Backtracking

A **backtracking** algorithm
begins with an empty solution
and extends the solution step by step.
The search recursively
goes through all different ways how
a solution can be constructed.

## Queen problem

As an example, consider the problem of
calculating the number
of ways $n$ queens can be placed on
an $n \times n$ chessboard so that
no two queens attack each other.
For example, when $n=4$,
there are two possible solutions:

<script type="text/tikz">
\begin{tikzpicture}[scale=1]
  \begin{scope}
    \draw (0, 0) grid (4, 4);
    \node at (1.5,3.5) {Q};
    \node at (3.5,2.5) {Q};
    \node at (0.5,1.5) {Q};
    \node at (2.5,0.5) {Q};
    \draw (6, 0) grid (10, 4);
    \node at (6+2.5,3.5) {Q};
    \node at (6+0.5,2.5) {Q};
    \node at (6+3.5,1.5) {Q};
    \node at (6+1.5,0.5) {Q};
  \end{scope}
\end{tikzpicture}
</script>

The problem can be solved using backtracking
by placing queens to the board row by row.
More precisely, exactly one queen will
be placed on each row so that no queen attacks
any of the queens placed before.
A solution has been found when all
$n$ queens have been placed on the board.

For example, when $n=4$,
some partial solutions generated by
the backtracking algorithm are as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.6]
  \begin{scope}
    \draw (0, 0) grid (4, 4);

    \draw (-9, -6) grid (-5, -2);
    \draw (-3, -6) grid (1, -2);
    \draw (3, -6) grid (7, -2);
    \draw (9, -6) grid (13, -2);

    \node at (-9+0.5,-3+0.5) {Q};
    \node at (-3+1+0.5,-3+0.5) {Q};
    \node at (3+2+0.5,-3+0.5) {Q};
    \node at (9+3+0.5,-3+0.5) {Q};

    \draw (2,0) -- (-7,-2);
    \draw (2,0) -- (-1,-2);
    \draw (2,0) -- (5,-2);
    \draw (2,0) -- (11,-2);

    \draw (-11, -12) grid (-7, -8);
    \draw (-6, -12) grid (-2, -8);
    \draw (-1, -12) grid (3, -8);
    \draw (4, -12) grid (8, -8);
    \draw[transparent] (11, -12) grid (15, -8);
    \node at (-11+1+0.5,-9+0.5) {Q};
    \node at (-6+1+0.5,-9+0.5) {Q};
    \node at (-1+1+0.5,-9+0.5) {Q};
    \node at (4+1+0.5,-9+0.5) {Q};
    \node at (-11+0+0.5,-10+0.5) {Q};
    \node at (-6+1+0.5,-10+0.5) {Q};
    \node at (-1+2+0.5,-10+0.5) {Q};
    \node at (4+3+0.5,-10+0.5) {Q};

    \draw (-1,-6) -- (-9,-8);
    \draw (-1,-6) -- (-4,-8);
    \draw (-1,-6) -- (1,-8);
    \draw (-1,-6) -- (6,-8);

    \node at (-9,-13) {illegal};
    \node at (-4,-13) {illegal};
    \node at (1,-13) {illegal};
    \node at (6,-13) {valid};

  \end{scope}
\end{tikzpicture}
</script>

At the bottom level, the three first configurations
are illegal, because the queens attack each other.
However, the fourth configuration is valid
and it can be extended to a complete solution by
placing two more queens to the board.
There is only one way to place the two remaining queens.

The algorithm can be implemented as follows:
```rust
# let n = 4;
# let mut count = 0;
# let mut column = vec![false;n];
# let mut diag1 = vec![false;2*n-1];
# let mut diag2 = vec![false;2*n-1];
# search(0, n, &mut count, &mut column, &mut diag1, &mut diag2);
# println!{"{count}"};
fn search(y: usize, n: usize, count: &mut usize, column: &mut Vec<bool>, diag1: &mut Vec<bool>, diag2: &mut Vec<bool>) {
    if y == n {
        *count += 1;
        return;
    }
    for x in 0..n {
        if column[x] || diag1[x + y] || diag2[x.wrapping_sub(y).wrapping_add(n).wrapping_sub(1)] {
            continue;
        }
        column[x] = true;
        diag1[x + y] = true;
        diag2[x + n - y - 1] = true;
        search(y + 1, n, count, column, diag1, diag2);
        column[x] = false;
        diag1[x + y] = false;
        diag2[x + n - y - 1] = false;
    }
}
```

> `wrapping_sub` is used to avoid that a negative number has used as `usize`

The search begins by calling `search(0, n, &mut count, &mut column, &mut diag1, &mut diag2)`;
The size of the board is $n \times n$,
and the code calculates the number of solutions
to `count`.

The code assumes that the rows and columns
of the board are numbered from 0 to $n-1$.
When the function `search` is
called with parameter $y$,
it places a queen on row $y$
and then calls itself with parameter $y+1$.
Then, if $y=n$, a solution has been found
and the variable `count` is increased by one.

The `Vec` `column` keeps track of columns
that contain a queen,
and the arrays `diag1` and `diag2`
keep track of diagonals.
It is not allowed to add another queen to a
column or diagonal that already contains a queen. 
For example, the columns and diagonals of
the $4 \times 4$ board are numbered as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=1]
  \begin{scope}
    \draw (0-6, 0) grid (4-6, 4);
    \node at (-6+0.5,3.5) {0};
    \node at (-6+1.5,3.5) {1};
    \node at (-6+2.5,3.5) {2};
    \node at (-6+3.5,3.5) {3};
    \node at (-6+0.5,2.5) {0};
    \node at (-6+1.5,2.5) {1};
    \node at (-6+2.5,2.5) {2};
    \node at (-6+3.5,2.5) {3};
    \node at (-6+0.5,1.5) {0};
    \node at (-6+1.5,1.5) {1};
    \node at (-6+2.5,1.5) {2};
    \node at (-6+3.5,1.5) {3};
    \node at (-6+0.5,0.5) {0};
    \node at (-6+1.5,0.5) {1};
    \node at (-6+2.5,0.5) {2};
    \node at (-6+3.5,0.5) {3};

    \draw (0, 0) grid (4, 4);
    \node at (0.5,3.5) {0};
    \node at (1.5,3.5) {1};
    \node at (2.5,3.5) {2};
    \node at (3.5,3.5) {3};
    \node at (0.5,2.5) {1};
    \node at (1.5,2.5) {2};
    \node at (2.5,2.5) {3};
    \node at (3.5,2.5) {4};
    \node at (0.5,1.5) {2};
    \node at (1.5,1.5) {3};
    \node at (2.5,1.5) {4};
    \node at (3.5,1.5) {5};
    \node at (0.5,0.5) {3};
    \node at (1.5,0.5) {4};
    \node at (2.5,0.5) {5};
    \node at (3.5,0.5) {6};
    \draw (6, 0) grid (10, 4);
    \node at (6.5,3.5) {3};
    \node at (7.5,3.5) {4};
    \node at (8.5,3.5) {5};
    \node at (9.5,3.5) {6};
    \node at (6.5,2.5) {2};
    \node at (7.5,2.5) {3};
    \node at (8.5,2.5) {4};
    \node at (9.5,2.5) {5};
    \node at (6.5,1.5) {1};
    \node at (7.5,1.5) {2};
    \node at (8.5,1.5) {3};
    \node at (9.5,1.5) {4};
    \node at (6.5,0.5) {0};
    \node at (7.5,0.5) {1};
    \node at (8.5,0.5) {2};
    \node at (9.5,0.5) {3};
    \node at (-4,-1) {\texttt{column}};
    \node at (2,-1) {\texttt{diag1}};
    \node at (8,-1) {\texttt{diag2}};
  \end{scope}
\end{tikzpicture}
</script>
Let $q(n)$ denote the number of ways
to place $n$ queens on an $n \times n$ chessboard.
The above backtracking
algorithm tells us that, for example, $q(8)=92$.
When $n$ increases, the search quickly becomes slow,
because the number of solutions increases
exponentially.
For example, calculating $q(16)=14772512$
using the above algorithm already takes about a minute
on a modern computer[^1]
___

[^1] There is no known way to efficiently calculate larger values of $q(n)$.  The current record is $q(27)=234907967154122528$, calculated in 2016 [55].
