# Linear recurrences

A **linear recurrence**
is a function $f(n)$
whose initial values are
$f(0),f(1),\ldots,f(k-1)$
and larger values
are calculated recursively using the formula
\\[
f(n) = c_1 f(n-1) + c_2 f(n-2) + \\ldots + c_k f (n-k),
\\]
where $c_1,c_2,\ldots,c_k$ are constant coefficients.

Dynamic programming can be used to calculate
any value of $f(n)$ in $O(kn)$ time by calculating
all values of $f(0),f(1),\ldots,f(n)$ one after another.
However, if $k$ is small, it is possible to calculate
$f(n)$ much more efficiently in $O(k^3 \log n)$
time using matrix operations.

## Fibonacci numbers

A simple example of a linear recurrence is the
following function that defines the Fibonacci numbers:
\\[
\\begin{array}{lcl}
f(0) & = & 0 \\\\
f(1) & = & 1 \\\\
f(n) & = & f(n-1)+f(n-2) \\\\
\\end{array}
\\]
In this case, $k=2$ and $c_1=c_2=1$.

To efficiently calculate Fibonacci numbers,
we represent the
Fibonacci formula as a
square matrix $X$ of size $2 \times 2$,
for which the following holds:
\\[
X \\cdot
 \\begin{bmatrix}
  f(i) \\\\
  f(i+1) \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  f(i+1) \\\\
  f(i+2) \\\\
 \\end{bmatrix}
\\]
Thus, values $f(i)$ and $f(i+1)$ are given as
''input'' for $X$,
and $X$ calculates values $f(i+1)$ and $f(i+2)$
from them.
It turns out that such a matrix is

\\[
X = 
 \\begin{bmatrix}
  0 & 1 \\\\
  1 & 1 \\\\
 \\end{bmatrix}.
\\]

\noindent
For example,
\\[
\\begin{bmatrix}
  0 & 1 \\\\
  1 & 1 \\\\
 \\end{bmatrix}
\\cdot
 \\begin{bmatrix}
  f(5) \\\\
  f(6) \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  0 & 1 \\\\
  1 & 1 \\\\
 \\end{bmatrix}
\\cdot
 \\begin{bmatrix}
  5 \\\\
  8 \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  8 \\\\
  13 \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  f(6) \\\\
  f(7) \\\\
 \\end{bmatrix}.
\\]
Thus, we can calculate $f(n)$ using the formula
\\[
\\begin{bmatrix}
  f(n) \\\\
  f(n+1) \\\\
 \\end{bmatrix} =
X^n \\cdot
 \\begin{bmatrix}
  f(0) \\\\
  f(1) \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  0 & 1 \\\\
  1 & 1 \\\\
 \\end{bmatrix}^n
\\cdot
 \\begin{bmatrix}
  0 \\\\
  1 \\\\
 \\end{bmatrix}.
\\]
The value of $X^n$ can be calculated in
$O(\log n)$ time,
so the value of $f(n)$ can also be calculated
in $O(\log n)$ time. Reusing `mul` and
`mat_pow` from the previous section, the $n$th Fibonacci number is:

```rust
# fn mul(a: &[Vec<i64>], b: &[Vec<i64>]) -> Vec<Vec<i64>> {
#     let (n, m) = (a.len(), b[0].len());
#     let mut c = vec![vec![0i64; m]; n];
#     for i in 0..n { for k in 0..b.len() { for j in 0..m {
#         c[i][j] += a[i][k] * b[k][j];
#     } } }
#     c
# }
# fn mat_pow(a: &[Vec<i64>], k: u64) -> Vec<Vec<i64>> {
#     let n = a.len();
#     let mut r: Vec<Vec<i64>> = (0..n)
#         .map(|i| (0..n).map(|j| if i == j {1} else {0}).collect())
#         .collect();
#     let (mut b, mut k) = (a.to_vec(), k);
#     while k > 0 {
#         if k % 2 == 1 { r = mul(&r, &b); }
#         b = mul(&b, &b);
#         k /= 2;
#     }
#     r
# }
fn fib(n: u64) -> i64 {
    let x = vec![vec![0, 1],
                 vec![1, 1]];
    // the first row of X^n holds f(n) and f(n+1)
    mat_pow(&x, n)[0][1]
}
# println!("f(10) = {}", fib(10));
# println!("f(0..10) = {:?}", (0..10).map(fib).collect::<Vec<_>>());
```

Note that $f(n)$ grows exponentially, so an `i64` overflows just past
$n = 92$; a real solution computes the entries modulo a prime.

## General case

Let us now consider the general case where
$f(n)$ is any linear recurrence.
Again, our goal is to construct a matrix $X$
for which

\\[
X \\cdot
 \\begin{bmatrix}
  f(i) \\\\
  f(i+1) \\\\
  \\vdots \\\\
  f(i+k-1) \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  f(i+1) \\\\
  f(i+2) \\\\
  \\vdots \\\\
  f(i+k) \\\\
 \\end{bmatrix}.
\\]
Such a matrix is
\\[
X =
 \\begin{bmatrix}
  0 & 1 & 0 & 0 & \\cdots & 0 \\\\
  0 & 0 & 1 & 0 & \\cdots & 0 \\\\
  0 & 0 & 0 & 1 & \\cdots & 0 \\\\
  \\vdots & \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
  0 & 0 & 0 & 0 & \\cdots & 1 \\\\
  c_k & c_{k-1} & c_{k-2} & c_{k-3} & \\cdots & c_1 \\\\
 \\end{bmatrix}.
\\]
In the first $k-1$ rows, each element is 0
except that one element is 1.
These rows replace $f(i)$ with $f(i+1)$,
$f(i+1)$ with $f(i+2)$, and so on.
The last row contains the coefficients of the recurrence
to calculate the new value $f(i+k)$.

Now, $f(n)$ can be calculated in
$O(k^3 \log n)$ time using the formula
\\[
\\begin{bmatrix}
  f(n) \\\\
  f(n+1) \\\\
  \\vdots \\\\
  f(n+k-1) \\\\
 \\end{bmatrix} =
X^n \\cdot
 \\begin{bmatrix}
  f(0) \\\\
  f(1) \\\\
  \\vdots \\\\
  f(k-1) \\\\
 \\end{bmatrix}.
\\]
