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

```rust
fn prime(n: usize) -> bool {
    if n < 2 {
        return false
    }
    let mut x = 2;
    while x*x <= n{
        if n%x == 0 {
            return false
        }
        x+=1
    }
    true
}
```

The following function `factors`
constructs a vector that contains the prime
factorization of $n$.
The function divides $n$ by its prime factors,
and adds them to the vector.
The process ends when the remaining number $n$
has no factors between $2$ and $\lfloor \sqrt n \rfloor$.
If $n>1$, it is prime and the last factor.

```rust
#println!("n = 100 -> {:?}", factors(100));
fn factors(mut n: isize) -> Vec<isize>{
    let mut f = Vec::new();
    let mut x = 2;
    while x*x <= n {
        while n%x == 0 {
            f.push(x);
            n/=x;
        }
        x+=1;
    }
    if n > 1 { f.push(n) }
    f
}
```

Note that each prime factor appears in the vector
as many times as it divides the number.
For example, $24=2^3 \cdot 3$,
so the result of the function is [2,2,2,3].

## Sieve of Eratosthenes

The sieve of Eratosthenes
is a preprocessing
algorithm that builds an array using which we
can efficiently check if a given number between $2 \ldots n$
is prime and, if it is not, find one prime factor of the number.

The algorithm builds an array `sieve`
whose positions $2,3,\ldots,n$ are used.
The value `sieve[k]=0` means
that $k$ is prime,
and the value `sieve[k] != 0`
means that $k$ is not a prime and one
of its prime factors is `sieve[k]`.

The algorithm iterates through the numbers
$2 \ldots n$ one by one.
Always when a new prime $x$ is found,
the algorithm records that the multiples
of $x$ ($2x,3x,4x,\ldots$) are not primes,
because the number $x$ divides them.

For example, if $n=20$, the array is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (19,1);

\node at (0.5,0.5) {0};
\node at (1.5,0.5) {0};
\node at (2.5,0.5) {2};
\node at (3.5,0.5) {0};
\node at (4.5,0.5) {3};
\node at (5.5,0.5) {0};
\node at (6.5,0.5) {2};
\node at (7.5,0.5) {3};
\node at (8.5,0.5) {5};
\node at (9.5,0.5) {0};
\node at (10.5,0.5) {3};
\node at (11.5,0.5) {0};
\node at (12.5,0.5) {7};
\node at (13.5,0.5) {5};
\node at (14.5,0.5) {2};
\node at (15.5,0.5) {0};
\node at (16.5,0.5) {3};
\node at (17.5,0.5) {0};
\node at (18.5,0.5) {5};
\node at (0.5,1.5) {2};
\node at (1.5,1.5) {3};
\node at (2.5,1.5) {4};
\node at (3.5,1.5) {5};
\node at (4.5,1.5) {6};
\node at (5.5,1.5) {7};
\node at (6.5,1.5) {8};
\node at (7.5,1.5) {9};
\node at (8.5,1.5) {10};
\node at (9.5,1.5) {11};
\node at (10.5,1.5) {12};
\node at (11.5,1.5) {13};
\node at (12.5,1.5) {14};
\node at (13.5,1.5) {15};
\node at (14.5,1.5) {16};
\node at (15.5,1.5) {17};
\node at (16.5,1.5) {18};
\node at (17.5,1.5) {19};
\node at (18.5,1.5) {20};
\end{tikzpicture}
</script>

The following code implements the sieve of
Eratosthenes.
The code assumes that each element of
`sieve` is initially zero.

```rust
#let mut n = 20;
#let mut sieve = vec![0_usize;n+1];
for x in 2..=n {
    if sieve[x] == 0 {
        let mut u = 2*x;
        while u <= n {
            sieve[u] = x;
            u+=x;
        }
    }
}
#println!("{:?}", &sieve[2..]);
```

The inner loop of the algorithm is executed
$n/x$ times for each value of $x$.
Thus, an upper bound for the running time
of the algorithm is the harmonic sum
\\[
\\sum_{x=2}^n n/x = n/2 + n/3 + n/4 + \\cdots + n/n = O(n \\log n)
\\]

In fact, the algorithm is more efficient,
because the inner loop will be executed only if
the number $x$ is prime.
It can be shown that the running time of the
algorithm is only $O(n \log \log n)$,
a complexity very near to $O(n)$. 

## Euclid's Algorithm

The **greatest common divisor** of
numbers $a$ and $b$, $\gcd(a,b)$,
is the greatest number that divides both $a$ and $b$,
and the **least common multiple** of
$a$ and $b$, $\textrm{lcm}(a,b)$,
is the smallest number that is divisible by
both $a$ and $b$.
For example,
$\gcd(24,36)=12$ and
$\textrm{lcm}(24,36)=72$.

The greatest common divisor and the least common multiple
are connected as follows:
\\[
\\textrm{lcm}(a,b)=\\frac{ab}{\\textrm{gcd}(a,b)}
\\]

**Euclid's algorithm**[^1] provides an efficient way
to find the greatest common divisor of two numbers.
The algorithm is based on the following formula:

\\[
    \\textrm{gcd}(a,b) = \\begin{cases}
               a        & b = 0\\\\
               \\textrm{gcd}(b,a \\bmod b) & b \\neq 0\\
           \\end{cases}
\\]

For example,
\\[
\\textrm{gcd}(24,36) = \\textrm{gcd}(36,24)
= \\textrm{gcd}(24,12) = \\textrm{gcd}(12,0)=12
\\]

The algorithm can be implemented as follows:

```rust
fn gcd(a: usize, b:usize)-> usize{
    if b == 0 {return a}
    gcd(b, a%b)
}
#println!("gcd between 100 and 85 is {:?}", gcd(100, 85));
```

It can be shown that Euclid's algorithm works
in $O(\log n)$ time, where $n=\min(a,b)$.
The worst case for the algorithm is
the case when $a$ and $b$ are consecutive Fibonacci numbers.
For example,
\\[
\\textrm{gcd}(13,8)=\\textrm{gcd}(8,5)
=\\textrm{gcd}(5,3)=\\textrm{gcd}(3,2)=\\textrm{gcd}(2,1)=\\textrm{gcd}(1,0)=1
\\]

## Euler's totient function

Numbers $a$ and $b$ are \key{coprime}
if $\textrm{gcd}(a,b)=1$.
**Euler's totient function** $\varphi(n)$
%\footnote{Euler presented this function in 1763.}
gives the number of coprime numbers to $n$
between $1$ and $n$.
For example, $\varphi(12)=4$,
because 1, 5, 7 and 11
are coprime to 12.

The value of $\varphi(n)$ can be calculated
from the prime factorization of $n$
using the formula

\\[
\\varphi(n) = \\prod_{i=1}^k p_i^{\\alpha_i-1}(p_i-1) 
\\]

For example, $\varphi(12)=2^1 \cdot (2-1) \cdot 3^0 \cdot (3-1)=4$.
Note that $\varphi(n)=n-1$ if $n$ is prime.

___
[^1] Euclid was a Greek mathematician who lived in about 300 BC. This is perhaps the first known algorithm in history.
