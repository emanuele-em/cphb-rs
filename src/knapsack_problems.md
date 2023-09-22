# Knapsack problems

The term knapsack refers to problems where
a set of objects is given, and 
subsets with some properties
have to be found.
Knapsack problems can often be solved
using dynamic programming.

In this section, we focus on the following
problem: Given a list of weights
\\([w_1,w_2,\ldots,w_n]\\),
determine all
sums that can be constructed using the weights.
For example, if the weights are
\\([1,3,3,5]\\), the following sums are possible:


| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X | X | | X | X | X | X | X | X | X | | X | X |

In this case, all sums between $0 \ldots 12$
are possible, except 2 and 10.
For example, the sum 7 is possible because we
can select the weights $[1,3,3]$.

To solve the problem, we focus on subproblems
where we only use the first $k$ weights
to construct sums.

Let `possible(x,k)=true` if
we can construct a sum $x$
using the first $k$ weights,
and otherwise `possible(x,k)=false`.
The values of the function can be recursively
calculated as follows:

\\[ \texttt{possible}(x,k) = \texttt{possible}(x-w_k,k-1) \lor \texttt{possible}(x,k-1) \\]

The formula is based on the fact that we can
either use or not use the weight $w_k$ in the sum.
If we use $w_k$, the remaining task is to
form the sum $x-w_k$ using the first $k-1$ weights,
and if we do not use $w_k$,
the remaining task is to form the sum $x$
using the first $k-1$ weights.
As the base cases,
\\[
\begin{equation*}
    \texttt{possible}(x,0) = \begin{cases}
               \textrm{true}    & x = 0\\\\
               \textrm{false}   & x \neq 0 \\\\
           \end{cases}
\end{equation*}
\\]
because if no weights are used,
we can only form the sum 0.

The following table shows all values of the function
for the weights $[1,3,3,5]$ (the symbol "X"
indicates the true values):

| k \ x | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | X | | | | | | | | | | | |
| 1 | X | X | | | | | | | | | |
|  2 | X | X | | X | X | | | | | | |
| 3 | X | X | | X | X | | X | X | | | |
| 4 | X | X | | X | X | X | X | X | X | X | | X | X |

After calculating those values, $\texttt{possible}(x,n)$
tells us whether we can construct a
sum $x$ using **all** weights.

Let $W$ denote the total sum of the weights.
The following $O(nW)$ time
dynamic programming solution
corresponds to the recursive function:
```rust
# let w = vec![1,3,3,5];
# let W = w.iter().sum();
# let n = w.len();
# let  mut possible: Vec<Vec<bool>> = vec![vec![false;n];W];
possible[0][0] = true;
for k in 1..n {
    for x in 0..W {
        if x >= w[k] {
            possible[x][k] |= possible[x.wrapping_sub(w[k])][k.wrapping_sub(1)];
        }
        possible[x][k] |= possible[x][k-1];
    }
}
# println!("{:#?}", possible);
```

However, here is a better implementation that only uses
a one-dimensional array $\texttt{possible}[x]$
that indicates whether we can construct a subset with sum $x$.
The trick is to update the array from right to left for
each new weight:
```rust
# let w = vec![1,3,3,5];
# let W = w.iter().sum();
# let n = w.len();
# let  mut possible: Vec<bool> = vec![false;W];
possible[0] = true;
for k in 1..n {
    for x in (0..W).rev(){
        if possible[x] {possible[x+w[k]] = true;}
    }
}
# println!("{:#?}", possible);
```

Note that the general idea presented here can be used
in many knapsack problems.
For example, if we are given objects with weights and values,
we can determine for each weight sum the maximum value
sum of a subset.

