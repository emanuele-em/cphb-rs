# Operations

The sum $A+B$ of matrices $A$ and $B$
is defined if the matrices are of the same size.
The result is a matrix where each element
is the sum of the corresponding elements
in $A$ and $B$.

For example,
\\[
\\begin{bmatrix}
  6 & 1 & 4 \\\\
  3 & 9 & 2 \\\\
 \\end{bmatrix} +
 \\begin{bmatrix}
  4 & 9 & 3 \\\\
  8 & 1 & 3 \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  6+4 & 1+9 & 4+3 \\\\
  3+8 & 9+1 & 2+3 \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  10 & 10 & 7 \\\\
  11 & 10 & 5 \\\\
 \\end{bmatrix}.
\\]

Multiplying a matrix $A$ by a value $x$ means
that each element of $A$ is multiplied by $x$.
For example,
\\[
2 \\cdot \\begin{bmatrix}
  6 & 1 & 4 \\\\
  3 & 9 & 2 \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  2 \\cdot 6 & 2\\cdot1 & 2\\cdot4 \\\\
  2\\cdot3 & 2\\cdot9 & 2\\cdot2 \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  12 & 2 & 8 \\\\
  6 & 18 & 4 \\\\
 \\end{bmatrix}.
\\]

## Matrix multiplication

The product $AB$ of matrices $A$ and $B$
is defined if $A$ is of size $a \times n$
and $B$ is of size $n \times b$, i.e.,
the width of $A$ equals the height of $B$.
The result is a matrix of size $a \times b$
whose elements are calculated using the formula
\\[
AB[i,j] = \\sum_{k=1}^n A[i,k] \\cdot B[k,j].
\\]

The idea is that each element of $AB$
is a sum of products of elements of $A$ and $B$
according to the following picture:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.5]
\draw (0,0) grid (4,3);
\draw (5,0) grid (10,3);
\draw (5,4) grid (10,8);

\node at (2,-1) {$A$};
\node at (7.5,-1) {$AB$};
\node at (11,6) {$B$};

\draw[thick,->,red,line width=2pt] (0,1.5) -- (4,1.5);
\draw[thick,->,red,line width=2pt] (6.5,8) -- (6.5,4);
\draw[thick,red,line width=2pt] (6.5,1.5) circle (0.4);
\end{tikzpicture}
</script>

For example,

\\[
\\begin{bmatrix}
  1 & 4 \\\\
  3 & 9 \\\\
  8 & 6 \\\\
 \\end{bmatrix}
\\cdot
 \\begin{bmatrix}
  1 & 6 \\\\
  2 & 9 \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  1 \\cdot 1 + 4 \\cdot 2 & 1 \\cdot 6 + 4 \\cdot 9 \\\\
  3 \\cdot 1 + 9 \\cdot 2 & 3 \\cdot 6 + 9 \\cdot 9 \\\\
  8 \\cdot 1 + 6 \\cdot 2 & 8 \\cdot 6 + 6 \\cdot 9 \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  9 & 42 \\\\
  21 & 99 \\\\
  20 & 102 \\\\
 \\end{bmatrix}.
\\]

Matrix multiplication is associative,
so $A(BC)=(AB)C$ holds,
but it is not commutative,
so $AB = BA$ does not usually hold.

An **identity matrix** is a square matrix
where each element on the diagonal is 1
and all other elements are 0.
For example, the following matrix
is the $3 \times 3$ identity matrix:
\\[
I = \\begin{bmatrix}
  1 & 0 & 0 \\\\
  0 & 1 & 0 \\\\
  0 & 0 & 1 \\\\
 \\end{bmatrix}
\\]

Multiplying a matrix by an identity matrix
does not change it. For example,
\\[
\\begin{bmatrix}
  1 & 0 & 0 \\\\
  0 & 1 & 0 \\\\
  0 & 0 & 1 \\\\
 \\end{bmatrix}
\\cdot
 \\begin{bmatrix}
  1 & 4 \\\\
  3 & 9 \\\\
  8 & 6 \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  1 & 4 \\\\
  3 & 9 \\\\
  8 & 6 \\\\
 \\end{bmatrix} \\hspace{10px} \\textrm{and} \\hspace{10px}
 \\begin{bmatrix}
  1 & 4 \\\\
  3 & 9 \\\\
  8 & 6 \\\\
 \\end{bmatrix}
\\cdot
 \\begin{bmatrix}
  1 & 0 \\\\
  0 & 1 \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  1 & 4 \\\\
  3 & 9 \\\\
  8 & 6 \\\\
 \\end{bmatrix}.
\\]

Using a straightforward algorithm,
we can calculate the product of
two $n \times n$ matrices
in $O(n^3)$ time.
There are also more efficient algorithms
for matrix multiplication[^1],
but they are mostly of theoretical interest
and such algorithms are not necessary
in competitive programming.

## Matrix power

The power $A^k$ of a matrix $A$ is defined
if $A$ is a square matrix.
The definition is based on matrix multiplication:
\\[
A^k = \\underbrace{A \\cdot A \\cdot A \\cdots A}_{\\textrm{$k$ times}}
\\]
For example,

