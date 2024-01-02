# Solving equations

## Diophantine Equations

A **Diophantine equation**
is an equation of the form

\\[ ax + by = c, \\]

where $a$, $b$ and $c$ are constants
and the values of $x$ and $y$ should be found.
Each number in the equation has to be an integer.
For example, one solution for the equation
$5x+2y=11$ is $x=3$ and $y=-2$.

We can efficiently solve a Diophantine equation
by using Euclid's algorithm.
It turns out that we can extend Euclid's algorithm
so that it will find numbers $x$ and $y$
that satisfy the following equation:
\\[
ax + by = \\textrm{gcd}(a,b)
\\]

A Diophantine equation can be solved if
$c$ is divisible by
$\textrm{gcd}(a,b)$,
and otherwise it cannot be solved.

As an example, let us find numbers $x$ and $y$
that satisfy the following equation:
\\[
39x + 15y = 12
\\]
The equation can be solved, because
$\textrm{gcd}(39,15)=3$ and $3 \mid 12$.
When Euclid's algorithm calculates the
greatest common divisor of 39 and 15,
it produces the following sequence of function calls:

\\[
\\textrm{gcd}(39,15) = \\textrm{gcd}(15,9)
= \\textrm{gcd}(9,6) = \\textrm{gcd}(6,3)
= \\textrm{gcd}(3,0) = 3
\\]

This corresponds to the following equations:

\\[
\\begin{array}{lcl}
39 - 2 \\cdot 15 & = & 9 \\\\
15 - 1 \\cdot 9 & = & 6 \\\\
9 - 1 \\cdot 6 & = & 3 \\\\
\\end{array}
\\]

Using these equations, we can derive

\\[
39 \\cdot 2 + 15 \\cdot (-5) = 3
\\]

and by multiplying this by 4, the result is

\\[
39 \\cdot 8 + 15 \\cdot (-20) = 12,
\\]

so a solution to the equation is
$x=8$ and $y=-20$.

A solution to a Diophantine equation is not unique,
because we can form an infinite number of solutions
if we know one solution.
If a pair $(x,y)$ is a solution, then also all pairs

\\[(x+\\frac{kb}{\\textrm{gcd}(a,b)},y-\\frac{ka}{\\textrm{gcd}(a,b)})\\]

are solutions, where $k$ is any integer.

## Chinese Remainder Theorem

The **Chinese remainder theorem** solves
a group of equations of the form

\\[
\\begin{array}{lcl}
x & = & a_1 \\bmod m_1 \\\\
x & = & a_2 \\bmod m_2 \\\\
\\cdots \\\\
x & = & a_n \\bmod m_n \\\\
\\end{array}
\\]

where all pairs of $m_1,m_2,\ldots,m_n$ are coprime.

Let $x^{-1}_m$ be the inverse of $x$ modulo $m$, and

\\[ X_k = \\frac{m_1 m_2 \\cdots m_n}{m_k}.\\]

Using this notation, a solution to the equations is

\\[
x = a_1 X_1 {X_1}^{-1}\_{m_1} + a_2 X_2 {X_2}^{-1}\_{m_2} + \\cdots + a_n X_n {X_n}^{-1}\_{m_n}
\\]

In this solution, for each $k=1,2,\ldots,n$,

\\[a_k X_k {X_k}^{-1}_{m_k} \\bmod m_k = a_k\\]

because

\\[X_k {X_k}^{-1}_{m_k} \\bmod m_k = 1\\]

Since all other terms in the sum are divisible by $m_k$,
they have no effect on the remainder,
and $x \bmod m_k = a_k$.

For example, a solution for

\\[
\\begin{array}{lcl}
x & = & 3 \\bmod 5 \\\\
x & = & 4 \\bmod 7 \\\\
x & = & 2 \\bmod 3 \\\\
\\end{array}
\\]

is

\\[
3 \\cdot 21 \\cdot 1 + 4 \\cdot 15 \\cdot 1 + 2 \\cdot 35 \\cdot 2 = 263.
\\]

Once we have found a solution $x$,
we can create an infinite number of other solutions,
because all numbers of the form

\\[
x+m_1 m_2 \\cdots m_n
\\]

are solutions.
