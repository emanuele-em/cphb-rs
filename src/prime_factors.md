# Primes and factors

A number $n>1$ is a **prime**
if its only positive factors are 1 and $n$.
For example, 7, 19 and 41 are primes,
but 35 is not a prime, because $5 \cdot 7 = 35$.
For every number $n>1$, there is a unique
**prime factorization**
\\[
n = p_1^{\\alpha_1} p_2^{\\alpha_2} \\cdots p_k^{\\alpha_k},\\]
where $p_1,p_2,\ldots,p_k$ are distinct primes and
$\alpha_1,\alpha_2,\ldots,\alpha_k$ are positive numbers.
For example, the prime factorization for 84 is
\\[
84 = 2^2 \\cdot 3^1 \\cdot 7^1
\\]

The **number of factors** of a number $n$ is

\\[
\\tau(n)=\\prod_{i=1}^k (\\alpha_i+1)
\\]

because for each prime $p_i$, there are
$\alpha_i+1$ ways to choose how many times
it appears in the factor.
For example, the number of factors
of 84 is
$\tau(84)=3 \cdot 2 \cdot 2 = 12$.
The factors are

$$1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84$$

The **sum of factors** of $n$ is
\\[
\\sigma(n)=\\prod_{i=1}^k (1+p_i+\\ldots+p_i^{\\alpha_i}) = \\prod_{i=1}^k \\frac{p_i^{a_i+1}-1}{p_i-1}
\\]
where the latter formula is based on the geometric progression formula.
For example, the sum of factors of 84 is
\\[
\\sigma(84)=\\frac{2^3-1}{2-1} \\cdot \\frac{3^2-1}{3-1} \\cdot \\frac{7^2-1}{7-1} = 7 \\cdot 4 \\cdot 8 = 224
\\]

The **product of factors** of $n$ is
\\[
\\mu(n)=n^{\\tau(n)/2}
\\]
because we can form $\tau(n)/2$ pairs from the factors,
each with product $n$.
For example, the factors of 84
produce the pairs
$1 \cdot 84$, $2 \cdot 42$, $3 \cdot 28$, etc.,
and the product of the factors is $\mu(84)=84^6=351298031616$.

A number $n$ is called a **perfect number** if $n=\sigma(n)-n$,
i.e., $n$ equals the sum of its factors
between $1$ and $n-1$.
For example, 28 is a perfect number,
because $28=1+2+4+7+14$.

## Number of primes

It is easy to show that there is an infinite number
of primes.
If the number of primes would be finite,
we could construct a set $P=\{p_1,p_2,\ldots,p_n\}$
that would contain all the primes.
For example, $p_1=2$, $p_2=3$, $p_3=5$, and so on.
However, using $P$, we could form a new prime
\\[p_1 p_2 \\cdots p_n+1\\]
that is larger than all elements in $P$.
This is a contradiction, and the number of primes
has to be infinite.

## Density of primes

The density of primes means how often there are primes
among the numbers.
Let $\pi(n)$ denote the number of primes between
$1$ and $n$. For example, $\pi(10)=4$, because
there are 4 primes between $1$ and $10$: 2, 3, 5 and 7.

It is possible to show that

\\[
\\pi(n) \\approx \\frac{n}{\\ln n}
\\]

which means that primes are quite frequent.
For example, the number of primes between
$1$ and $10^6$ is $\pi(10^6)=78498$,
and $10^6 / \ln 10^6 \approx 72382$.

## Conjectures

There are many _conjectures_ involving primes.
Most people think that the conjectures are true,
but nobody has been able to prove them.
For example, the following conjectures are famous:

- **Goldbach's conjecture**: Each even integer $n>2$ can be represented as a sum $n=a+b$ so that both $a$ and $b$ are primes.
- **Twin prime conjecture**: There is an infinite number of pairs of the form $\{p,p+2\}$, where both $p$ and $p+2$ are primes.
- **Legendre's conjecture**: There is always a prime between numbers $n^2$ and $(n+1)^2$, where $n$ is any positive integer.

## Basic algorithms

If a number $n$ is not prime,
it can be represented as a product $a \cdot b$,
where $a \le \sqrt n$ or $b \le \sqrt n$,
so it certainly has a factor between $2$ and $\lfloor \sqrt n \rfloor$.
Using this observation, we can both test
if a number is prime and find the prime factorization
of a number in $O(\sqrt n)$ time.

The following function `prime` checks
if the given number $n$ is prime.
The function attempts to divide $n$ by
all numbers between $2$ and $\lfloor \sqrt n \rfloor$,
and if none of them divides $n$, then $n$ is prime.

