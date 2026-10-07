# Randomized algorithms

Sometimes we can use randomness for solving a problem,
even if the problem is not related to probabilities.
A **randomized algorithm** is an algorithm that
is based on randomness.

A **Monte Carlo algorithm** is a randomized algorithm
that may sometimes give a wrong answer.
For such an algorithm to be useful,
the probability of a wrong answer should be small.

A **Las Vegas algorithm** is a randomized algorithm
that always gives the correct answer,
but its running time varies randomly.
The goal is to design an algorithm that is
efficient with high probability.

Next we will go through three example problems that
can be solved using randomness.

### Randomness in Rust

Rust's standard library has no random number generator, and the `rand`
crate is not available in this book's runnable examples, so the code
below uses a **xorshift** generator written out in full:

```rust
fn next(state: &mut u64) -> u64 {
    *state ^= *state << 13;
    *state ^= *state >> 7;
    *state ^= *state << 17;
    *state
}

// a value in 0..n, good enough for these examples
fn below(state: &mut u64, n: usize) -> usize {
    (next(state) % n as u64) as usize
}
# let mut rng = 88172645463325252u64;
# let rolls: Vec<usize> = (0..10).map(|_| below(&mut rng, 6) + 1).collect();
# println!("ten dice rolls: {rolls:?}");
```

The seed is a fixed constant so the examples print the same thing every
time. A real contest solution seeds from the clock instead, which cannot
be shown as a runnable block here because the output would change on
every run:

```rust, ignore
use std::time::{SystemTime, UNIX_EPOCH};
let mut rng = SystemTime::now()
    .duration_since(UNIX_EPOCH)
    .unwrap()
    .as_nanos() as u64;
```

Note that the state must never be zero: xorshift maps 0 to 0 and would
produce nothing but zeros forever.

## Order statistics

The $kth$ **order statistic** of an array
is the element at position $k$ after sorting
the array in increasing order.
It is easy to calculate any order statistic
in $O(n \log n)$ time by first sorting the array,
but is it really needed to sort the entire array
just to find one element?

It turns out that we can find order statistics
using a randomized algorithm without sorting the array.
The algorithm, called **quickselect**[^1], is a Las Vegas algorithm:
its running time is usually $O(n)$
but $O(n^2)$ in the worst case.

The algorithm chooses a random element $x$
of the array, and moves elements smaller than $x$
to the left part of the array,
and all other elements to the right part of the array.
This takes $O(n)$ time when there are $n$ elements.
Assume that the left part contains $a$ elements
and the right part contains $b$ elements.
If $a=k$, element $x$ is the $k$th order statistic.
Otherwise, if $a>k$, we recursively find the $k$th order
statistic for the left part,
and if $a<k$, we recursively find the $r$th order
statistic for the right part where $r=k-a$.
The search continues in a similar way, until the element
has been found.

When each element $x$ is randomly chosen,
the size of the array about halves at each step,
so the time complexity for
finding the $k$th order statistic is about
\\[
n+n/2+n/4+n/8+\\cdots < 2n = O(n).
\\]

The worst case of the algorithm requires still $O(n^2)$ time,
because it is possible that $x$ is always chosen
in such a way that it is one of the smallest or largest
elements in the array and $O(n)$ steps are needed.
However, the probability for this is so small
that this never happens in practice.

## Verifying matrix multiplication

Our next problem is to _verify_
if $AB=C$ holds when $A$, $B$ and $C$
are matrices of size $n \times n$.
Of course, we can solve the problem
by calculating the product $AB$ again
(in $O(n^3)$ time using the basic algorithm),
but one could hope that verifying the
answer would by easier than to calculate it from scratch.

It turns out that we can solve the problem
using a Monte Carlo algorithm[^2] whose
time complexity is only $O(n^2)$.
The idea is simple: we choose a random vector
$X$ of $n$ elements, and calculate the matrices
$ABX$ and $CX$. If $ABX=CX$, we report that $AB=C$,
and otherwise we report that $AB \neq C$.

The time complexity of the algorithm is
$O(n^2)$, because we can calculate the matrices
$ABX$ and $CX$ in $O(n^2)$ time.
We can calculate the matrix $ABX$ efficiently
by using the representation $A(BX)$, so only two
multiplications of $n \times n$ and $n \times 1$
size matrices are needed.

The drawback of the algorithm is
that there is a small chance that the algorithm
makes a mistake when it reports that $AB=C$.
For example, 
\\[
\\begin{bmatrix}
  6 & 8 \\\\
  1 & 3 \\\\
 \\end{bmatrix}
\\neq
 \\begin{bmatrix}
  8 & 7 \\\\
  3 & 2 \\\\
 \\end{bmatrix},
\\]
but
\\[
\\begin{bmatrix}
  6 & 8 \\\\
  1 & 3 \\\\
 \\end{bmatrix}
 \\begin{bmatrix}
  3 \\\\
  6 \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  8 & 7 \\\\
  3 & 2 \\\\
 \\end{bmatrix}
 \\begin{bmatrix}
  3 \\\\
  6 \\\\
 \\end{bmatrix}.
\\]
However, in practice, the probability that the
algorithm makes a mistake is small,
and we can decrease the probability by
verifying the result using multiple random vectors $X$
before reporting that $AB=C$.

## Graph coloring

Given a graph that contains $n$ nodes and $m$ edges,
our task is to find a way to color the nodes
of the graph using two colors so that
for at least $m/2$ edges, the endpoints 
have different colors.
For example, in the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {$1$};
\node[draw, circle] (2) at (4,3) {$2$};
\node[draw, circle] (3) at (1,1) {$3$};
\node[draw, circle] (4) at (4,1) {$4$};
\node[draw, circle] (5) at (6,2) {$5$};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);
\end{tikzpicture}
</script>

a valid coloring is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle, fill=blue!40] (1) at (1,3) {$1$};
\node[draw, circle, fill=red!40] (2) at (4,3) {$2$};
\node[draw, circle, fill=red!40] (3) at (1,1) {$3$};
\node[draw, circle, fill=blue!40] (4) at (4,1) {$4$};
\node[draw, circle, fill=blue!40] (5) at (6,2) {$5$};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);
\end{tikzpicture}
</script>

The above graph contains 7 edges, and for 5 of them,
the endpoints have different colors,
so the coloring is valid.

The problem can be solved using a Las Vegas algorithm
that generates random colorings until a valid coloring
has been found.
In a random coloring, the color of each node is
independently chosen so that the probability of
both colors is $1/2$.

In a random coloring, the probability that the endpoints
of a single edge have different colors is $1/2$.
Hence, the expected number of edges whose endpoints
have different colors is $m/2$.
Since it is expected that a random coloring is valid,
we will quickly find a valid coloring in practice.

___

[^1]: In 1961,
C. A. R. Hoare published two algorithms that
are efficient on average:  
**quicksort** [40] for sorting arrays and
**quickselect** [41] for finding order statistics.

[^2]: R. M. Freivalds published
this algorithm in 1977 [29], and it is sometimes
called  **Freivalds' algorithm**.