\\[
\\begin{bmatrix}
  2 & 5 \\\\
  1 & 4 \\\\
 \\end{bmatrix}^3 =
 \\begin{bmatrix}
  2 & 5 \\\\
  1 & 4 \\\\
 \\end{bmatrix} \\cdot
 \\begin{bmatrix}
  2 & 5 \\\\
  1 & 4 \\\\
 \\end{bmatrix} \\cdot
 \\begin{bmatrix}
  2 & 5 \\\\
  1 & 4 \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  48 & 165 \\\\
  33 & 114 \\\\
 \\end{bmatrix}.
\\]
In addition, $A^0$ is an identity matrix. For example,
\\[
\\begin{bmatrix}
  2 & 5 \\\\
  1 & 4 \\\\
 \\end{bmatrix}^0 =
 \\begin{bmatrix}
  1 & 0 \\\\
  0 & 1 \\\\
 \\end{bmatrix}.
\\]

The matrix $A^k$ can be efficiently calculated
in $O(n^3 \log k)$ time using the
algorithm in Chapter 21.2. Multiplication and
exponentiation can be written as follows, representing a matrix simply as
a `Vec<Vec<i64>>` so that the size is a runtime value:

```rust
fn mul(a: &[Vec<i64>], b: &[Vec<i64>]) -> Vec<Vec<i64>> {
    let (n, m) = (a.len(), b[0].len());
    let mut c = vec![vec![0i64; m]; n];
    for i in 0..n {
        for k in 0..b.len() {
            for j in 0..m {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    c
}

fn mat_pow(a: &[Vec<i64>], k: u64) -> Vec<Vec<i64>> {
    let n = a.len();
    // start from the identity matrix, so that k = 0 gives it back
    let mut r: Vec<Vec<i64>> = (0..n)
        .map(|i| (0..n).map(|j| if i == j {1} else {0}).collect())
        .collect();
    let (mut b, mut k) = (a.to_vec(), k);
    while k > 0 {
        if k % 2 == 1 { r = mul(&r, &b); }
        b = mul(&b, &b);
        k /= 2;
    }
    r
}
# let a = vec![vec![2,5], vec![1,4]];
# println!("A^3 = {:?}", mat_pow(&a, 3));
```

The `while` loop squares the matrix and keeps the factors matching the
set bits of $k$, exactly like the `modpow` function of Chapter 21.2, so
only $O(\log k)$ multiplications are performed. For example,
\\[
\\begin{bmatrix}
  2 & 5 \\\\
  1 & 4 \\\\
 \\end{bmatrix}^8 =
 \\begin{bmatrix}
  2 & 5 \\\\
  1 & 4 \\\\
 \\end{bmatrix}^4 \\cdot
 \\begin{bmatrix}
  2 & 5 \\\\
  1 & 4 \\\\
 \\end{bmatrix}^4.
\\]

## Determinant

The **determinant** $\det(A)$ of a matrix $A$
is defined if $A$ is a square matrix.
If $A$ is of size $1 \times 1$,
then $\det(A)=A[1,1]$.
The determinant of a larger matrix is
calculated recursively using the formula 
\\[
\\det(A)=\\sum_{j=1}^n A[1,j] C[1,j],
\\]
where $C[i,j]$ is the **cofactor** of $A$
at $[i,j]$.
The cofactor is calculated using the formula
\\[
C[i,j] = (-1)^{i+j} \\det(M[i,j]),
\\]
where $M[i,j]$ is obtained by removing
row $i$ and column $j$ from $A$.
Due to the coefficient $(-1)^{i+j}$ in the cofactor,
every other determinant is positive
and negative.
For example,
\\[
\\det(
 \\begin{bmatrix}
  3 & 4 \\\\
  1 & 6 \\\\
 \\end{bmatrix}
) = 3 \\cdot 6 - 4 \\cdot 1 = 14
\\]
and
\\[
\\det(
 \\begin{bmatrix}
  2 & 4 & 3 \\\\
  5 & 1 & 6 \\\\
  7 & 2 & 4 \\\\
 \\end{bmatrix}
) = 
2 \\cdot
\\det(
 \\begin{bmatrix}
  1 & 6 \\\\
  2 & 4 \\\\
 \\end{bmatrix}
)
-4 \\cdot
\\det(
 \\begin{bmatrix}
  5 & 6 \\\\
  7 & 4 \\\\
 \\end{bmatrix}
)
+3 \\cdot
\\det(
 \\begin{bmatrix}
  5 & 1 \\\\
  7 & 2 \\\\
 \\end{bmatrix}
) = 81.
\\]

The determinant of $A$ tells us
whether there is an **inverse matrix**
$A^{-1}$ such that $A \cdot A^{-1} = I$,
where $I$ is an identity matrix.
It turns out that $A^{-1}$ exists
exactly when $\det(A) \neq 0$,
and it can be calculated using the formula

\\[
A^{-1}[i,j] = \\frac{C[j,i]}{det(A)}.
\\]

For example,

\\[
\\underbrace{
 \\begin{bmatrix}
  2 & 4 & 3\\\\
  5 & 1 & 6\\\\
  7 & 2 & 4\\\\
 \\end{bmatrix}
}_{A}
\\cdot
\\underbrace{
 \\frac{1}{81}
 \\begin{bmatrix}
   -8 & -10 & 21 \\\\
   22 & -13 & 3 \\\\
   3 & 24 & -18 \\\\
 \\end{bmatrix}
}_{A^{-1}} =
\\underbrace{
 \\begin{bmatrix}
  1 & 0 & 0 \\\\
  0 & 1 & 0 \\\\
  0 & 0 & 1 \\\\
 \\end{bmatrix}
}_{I}.
\\]

___

[^1]: The first such
algorithm was Strassen's algorithm,
published in 1969 [71],
whose time complexity is $O(n^{2.80735})$;
the best current algorithm [30]
works in $O(n^{2.37286})$ time.
