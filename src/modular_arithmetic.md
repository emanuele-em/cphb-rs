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
    x^n = \\begin{cases}
               1        & n = 0\\\\
               x^{n/2} \\cdot x^{n/2} & \\text{$n$ is even}\\\\
               x^{n-1} \\cdot x & \\text{$n$ is odd}
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
