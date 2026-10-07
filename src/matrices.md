# Matrices

A **matrix** is a mathematical concept
that corresponds to a two-dimensional array
in programming. For example,
\\[
A = 
 \\begin{bmatrix}
  6 & 13 & 7 & 4 \\\\
  7 & 0 & 8 & 2 \\\\
  9 & 5 & 4 & 18 \\\\
 \\end{bmatrix}
\\]
is a matrix of size $3 \times 4$, i.e.,
it has 3 rows and 4 columns.
The notation $[i,j]$ refers to
the element in row $i$ and column $j$
in a matrix.
For example, in the above matrix,
$A[2,3]=8$ and $A[3,1]=9$.

A special case of a matrix is a **vector**
that is a one-dimensional matrix of size $n \times 1$.
For example,
\\[
V =
\\begin{bmatrix}
4 \\\\
7 \\\\
5 \\\\
\\end{bmatrix}
\\]
is a vector that contains three elements.

The **transpose** $A^T$ of a matrix $A$
is obtained when the rows and columns of $A$
are swapped, i.e., $A^T[i,j]=A[j,i]$:
\\[
A^T = 
 \\begin{bmatrix}
  6 & 7 & 9 \\\\
  13 & 0 & 5 \\\\
  7 & 8 & 4 \\\\
  4 & 2 & 18 \\\\
 \\end{bmatrix}
\\]

A matrix is a **square matrix** if it
has the same number of rows and columns.
For example, the following matrix is a
square matrix:

\\[
S = 
 \\begin{bmatrix}
  3 & 12 & 4  \\\\
  5 & 9 & 15  \\\\
  0 & 2 & 4 \\\\
 \\end{bmatrix}
\\]
