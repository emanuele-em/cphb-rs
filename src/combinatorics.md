# Combinatorics

**Combinatorics** studies methods for counting
combinations of objects.
Usually, the goal is to find a way to
count the combinations efficiently
without generating each combination separately.

As an example, consider the problem
of counting the number of ways to
represent an integer $n$ as a sum of positive integers.
For example, there are 8 representations
for $4$:
- $1+1+1+1$
- $1+1+2$
- $1+2+1$
- $2+1+1$
- $2+2$
- $3+1$
- $1+3$
- $4$

A combinatorial problem can often be solved
using a recursive function.
In this problem, we can define a function $f(n)$
that gives the number of representations for $n$.
For example, $f(4)=8$ according to the above example.
The values of the function
can be recursively calculated as follows:
\\begin{equation*}
    f(n) = \\begin{cases}
               1               & n = 0\\\\
               f(0)+f(1)+\\cdots+f(n-1) & n > 0\\\\
           \\end{cases}
\\end{equation*}
The base case is $f(0)=1$,
because the empty sum represents the number 0.
Then, if $n>0$, we consider all ways to
choose the first number of the sum.
If the first number is $k$,
there are $f(n-k)$ representations
for the remaining part of the sum.
Thus, we calculate the sum of all values
of the form $f(n-k)$ where $k<n$.

The first values for the function are:
\\[
\\begin{array}{lcl}
f(0) & = & 1 \\\\
f(1) & = & 1 \\\\
f(2) & = & 2 \\\\
f(3) & = & 4 \\\\
f(4) & = & 8 \\\\
\\end{array}
\\]

Sometimes, a recursive formula can be replaced
with a closed-form formula.
In this problem,
\\[
f(n)=2^{n-1},
\\]
which is based on the fact that there are $n-1$
possible positions for +-signs in the sum
and we can choose any subset of them.
