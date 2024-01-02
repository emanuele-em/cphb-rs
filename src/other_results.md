# Other results

## Lagrange's Theorem

**Lagrange's theorem**
states that every positive integer
can be represented as a sum of four squares, i.e.,
$a^2+b^2+c^2+d^2$.
For example, the number 123 can be represented
as the sum $8^2+5^2+5^2+3^2$.

## Zeckendorf's Theorem

**Zeckendorf's theorem**
states that every
positive integer has a unique representation
as a sum of Fibonacci numbers such that
no two numbers are equal or consecutive
Fibonacci numbers.
For example, the number 74 can be represented
as the sum $55+13+5+1$.

## Pythagorean triples

A **Pythagorean triple** is a triple $(a,b,c)$
that satisfies the Pythagorean theorem
$a^2+b^2=c^2$, which means that there is a right triangle
with side lengths $a$, $b$ and $c$.
For example, $(3,4,5)$ is a Pythagorean triple.

If $(a,b,c)$ is a Pythagorean triple,
all triples of the form $(ka,kb,kc)$
are also Pythagorean triples where $k>1$.
A Pythagorean triple is _primitive_ if
$a$, $b$ and $c$ are coprime,
and all Pythagorean triples can be constructed
from primitive triples using a multiplier $k$.

**Euclid's formula** can be used to produce
all primitive Pythagorean triples.
Each such triple is of the form

\\[(n^2-m^2,2nm,n^2+m^2),\\]

where $0<m<n$, $n$ and $m$ are coprime
and at least one of $n$ and $m$ is even.
For example, when $m=1$ and $n=2$, the formula
produces the smallest Pythagorean triple

\\[
(2^2-1^2,2\\cdot2\\cdot1,2^2+1^2)=(3,4,5)
\\]

## Wilson's Theorem

**Wilson's theorem**
states that a number $n$
is prime exactly when

\\[
(n-1)! \\bmod n = n-1
\\]

For example, the number 11 is prime, because

\\[
10! \\bmod 11 = 10
\\]
and the number 12 is not prime, because

\\[
11! \\bmod 12 = 0 \\neq 11
\\]

Hence, Wilson's theorem can be used to find out
whether a number is prime. However, in practice, the theorem cannot be
applied to large values of $n$, because it is difficult
to calculate values of $(n-1)!$ when $n$ is large.
