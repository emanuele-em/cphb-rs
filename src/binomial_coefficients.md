# Binomial coefficients

The **binomial coefficient** ${n \choose k}$
equals the number of ways we can choose a subset
of $k$ elements from a set of $n$ elements.
For example, ${5 \choose 3}=10$,
because the set $\\{1,2,3,4,5\\}$
has 10 subsets of 3 elements:
\\[
\\begin{array}{l}
\\{1,2,3\\}, \\{1,2,4\\}, \\{1,2,5\\}, \\{1,3,4\\}, \\{1,3,5\\}, \\\\
\\{1,4,5\\}, \\{2,3,4\\}, \\{2,3,5\\}, \\{2,4,5\\}, \\{3,4,5\\}
\\end{array}
\\]

## Formula 1

Binomial coefficients can be
recursively calculated as follows:

\\[
{n \\choose k}  =  {n-1 \\choose k-1} + {n-1 \\choose k}
\\]

The idea is to fix an element $x$ in the set.
If $x$ is included in the subset,
we have to choose $k-1$
elements from $n-1$ elements,
and if $x$ is not included in the subset,
we have to choose $k$ elements from $n-1$ elements.

The base cases for the recursion are
\\[
{n \\choose 0}  =  {n \\choose n} = 1,
\\]
because there is always exactly
one way to construct an empty subset
and a subset that contains all the elements.

Using the recursion directly would recalculate the same values over and
over, so we fill a table instead. Row $i$ of the table holds all
coefficients ${i \choose j}$, and each entry is the sum of the two
entries above it:

```rust
# let n = 5;
# let k = 3;
let mut binom = vec![vec![0u64; n+1]; n+1];
for i in 0..=n {
    binom[i][0] = 1;
    for j in 1..=i {
        binom[i][j] = binom[i-1][j-1] + binom[i-1][j];
    }
}
# println!("C({n},{k}) = {}", binom[n][k]);
```

This is Pascal's triangle, and it computes every coefficient up to
${n \choose k}$ in $O(n^2)$ time using only additions.

## Formula 2

Another way to calculate binomial coefficients is as follows:
\\[
{n \\choose k}  =  \\frac{n!}{k!(n-k)!}.
\\]

There are $n!$ permutations of $n$ elements.
We go through all permutations and always
include the first $k$ elements of the permutation
in the subset.
Since the order of the elements in the subset
and outside the subset does not matter,
the result is divided by $k!$ and $(n-k)!$

Factorials overflow quickly, so in practice this formula is evaluated
modulo a prime $M$. Division is not available in modular arithmetic, but
since $M$ is prime we can multiply by a modular inverse instead, using
Fermat's theorem and the `modpow` function from the chapter on modular
arithmetic:

```rust
# const M: usize = 1_000_000_007;
# fn modpow(x: usize, n: usize, m: usize) -> usize {
#     if n == 0 {return 1%m}
#     let mut u = modpow(x, n/2, m);
#     u = (u*u)%m;
#     if n%2 == 1 {u = (u*x)%m}
#     u
# }
# let n = 5;
# let k = 3;
let mut fact = vec![1usize; n+1];
for i in 1..=n {
    fact[i] = fact[i-1] * i % M;
}
// a^(M-2) is the inverse of a, because M is prime
let inv = |a: usize| modpow(a, M-2, M);
let binom = fact[n] * inv(fact[k]) % M * inv(fact[n-k]) % M;
# println!("C({n},{k}) mod M = {binom}");
```

Every product stays below $M^2 \approx 10^{18}$, which fits in a `usize`
on a 64-bit target, so no intermediate value overflows.

## Properties

For binomial coefficients,
\\[
{n \\choose k}  =  {n \\choose n-k},
\\]
because we actually divide a set of $n$ elements into
two subsets: the first contains $k$ elements
and the second contains $n-k$ elements.

The sum of binomial coefficients is
\\[
{n \\choose 0}+{n \\choose 1}+{n \\choose 2}+\\ldots+{n \\choose n}=2^n.
\\]

The reason for the name ''binomial coefficient''
can be seen when the binomial $(a+b)$ is raised to
the $n$th power:

\\[
(a+b)^n =
{n \\choose 0} a^n b^0 + 
{n \\choose 1} a^{n-1} b^1 +
\\ldots + 
{n \\choose n-1} a^1 b^{n-1} +
{n \\choose n} a^0 b^n.
\\]

Binomial coefficients also appear in
**Pascal's triangle**
where each value equals the sum of two
above values:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node at (0,0) {1};
\node at (-0.5,-0.5) {1};
\node at (0.5,-0.5) {1};
\node at (-1,-1) {1};
\node at (0,-1) {2};
\node at (1,-1) {1};
\node at (-1.5,-1.5) {1};
\node at (-0.5,-1.5) {3};
\node at (0.5,-1.5) {3};
\node at (1.5,-1.5) {1};
\node at (-2,-2) {1};
\node at (-1,-2) {4};
\node at (0,-2) {6};
\node at (1,-2) {4};
\node at (2,-2) {1};
\node at (-2,-2.5) {$\ldots$};
\node at (-1,-2.5) {$\ldots$};
\node at (0,-2.5) {$\ldots$};
\node at (1,-2.5) {$\ldots$};
\node at (2,-2.5) {$\ldots$};
\end{tikzpicture}
</script>

## Boxes and balls

''Boxes and balls'' is a useful model,
where we count the ways to
place $k$ balls in $n$ boxes.
Let us consider three scenarios:

_Scenario 1_: Each box can contain
at most one ball.
For example, when $n=5$ and $k=2$,
there are 10 solutions:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.5]

    
\path[draw,thick,-] (0-0.5,0+0.5) -- (0-0.5,0-0.5) --
                    (0+0.5,0-0.5) -- (0+0.5,0+0.5);
