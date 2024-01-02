# Modular arithmetic

In **modular arithmetic**,
the set of numbers is limited so
that only numbers $0,1,2,\ldots,m-1$ are used,
where $m$ is a constant.
Each number $x$ is
represented by the number $x \bmod m$:
the remainder after dividing $x$ by $m$.
For example, if $m=17$, then $75$
is represented by $75 \bmod 17 = 7$.

Often we can take remainders before doing
calculations.
In particular, the following formulas hold:
\\[
\\begin{array}{rcl}
(x+y) \\bmod m & = & (x \\bmod m + y \\bmod m) \\bmod m \\\\
(x-y) \\bmod m & = & (x \\bmod m - y \\bmod m) \\bmod m \\\\
(x \\cdot y) \\bmod m & = & (x \\bmod m \\cdot y \\bmod m) \\bmod m \\\\
x^n \\bmod m & = & (x \\bmod m)^n \\bmod m \\\\
\\end{array}
\\]

## Modular exponentiation

There is often need to efficiently calculate
the value of $x^n \bmod m$.
This can be done in $O(\log n)$ time
using the following recursion:

\\[
x^n =
\\begin{cases}
   1        & n = 0 \\\\
   x^{n/2} \\cdot x^{n/2} & \\text{n is even} \\\\
   x^{n-1} \\cdot x & \\text{n is odd} \\\\
\\end{cases}
\\]

It is important that in the case of an even $n$,
the value of $x^{n/2}$ is calculated only once.
This guarantees that the time complexity of the
algorithm is $O(\log n)$, because $n$ is always halved
when it is even.

The following function calculates the value of
$x^n \bmod m$:

```rust
#println!("{:?}", modpow(5, 4, 2));
fn modpow(x: usize, n:usize, m:usize) -> usize{
    if n == 0 {return 1%m}
    let mut u = modpow(x, n/2, m);
    u = (u*u)%m;
    if n%2 == 1 {u = (u*x)%m}
    u
}
```

## Fermat's theorem and Euler's theorem

**Fermat's theorem**
states that
\\[x^{m-1} \\bmod m = 1\\]
when $m$ is prime and $x$ and $m$ are coprime.
This also yields
\\[x^k \\bmod m = x^{k \\bmod (m-1)} \\bmod m.\\]
More generally, **Euler's theorem**
states that
\\[x^{\\varphi(m)} \\bmod m = 1\\]
when $x$ and $m$ are coprime.
Fermat's theorem follows from Euler's theorem,
because if $m$ is a prime, then $\varphi(m)=m-1$.

## Modular Inverse

The inverse of $x$ modulo $m$
is a number $x^{-1}$ such that
\\[ x x^{-1} \\bmod m = 1. \\]
For example, if $x=6$ and $m=17$,
then $x^{-1}=3$, because $6\cdot3 \bmod 17=1$.

Using modular inverses, we can divide numbers
modulo $m$, because division by $x$
corresponds to multiplication by $x^{-1}$.
For example, to evaluate the value of $36/6 \bmod 17$,
we can use the formula $2 \cdot 3 \bmod 17$,
because $36 \bmod 17 = 2$ and $6^{-1} \bmod 17 = 3$.

However, a modular inverse does not always exist.
For example, if $x=2$ and $m=4$, the equation
\\[ x x^{-1} \\bmod m = 1 \\]
cannot be solved, because all multiples of 2
are even and the remainder can never be 1 when $m=4$.
It turns out that the value of $x^{-1} \bmod m$
can be calculated exactly when $x$ and $m$ are coprime.

If a modular inverse exists, it can be
calculated using the formula
\\[
x^{-1} = x^{\\varphi(m)-1}.
\\]

If $m$ is prime, the formula becomes

\\[
x^{-1} = x^{m-2}.
\\]

For example,

\\[6^{-1} \\bmod 17 =6^{17-2} \\bmod 17 = 3.\\]

This formula allows us to efficiently calculate
modular inverses using the modular exponentation algorithm.
The formula can be derived using Euler's theorem.
First, the modular inverse should satisfy the following equation:

\\[
x x^{-1} \\bmod m = 1.
\\]

On the other hand, according to Euler's theorem,

\\[
x^{\\varphi(m)} \\bmod m =  xx^{\\varphi(m)-1} \\bmod m = 1,
\\]

so the numbers $x^{-1}$ and $x^{\varphi(m)-1}$ are equal.

## Computer Arithmetic

In Rust, when arithmetic operations result in a value that exceeds the maximum representable value for a given data type, it causes an overflow.
This behavior is different from modulo wrapping.

For example, in Rust, if you have a `u32` variable with a value of $123456789$, and you multiply it by itself,
the result will overflow because it exceeds the maximum value that can be represented by a `u32`. The calculation would be:

```rust
let x = 123456789_u32;
println!("{}", x*x); // overflow
```
Rust provides several ways to handle integer overflow.
One common approach is to use the `wrapping_*` methods, 
which perform arithmetic operations while wrapping around on overflow. 
Here's an example of using `wrapping_mul` to perform multiplication, 
the result is
$123456789^2 \bmod 2^{32} = 2537071545$.

```rust
let x = 123456789_u32;
println!("{}", x.wrapping_mul(x)); // 2537071545
```