\draw[fill=black] (0,0-0.3) circle (0.15);

    
\path[draw,thick,-] (0+1.2-0.5,0+0.5) -- (0+1.2-0.5,0-0.5) --
                    (0+1.2+0.5,0-0.5) -- (0+1.2+0.5,0+0.5);
\draw[fill=black] (0+1.2,0-0.3) circle (0.15);

    
\path[draw,thick,-] (0+2.4-0.5,0+0.5) -- (0+2.4-0.5,0-0.5) --
                    (0+2.4+0.5,0-0.5) -- (0+2.4+0.5,0+0.5);

    
\path[draw,thick,-] (0+3.6-0.5,0+0.5) -- (0+3.6-0.5,0-0.5) --
                    (0+3.6+0.5,0-0.5) -- (0+3.6+0.5,0+0.5);

    
\path[draw,thick,-] (0+4.8-0.5,0+0.5) -- (0+4.8-0.5,0-0.5) --
                    (0+4.8+0.5,0-0.5) -- (0+4.8+0.5,0+0.5);

    
\path[draw,thick,-] (0-0.5,-2+0.5) -- (0-0.5,-2-0.5) --
                    (0+0.5,-2-0.5) -- (0+0.5,-2+0.5);
\draw[fill=black] (0,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (0+1.2-0.5,-2+0.5) -- (0+1.2-0.5,-2-0.5) --
                    (0+1.2+0.5,-2-0.5) -- (0+1.2+0.5,-2+0.5);

    
\path[draw,thick,-] (0+2.4-0.5,-2+0.5) -- (0+2.4-0.5,-2-0.5) --
                    (0+2.4+0.5,-2-0.5) -- (0+2.4+0.5,-2+0.5);
\draw[fill=black] (0+2.4,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (0+3.6-0.5,-2+0.5) -- (0+3.6-0.5,-2-0.5) --
                    (0+3.6+0.5,-2-0.5) -- (0+3.6+0.5,-2+0.5);

    
\path[draw,thick,-] (0+4.8-0.5,-2+0.5) -- (0+4.8-0.5,-2-0.5) --
                    (0+4.8+0.5,-2-0.5) -- (0+4.8+0.5,-2+0.5);

    
\path[draw,thick,-] (0-0.5,-4+0.5) -- (0-0.5,-4-0.5) --
                    (0+0.5,-4-0.5) -- (0+0.5,-4+0.5);
\draw[fill=black] (0,-4-0.3) circle (0.15);

    
\path[draw,thick,-] (0+1.2-0.5,-4+0.5) -- (0+1.2-0.5,-4-0.5) --
                    (0+1.2+0.5,-4-0.5) -- (0+1.2+0.5,-4+0.5);

    
\path[draw,thick,-] (0+2.4-0.5,-4+0.5) -- (0+2.4-0.5,-4-0.5) --
                    (0+2.4+0.5,-4-0.5) -- (0+2.4+0.5,-4+0.5);

    
\path[draw,thick,-] (0+3.6-0.5,-4+0.5) -- (0+3.6-0.5,-4-0.5) --
                    (0+3.6+0.5,-4-0.5) -- (0+3.6+0.5,-4+0.5);
\draw[fill=black] (0+3.6,-4-0.3) circle (0.15);

    
\path[draw,thick,-] (0+4.8-0.5,-4+0.5) -- (0+4.8-0.5,-4-0.5) --
                    (0+4.8+0.5,-4-0.5) -- (0+4.8+0.5,-4+0.5);

    
\path[draw,thick,-] (0-0.5,-6+0.5) -- (0-0.5,-6-0.5) --
                    (0+0.5,-6-0.5) -- (0+0.5,-6+0.5);
\draw[fill=black] (0,-6-0.3) circle (0.15);

    
\path[draw,thick,-] (0+1.2-0.5,-6+0.5) -- (0+1.2-0.5,-6-0.5) --
                    (0+1.2+0.5,-6-0.5) -- (0+1.2+0.5,-6+0.5);

    
\path[draw,thick,-] (0+2.4-0.5,-6+0.5) -- (0+2.4-0.5,-6-0.5) --
                    (0+2.4+0.5,-6-0.5) -- (0+2.4+0.5,-6+0.5);

    
\path[draw,thick,-] (0+3.6-0.5,-6+0.5) -- (0+3.6-0.5,-6-0.5) --
                    (0+3.6+0.5,-6-0.5) -- (0+3.6+0.5,-6+0.5);

    
\path[draw,thick,-] (0+4.8-0.5,-6+0.5) -- (0+4.8-0.5,-6-0.5) --
                    (0+4.8+0.5,-6-0.5) -- (0+4.8+0.5,-6+0.5);
\draw[fill=black] (0+4.8,-6-0.3) circle (0.15);

    
\path[draw,thick,-] (8-0.5,0+0.5) -- (8-0.5,0-0.5) --
                    (8+0.5,0-0.5) -- (8+0.5,0+0.5);

    
\path[draw,thick,-] (8+1.2-0.5,0+0.5) -- (8+1.2-0.5,0-0.5) --
                    (8+1.2+0.5,0-0.5) -- (8+1.2+0.5,0+0.5);
\draw[fill=black] (8+1.2,0-0.3) circle (0.15);

    
\path[draw,thick,-] (8+2.4-0.5,0+0.5) -- (8+2.4-0.5,0-0.5) --
                    (8+2.4+0.5,0-0.5) -- (8+2.4+0.5,0+0.5);
\draw[fill=black] (8+2.4,0-0.3) circle (0.15);

    
\path[draw,thick,-] (8+3.6-0.5,0+0.5) -- (8+3.6-0.5,0-0.5) --
                    (8+3.6+0.5,0-0.5) -- (8+3.6+0.5,0+0.5);

    
\path[draw,thick,-] (8+4.8-0.5,0+0.5) -- (8+4.8-0.5,0-0.5) --
                    (8+4.8+0.5,0-0.5) -- (8+4.8+0.5,0+0.5);

    
\path[draw,thick,-] (8-0.5,-2+0.5) -- (8-0.5,-2-0.5) --
                    (8+0.5,-2-0.5) -- (8+0.5,-2+0.5);

    
\path[draw,thick,-] (8+1.2-0.5,-2+0.5) -- (8+1.2-0.5,-2-0.5) --
                    (8+1.2+0.5,-2-0.5) -- (8+1.2+0.5,-2+0.5);
\draw[fill=black] (8+1.2,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (8+2.4-0.5,-2+0.5) -- (8+2.4-0.5,-2-0.5) --
                    (8+2.4+0.5,-2-0.5) -- (8+2.4+0.5,-2+0.5);

    
\path[draw,thick,-] (8+3.6-0.5,-2+0.5) -- (8+3.6-0.5,-2-0.5) --
                    (8+3.6+0.5,-2-0.5) -- (8+3.6+0.5,-2+0.5);
\draw[fill=black] (8+3.6,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (8+4.8-0.5,-2+0.5) -- (8+4.8-0.5,-2-0.5) --
                    (8+4.8+0.5,-2-0.5) -- (8+4.8+0.5,-2+0.5);

    
\path[draw,thick,-] (8-0.5,-4+0.5) -- (8-0.5,-4-0.5) --
                    (8+0.5,-4-0.5) -- (8+0.5,-4+0.5);

    
\path[draw,thick,-] (8+1.2-0.5,-4+0.5) -- (8+1.2-0.5,-4-0.5) --
                    (8+1.2+0.5,-4-0.5) -- (8+1.2+0.5,-4+0.5);
\draw[fill=black] (8+1.2,-4-0.3) circle (0.15);

    
\path[draw,thick,-] (8+2.4-0.5,-4+0.5) -- (8+2.4-0.5,-4-0.5) --
                    (8+2.4+0.5,-4-0.5) -- (8+2.4+0.5,-4+0.5);

    
\path[draw,thick,-] (8+3.6-0.5,-4+0.5) -- (8+3.6-0.5,-4-0.5) --
                    (8+3.6+0.5,-4-0.5) -- (8+3.6+0.5,-4+0.5);

    
\path[draw,thick,-] (8+4.8-0.5,-4+0.5) -- (8+4.8-0.5,-4-0.5) --
                    (8+4.8+0.5,-4-0.5) -- (8+4.8+0.5,-4+0.5);
\draw[fill=black] (8+4.8,-4-0.3) circle (0.15);

    
\path[draw,thick,-] (16-0.5,0+0.5) -- (16-0.5,0-0.5) --
                    (16+0.5,0-0.5) -- (16+0.5,0+0.5);

    
\path[draw,thick,-] (16+1.2-0.5,0+0.5) -- (16+1.2-0.5,0-0.5) --
                    (16+1.2+0.5,0-0.5) -- (16+1.2+0.5,0+0.5);

    
\path[draw,thick,-] (16+2.4-0.5,0+0.5) -- (16+2.4-0.5,0-0.5) --
                    (16+2.4+0.5,0-0.5) -- (16+2.4+0.5,0+0.5);
\draw[fill=black] (16+2.4,0-0.3) circle (0.15);

    
\path[draw,thick,-] (16+3.6-0.5,0+0.5) -- (16+3.6-0.5,0-0.5) --
                    (16+3.6+0.5,0-0.5) -- (16+3.6+0.5,0+0.5);
\draw[fill=black] (16+3.6,0-0.3) circle (0.15);

    
\path[draw,thick,-] (16+4.8-0.5,0+0.5) -- (16+4.8-0.5,0-0.5) --
                    (16+4.8+0.5,0-0.5) -- (16+4.8+0.5,0+0.5);

    
\path[draw,thick,-] (16-0.5,-2+0.5) -- (16-0.5,-2-0.5) --
                    (16+0.5,-2-0.5) -- (16+0.5,-2+0.5);

    
\path[draw,thick,-] (16+1.2-0.5,-2+0.5) -- (16+1.2-0.5,-2-0.5) --
                    (16+1.2+0.5,-2-0.5) -- (16+1.2+0.5,-2+0.5);

    
\path[draw,thick,-] (16+2.4-0.5,-2+0.5) -- (16+2.4-0.5,-2-0.5) --
                    (16+2.4+0.5,-2-0.5) -- (16+2.4+0.5,-2+0.5);
\draw[fill=black] (16+2.4,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (16+3.6-0.5,-2+0.5) -- (16+3.6-0.5,-2-0.5) --
                    (16+3.6+0.5,-2-0.5) -- (16+3.6+0.5,-2+0.5);

    
\path[draw,thick,-] (16+4.8-0.5,-2+0.5) -- (16+4.8-0.5,-2-0.5) --
                    (16+4.8+0.5,-2-0.5) -- (16+4.8+0.5,-2+0.5);
\draw[fill=black] (16+4.8,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (16-0.5,-4+0.5) -- (16-0.5,-4-0.5) --
                    (16+0.5,-4-0.5) -- (16+0.5,-4+0.5);

    
\path[draw,thick,-] (16+1.2-0.5,-4+0.5) -- (16+1.2-0.5,-4-0.5) --
                    (16+1.2+0.5,-4-0.5) -- (16+1.2+0.5,-4+0.5);

    
\path[draw,thick,-] (16+2.4-0.5,-4+0.5) -- (16+2.4-0.5,-4-0.5) --
                    (16+2.4+0.5,-4-0.5) -- (16+2.4+0.5,-4+0.5);

    
\path[draw,thick,-] (16+3.6-0.5,-4+0.5) -- (16+3.6-0.5,-4-0.5) --
                    (16+3.6+0.5,-4-0.5) -- (16+3.6+0.5,-4+0.5);
\draw[fill=black] (16+3.6,-4-0.3) circle (0.15);

    
\path[draw,thick,-] (16+4.8-0.5,-4+0.5) -- (16+4.8-0.5,-4-0.5) --
                    (16+4.8+0.5,-4-0.5) -- (16+4.8+0.5,-4+0.5);
\draw[fill=black] (16+4.8,-4-0.3) circle (0.15);

\end{tikzpicture}
</script>

In this scenario, the answer is directly the
binomial coefficient ${n \choose k}$.

_Scenario 2_: A box can contain multiple balls.
For example, when $n=5$ and $k=2$,
there are 15 solutions:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.5]

    
\path[draw,thick,-] (0-0.5,0+0.5) -- (0-0.5,0-0.5) --
                    (0+0.5,0-0.5) -- (0+0.5,0+0.5);

\draw[fill=black] (0-0.2,0-0.3) circle (0.15);
\draw[fill=black] (0+0.2,0-0.3) circle (0.15);

    
\path[draw,thick,-] (0+1.2-0.5,0+0.5) -- (0+1.2-0.5,0-0.5) --
                    (0+1.2+0.5,0-0.5) -- (0+1.2+0.5,0+0.5);

    
\path[draw,thick,-] (0+2.4-0.5,0+0.5) -- (0+2.4-0.5,0-0.5) --
                    (0+2.4+0.5,0-0.5) -- (0+2.4+0.5,0+0.5);

    
\path[draw,thick,-] (0+3.6-0.5,0+0.5) -- (0+3.6-0.5,0-0.5) --
                    (0+3.6+0.5,0-0.5) -- (0+3.6+0.5,0+0.5);

    
\path[draw,thick,-] (0+4.8-0.5,0+0.5) -- (0+4.8-0.5,0-0.5) --
                    (0+4.8+0.5,0-0.5) -- (0+4.8+0.5,0+0.5);

    
\path[draw,thick,-] (0-0.5,-2+0.5) -- (0-0.5,-2-0.5) --
                    (0+0.5,-2-0.5) -- (0+0.5,-2+0.5);
\draw[fill=black] (0,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (0+1.2-0.5,-2+0.5) -- (0+1.2-0.5,-2-0.5) --
                    (0+1.2+0.5,-2-0.5) -- (0+1.2+0.5,-2+0.5);
\draw[fill=black] (0+1.2,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (0+2.4-0.5,-2+0.5) -- (0+2.4-0.5,-2-0.5) --
                    (0+2.4+0.5,-2-0.5) -- (0+2.4+0.5,-2+0.5);

    
\path[draw,thick,-] (0+3.6-0.5,-2+0.5) -- (0+3.6-0.5,-2-0.5) --
                    (0+3.6+0.5,-2-0.5) -- (0+3.6+0.5,-2+0.5);

    
\path[draw,thick,-] (0+4.8-0.5,-2+0.5) -- (0+4.8-0.5,-2-0.5) --
                    (0+4.8+0.5,-2-0.5) -- (0+4.8+0.5,-2+0.5);

    
\path[draw,thick,-] (0-0.5,-4+0.5) -- (0-0.5,-4-0.5) --
                    (0+0.5,-4-0.5) -- (0+0.5,-4+0.5);
\draw[fill=black] (0,-4-0.3) circle (0.15);

    
\path[draw,thick,-] (0+1.2-0.5,-4+0.5) -- (0+1.2-0.5,-4-0.5) --
                    (0+1.2+0.5,-4-0.5) -- (0+1.2+0.5,-4+0.5);

    
\path[draw,thick,-] (0+2.4-0.5,-4+0.5) -- (0+2.4-0.5,-4-0.5) --
                    (0+2.4+0.5,-4-0.5) -- (0+2.4+0.5,-4+0.5);
\draw[fill=black] (0+2.4,-4-0.3) circle (0.15);

    
\path[draw,thick,-] (0+3.6-0.5,-4+0.5) -- (0+3.6-0.5,-4-0.5) --
                    (0+3.6+0.5,-4-0.5) -- (0+3.6+0.5,-4+0.5);

    
\path[draw,thick,-] (0+4.8-0.5,-4+0.5) -- (0+4.8-0.5,-4-0.5) --
                    (0+4.8+0.5,-4-0.5) -- (0+4.8+0.5,-4+0.5);

    
\path[draw,thick,-] (0-0.5,-6+0.5) -- (0-0.5,-6-0.5) --
                    (0+0.5,-6-0.5) -- (0+0.5,-6+0.5);
\draw[fill=black] (0,-6-0.3) circle (0.15);

    
\path[draw,thick,-] (0+1.2-0.5,-6+0.5) -- (0+1.2-0.5,-6-0.5) --
                    (0+1.2+0.5,-6-0.5) -- (0+1.2+0.5,-6+0.5);

    
\path[draw,thick,-] (0+2.4-0.5,-6+0.5) -- (0+2.4-0.5,-6-0.5) --
                    (0+2.4+0.5,-6-0.5) -- (0+2.4+0.5,-6+0.5);

    
\path[draw,thick,-] (0+3.6-0.5,-6+0.5) -- (0+3.6-0.5,-6-0.5) --
                    (0+3.6+0.5,-6-0.5) -- (0+3.6+0.5,-6+0.5);
\draw[fill=black] (0+3.6,-6-0.3) circle (0.15);

    
\path[draw,thick,-] (0+4.8-0.5,-6+0.5) -- (0+4.8-0.5,-6-0.5) --
                    (0+4.8+0.5,-6-0.5) -- (0+4.8+0.5,-6+0.5);

    
\path[draw,thick,-] (0-0.5,-8+0.5) -- (0-0.5,-8-0.5) --
                    (0+0.5,-8-0.5) -- (0+0.5,-8+0.5);
\draw[fill=black] (0,-8-0.3) circle (0.15);

    
\path[draw,thick,-] (0+1.2-0.5,-8+0.5) -- (0+1.2-0.5,-8-0.5) --
                    (0+1.2+0.5,-8-0.5) -- (0+1.2+0.5,-8+0.5);

    
\path[draw,thick,-] (0+2.4-0.5,-8+0.5) -- (0+2.4-0.5,-8-0.5) --
                    (0+2.4+0.5,-8-0.5) -- (0+2.4+0.5,-8+0.5);

    
\path[draw,thick,-] (0+3.6-0.5,-8+0.5) -- (0+3.6-0.5,-8-0.5) --
                    (0+3.6+0.5,-8-0.5) -- (0+3.6+0.5,-8+0.5);

    
\path[draw,thick,-] (0+4.8-0.5,-8+0.5) -- (0+4.8-0.5,-8-0.5) --
                    (0+4.8+0.5,-8-0.5) -- (0+4.8+0.5,-8+0.5);
\draw[fill=black] (0+4.8,-8-0.3) circle (0.15);

    
\path[draw,thick,-] (8-0.5,0+0.5) -- (8-0.5,0-0.5) --
                    (8+0.5,0-0.5) -- (8+0.5,0+0.5);

    
\path[draw,thick,-] (8+1.2-0.5,0+0.5) -- (8+1.2-0.5,0-0.5) --
                    (8+1.2+0.5,0-0.5) -- (8+1.2+0.5,0+0.5);

\draw[fill=black] (8+1.2-0.2,0-0.3) circle (0.15);
\draw[fill=black] (8+1.2+0.2,0-0.3) circle (0.15);

    
\path[draw,thick,-] (8+2.4-0.5,0+0.5) -- (8+2.4-0.5,0-0.5) --
                    (8+2.4+0.5,0-0.5) -- (8+2.4+0.5,0+0.5);

    
\path[draw,thick,-] (8+3.6-0.5,0+0.5) -- (8+3.6-0.5,0-0.5) --
                    (8+3.6+0.5,0-0.5) -- (8+3.6+0.5,0+0.5);

    
\path[draw,thick,-] (8+4.8-0.5,0+0.5) -- (8+4.8-0.5,0-0.5) --
                    (8+4.8+0.5,0-0.5) -- (8+4.8+0.5,0+0.5);

    
\path[draw,thick,-] (8-0.5,-2+0.5) -- (8-0.5,-2-0.5) --
                    (8+0.5,-2-0.5) -- (8+0.5,-2+0.5);

    
\path[draw,thick,-] (8+1.2-0.5,-2+0.5) -- (8+1.2-0.5,-2-0.5) --
                    (8+1.2+0.5,-2-0.5) -- (8+1.2+0.5,-2+0.5);
\draw[fill=black] (8+1.2,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (8+2.4-0.5,-2+0.5) -- (8+2.4-0.5,-2-0.5) --
                    (8+2.4+0.5,-2-0.5) -- (8+2.4+0.5,-2+0.5);
\draw[fill=black] (8+2.4,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (8+3.6-0.5,-2+0.5) -- (8+3.6-0.5,-2-0.5) --
                    (8+3.6+0.5,-2-0.5) -- (8+3.6+0.5,-2+0.5);

    
\path[draw,thick,-] (8+4.8-0.5,-2+0.5) -- (8+4.8-0.5,-2-0.5) --
                    (8+4.8+0.5,-2-0.5) -- (8+4.8+0.5,-2+0.5);

    
\path[draw,thick,-] (8-0.5,-4+0.5) -- (8-0.5,-4-0.5) --
                    (8+0.5,-4-0.5) -- (8+0.5,-4+0.5);

    
\path[draw,thick,-] (8+1.2-0.5,-4+0.5) -- (8+1.2-0.5,-4-0.5) --
                    (8+1.2+0.5,-4-0.5) -- (8+1.2+0.5,-4+0.5);
\draw[fill=black] (8+1.2,-4-0.3) circle (0.15);

    
\path[draw,thick,-] (8+2.4-0.5,-4+0.5) -- (8+2.4-0.5,-4-0.5) --
                    (8+2.4+0.5,-4-0.5) -- (8+2.4+0.5,-4+0.5);

    
\path[draw,thick,-] (8+3.6-0.5,-4+0.5) -- (8+3.6-0.5,-4-0.5) --
                    (8+3.6+0.5,-4-0.5) -- (8+3.6+0.5,-4+0.5);
\draw[fill=black] (8+3.6,-4-0.3) circle (0.15);

    
\path[draw,thick,-] (8+4.8-0.5,-4+0.5) -- (8+4.8-0.5,-4-0.5) --
                    (8+4.8+0.5,-4-0.5) -- (8+4.8+0.5,-4+0.5);

    
\path[draw,thick,-] (8-0.5,-6+0.5) -- (8-0.5,-6-0.5) --
                    (8+0.5,-6-0.5) -- (8+0.5,-6+0.5);

    
\path[draw,thick,-] (8+1.2-0.5,-6+0.5) -- (8+1.2-0.5,-6-0.5) --
                    (8+1.2+0.5,-6-0.5) -- (8+1.2+0.5,-6+0.5);
\draw[fill=black] (8+1.2,-6-0.3) circle (0.15);

    
\path[draw,thick,-] (8+2.4-0.5,-6+0.5) -- (8+2.4-0.5,-6-0.5) --
                    (8+2.4+0.5,-6-0.5) -- (8+2.4+0.5,-6+0.5);

    
\path[draw,thick,-] (8+3.6-0.5,-6+0.5) -- (8+3.6-0.5,-6-0.5) --
                    (8+3.6+0.5,-6-0.5) -- (8+3.6+0.5,-6+0.5);

    
\path[draw,thick,-] (8+4.8-0.5,-6+0.5) -- (8+4.8-0.5,-6-0.5) --
                    (8+4.8+0.5,-6-0.5) -- (8+4.8+0.5,-6+0.5);
\draw[fill=black] (8+4.8,-6-0.3) circle (0.15);

    
\path[draw,thick,-] (8-0.5,-8+0.5) -- (8-0.5,-8-0.5) --
                    (8+0.5,-8-0.5) -- (8+0.5,-8+0.5);

    
\path[draw,thick,-] (8+1.2-0.5,-8+0.5) -- (8+1.2-0.5,-8-0.5) --
                    (8+1.2+0.5,-8-0.5) -- (8+1.2+0.5,-8+0.5);

    
\path[draw,thick,-] (8+2.4-0.5,-8+0.5) -- (8+2.4-0.5,-8-0.5) --
                    (8+2.4+0.5,-8-0.5) -- (8+2.4+0.5,-8+0.5);

\draw[fill=black] (8+2.4-0.2,-8-0.3) circle (0.15);
\draw[fill=black] (8+2.4+0.2,-8-0.3) circle (0.15);

    
\path[draw,thick,-] (8+3.6-0.5,-8+0.5) -- (8+3.6-0.5,-8-0.5) --
                    (8+3.6+0.5,-8-0.5) -- (8+3.6+0.5,-8+0.5);

    
\path[draw,thick,-] (8+4.8-0.5,-8+0.5) -- (8+4.8-0.5,-8-0.5) --
                    (8+4.8+0.5,-8-0.5) -- (8+4.8+0.5,-8+0.5);

    
\path[draw,thick,-] (16-0.5,0+0.5) -- (16-0.5,0-0.5) --
                    (16+0.5,0-0.5) -- (16+0.5,0+0.5);

    
\path[draw,thick,-] (16+1.2-0.5,0+0.5) -- (16+1.2-0.5,0-0.5) --
                    (16+1.2+0.5,0-0.5) -- (16+1.2+0.5,0+0.5);

    
\path[draw,thick,-] (16+2.4-0.5,0+0.5) -- (16+2.4-0.5,0-0.5) --
                    (16+2.4+0.5,0-0.5) -- (16+2.4+0.5,0+0.5);
\draw[fill=black] (16+2.4,0-0.3) circle (0.15);

    
\path[draw,thick,-] (16+3.6-0.5,0+0.5) -- (16+3.6-0.5,0-0.5) --
                    (16+3.6+0.5,0-0.5) -- (16+3.6+0.5,0+0.5);
\draw[fill=black] (16+3.6,0-0.3) circle (0.15);

    
\path[draw,thick,-] (16+4.8-0.5,0+0.5) -- (16+4.8-0.5,0-0.5) --
                    (16+4.8+0.5,0-0.5) -- (16+4.8+0.5,0+0.5);

    
\path[draw,thick,-] (16-0.5,-2+0.5) -- (16-0.5,-2-0.5) --
                    (16+0.5,-2-0.5) -- (16+0.5,-2+0.5);

    
\path[draw,thick,-] (16+1.2-0.5,-2+0.5) -- (16+1.2-0.5,-2-0.5) --
                    (16+1.2+0.5,-2-0.5) -- (16+1.2+0.5,-2+0.5);

    
\path[draw,thick,-] (16+2.4-0.5,-2+0.5) -- (16+2.4-0.5,-2-0.5) --
                    (16+2.4+0.5,-2-0.5) -- (16+2.4+0.5,-2+0.5);
\draw[fill=black] (16+2.4,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (16+3.6-0.5,-2+0.5) -- (16+3.6-0.5,-2-0.5) --
                    (16+3.6+0.5,-2-0.5) -- (16+3.6+0.5,-2+0.5);

    
\path[draw,thick,-] (16+4.8-0.5,-2+0.5) -- (16+4.8-0.5,-2-0.5) --
                    (16+4.8+0.5,-2-0.5) -- (16+4.8+0.5,-2+0.5);
\draw[fill=black] (16+4.8,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (16-0.5,-4+0.5) -- (16-0.5,-4-0.5) --
                    (16+0.5,-4-0.5) -- (16+0.5,-4+0.5);

    
\path[draw,thick,-] (16+1.2-0.5,-4+0.5) -- (16+1.2-0.5,-4-0.5) --
                    (16+1.2+0.5,-4-0.5) -- (16+1.2+0.5,-4+0.5);

    
\path[draw,thick,-] (16+2.4-0.5,-4+0.5) -- (16+2.4-0.5,-4-0.5) --
                    (16+2.4+0.5,-4-0.5) -- (16+2.4+0.5,-4+0.5);

    
\path[draw,thick,-] (16+3.6-0.5,-4+0.5) -- (16+3.6-0.5,-4-0.5) --
                    (16+3.6+0.5,-4-0.5) -- (16+3.6+0.5,-4+0.5);

\draw[fill=black] (16+3.6-0.2,-4-0.3) circle (0.15);
\draw[fill=black] (16+3.6+0.2,-4-0.3) circle (0.15);

    
\path[draw,thick,-] (16+4.8-0.5,-4+0.5) -- (16+4.8-0.5,-4-0.5) --
                    (16+4.8+0.5,-4-0.5) -- (16+4.8+0.5,-4+0.5);

    
\path[draw,thick,-] (16-0.5,-6+0.5) -- (16-0.5,-6-0.5) --
                    (16+0.5,-6-0.5) -- (16+0.5,-6+0.5);

    
\path[draw,thick,-] (16+1.2-0.5,-6+0.5) -- (16+1.2-0.5,-6-0.5) --
                    (16+1.2+0.5,-6-0.5) -- (16+1.2+0.5,-6+0.5);

    
\path[draw,thick,-] (16+2.4-0.5,-6+0.5) -- (16+2.4-0.5,-6-0.5) --
                    (16+2.4+0.5,-6-0.5) -- (16+2.4+0.5,-6+0.5);

    
\path[draw,thick,-] (16+3.6-0.5,-6+0.5) -- (16+3.6-0.5,-6-0.5) --
                    (16+3.6+0.5,-6-0.5) -- (16+3.6+0.5,-6+0.5);
\draw[fill=black] (16+3.6,-6-0.3) circle (0.15);

    
\path[draw,thick,-] (16+4.8-0.5,-6+0.5) -- (16+4.8-0.5,-6-0.5) --
                    (16+4.8+0.5,-6-0.5) -- (16+4.8+0.5,-6+0.5);
\draw[fill=black] (16+4.8,-6-0.3) circle (0.15);

    
\path[draw,thick,-] (16-0.5,-8+0.5) -- (16-0.5,-8-0.5) --
                    (16+0.5,-8-0.5) -- (16+0.5,-8+0.5);

    
\path[draw,thick,-] (16+1.2-0.5,-8+0.5) -- (16+1.2-0.5,-8-0.5) --
                    (16+1.2+0.5,-8-0.5) -- (16+1.2+0.5,-8+0.5);

    
\path[draw,thick,-] (16+2.4-0.5,-8+0.5) -- (16+2.4-0.5,-8-0.5) --
                    (16+2.4+0.5,-8-0.5) -- (16+2.4+0.5,-8+0.5);

    
\path[draw,thick,-] (16+3.6-0.5,-8+0.5) -- (16+3.6-0.5,-8-0.5) --
                    (16+3.6+0.5,-8-0.5) -- (16+3.6+0.5,-8+0.5);

    
\path[draw,thick,-] (16+4.8-0.5,-8+0.5) -- (16+4.8-0.5,-8-0.5) --
                    (16+4.8+0.5,-8-0.5) -- (16+4.8+0.5,-8+0.5);

\draw[fill=black] (16+4.8-0.2,-8-0.3) circle (0.15);
\draw[fill=black] (16+4.8+0.2,-8-0.3) circle (0.15);

\end{tikzpicture}
</script>

The process of placing the balls in the boxes
can be represented as a string
that consists of symbols
''o'' and ''$\rightarrow$''.
Initially, assume that we are standing at the leftmost box.
The symbol ''o'' means that we place a ball
in the current box, and the symbol
''$\rightarrow$'' means that we move to
the next box to the right.

Using this notation, each solution is a string
that contains $k$ times the symbol ''o'' and
$n-1$ times the symbol ''$\rightarrow$''.
For example, the upper-right solution
in the above picture corresponds to the string
''$\rightarrow$ $\rightarrow$ o $\rightarrow$ o $\rightarrow$''.
Thus, the number of solutions is
${k+n-1 \choose k}$.

_Scenario 3_: Each box may contain at most one ball,
and in addition, no two adjacent boxes may both contain a ball.
For example, when $n=5$ and $k=2$,
there are 6 solutions:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.5]

    
\path[draw,thick,-] (0-0.5,0+0.5) -- (0-0.5,0-0.5) --
                    (0+0.5,0-0.5) -- (0+0.5,0+0.5);
\draw[fill=black] (0,0-0.3) circle (0.15);

    
\path[draw,thick,-] (0+1.2-0.5,0+0.5) -- (0+1.2-0.5,0-0.5) --
                    (0+1.2+0.5,0-0.5) -- (0+1.2+0.5,0+0.5);

    
\path[draw,thick,-] (0+2.4-0.5,0+0.5) -- (0+2.4-0.5,0-0.5) --
                    (0+2.4+0.5,0-0.5) -- (0+2.4+0.5,0+0.5);
\draw[fill=black] (0+2.4,0-0.3) circle (0.15);

    
\path[draw,thick,-] (0+3.6-0.5,0+0.5) -- (0+3.6-0.5,0-0.5) --
                    (0+3.6+0.5,0-0.5) -- (0+3.6+0.5,0+0.5);

    
\path[draw,thick,-] (0+4.8-0.5,0+0.5) -- (0+4.8-0.5,0-0.5) --
                    (0+4.8+0.5,0-0.5) -- (0+4.8+0.5,0+0.5);

    
\path[draw,thick,-] (0-0.5,-2+0.5) -- (0-0.5,-2-0.5) --
                    (0+0.5,-2-0.5) -- (0+0.5,-2+0.5);
\draw[fill=black] (0,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (0+1.2-0.5,-2+0.5) -- (0+1.2-0.5,-2-0.5) --
                    (0+1.2+0.5,-2-0.5) -- (0+1.2+0.5,-2+0.5);

    
\path[draw,thick,-] (0+2.4-0.5,-2+0.5) -- (0+2.4-0.5,-2-0.5) --
                    (0+2.4+0.5,-2-0.5) -- (0+2.4+0.5,-2+0.5);

    
\path[draw,thick,-] (0+3.6-0.5,-2+0.5) -- (0+3.6-0.5,-2-0.5) --
                    (0+3.6+0.5,-2-0.5) -- (0+3.6+0.5,-2+0.5);
\draw[fill=black] (0+3.6,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (0+4.8-0.5,-2+0.5) -- (0+4.8-0.5,-2-0.5) --
                    (0+4.8+0.5,-2-0.5) -- (0+4.8+0.5,-2+0.5);

    
\path[draw,thick,-] (8-0.5,0+0.5) -- (8-0.5,0-0.5) --
                    (8+0.5,0-0.5) -- (8+0.5,0+0.5);
\draw[fill=black] (8,0-0.3) circle (0.15);

    
\path[draw,thick,-] (8+1.2-0.5,0+0.5) -- (8+1.2-0.5,0-0.5) --
                    (8+1.2+0.5,0-0.5) -- (8+1.2+0.5,0+0.5);

    
\path[draw,thick,-] (8+2.4-0.5,0+0.5) -- (8+2.4-0.5,0-0.5) --
                    (8+2.4+0.5,0-0.5) -- (8+2.4+0.5,0+0.5);

    
\path[draw,thick,-] (8+3.6-0.5,0+0.5) -- (8+3.6-0.5,0-0.5) --
                    (8+3.6+0.5,0-0.5) -- (8+3.6+0.5,0+0.5);

    
\path[draw,thick,-] (8+4.8-0.5,0+0.5) -- (8+4.8-0.5,0-0.5) --
                    (8+4.8+0.5,0-0.5) -- (8+4.8+0.5,0+0.5);
\draw[fill=black] (8+4.8,0-0.3) circle (0.15);

    
\path[draw,thick,-] (8-0.5,-2+0.5) -- (8-0.5,-2-0.5) --
                    (8+0.5,-2-0.5) -- (8+0.5,-2+0.5);

    
\path[draw,thick,-] (8+1.2-0.5,-2+0.5) -- (8+1.2-0.5,-2-0.5) --
                    (8+1.2+0.5,-2-0.5) -- (8+1.2+0.5,-2+0.5);
\draw[fill=black] (8+1.2,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (8+2.4-0.5,-2+0.5) -- (8+2.4-0.5,-2-0.5) --
                    (8+2.4+0.5,-2-0.5) -- (8+2.4+0.5,-2+0.5);

    
\path[draw,thick,-] (8+3.6-0.5,-2+0.5) -- (8+3.6-0.5,-2-0.5) --
                    (8+3.6+0.5,-2-0.5) -- (8+3.6+0.5,-2+0.5);
\draw[fill=black] (8+3.6,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (8+4.8-0.5,-2+0.5) -- (8+4.8-0.5,-2-0.5) --
                    (8+4.8+0.5,-2-0.5) -- (8+4.8+0.5,-2+0.5);

    
\path[draw,thick,-] (16-0.5,0+0.5) -- (16-0.5,0-0.5) --
                    (16+0.5,0-0.5) -- (16+0.5,0+0.5);

    
\path[draw,thick,-] (16+1.2-0.5,0+0.5) -- (16+1.2-0.5,0-0.5) --
                    (16+1.2+0.5,0-0.5) -- (16+1.2+0.5,0+0.5);
\draw[fill=black] (16+1.2,0-0.3) circle (0.15);

    
\path[draw,thick,-] (16+2.4-0.5,0+0.5) -- (16+2.4-0.5,0-0.5) --
                    (16+2.4+0.5,0-0.5) -- (16+2.4+0.5,0+0.5);

    
\path[draw,thick,-] (16+3.6-0.5,0+0.5) -- (16+3.6-0.5,0-0.5) --
                    (16+3.6+0.5,0-0.5) -- (16+3.6+0.5,0+0.5);

    
\path[draw,thick,-] (16+4.8-0.5,0+0.5) -- (16+4.8-0.5,0-0.5) --
                    (16+4.8+0.5,0-0.5) -- (16+4.8+0.5,0+0.5);
\draw[fill=black] (16+4.8,0-0.3) circle (0.15);

    
\path[draw,thick,-] (16-0.5,-2+0.5) -- (16-0.5,-2-0.5) --
                    (16+0.5,-2-0.5) -- (16+0.5,-2+0.5);

    
\path[draw,thick,-] (16+1.2-0.5,-2+0.5) -- (16+1.2-0.5,-2-0.5) --
                    (16+1.2+0.5,-2-0.5) -- (16+1.2+0.5,-2+0.5);

    
\path[draw,thick,-] (16+2.4-0.5,-2+0.5) -- (16+2.4-0.5,-2-0.5) --
                    (16+2.4+0.5,-2-0.5) -- (16+2.4+0.5,-2+0.5);
\draw[fill=black] (16+2.4,-2-0.3) circle (0.15);

    
\path[draw,thick,-] (16+3.6-0.5,-2+0.5) -- (16+3.6-0.5,-2-0.5) --
                    (16+3.6+0.5,-2-0.5) -- (16+3.6+0.5,-2+0.5);

    
\path[draw,thick,-] (16+4.8-0.5,-2+0.5) -- (16+4.8-0.5,-2-0.5) --
                    (16+4.8+0.5,-2-0.5) -- (16+4.8+0.5,-2+0.5);
\draw[fill=black] (16+4.8,-2-0.3) circle (0.15);

\end{tikzpicture}
</script>

In this scenario, we can assume that
$k$ balls are initially placed in boxes
and there is an empty box between each
two adjacent boxes.
The remaining task is to choose the
positions for the remaining empty boxes.
There are $n-2k+1$ such boxes and
$k+1$ positions for them.
Thus, using the formula of scenario 2,
the number of solutions is
${n-k+1 \choose n-2k+1}$.

## Multinomial coefficients

The **multinomial coefficient**
\\[
{n \\choose k_1,k_2,\\ldots,k_m} = \\frac{n!}{k_1! k_2! \\cdots k_m!},
\\]
equals the number of ways
we can divide $n$ elements into subsets
of sizes $k_1,k_2,\ldots,k_m$,
where $k_1+k_2+\cdots+k_m=n$.
Multinomial coefficients can be seen as a
generalization of binomial cofficients;
if $m=2$, the above formula
corresponds to the binomial coefficient formula.
