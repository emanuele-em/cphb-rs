# String hashing

**String hashing** is a technique that
allows us to efficiently check whether two
strings are equal[^1].
The idea in string hashing is to compare hash values of
strings instead of their individual characters.

## Calculating hash values

A **hash value** of a string is
a number that is calculated from the characters
of the string.
If two strings are the same,
their hash values are also the same,
which makes it possible to compare strings
based on their hash values.

A usual way to implement string hashing
is **polynomial hashing**, which means
that the hash value of a string `s`
of length $n$ is
\\[
(\\texttt{s}[0] A^{n-1} + \\texttt{s}[1] A^{n-2} + \\cdots + \\texttt{s}[n-1] A^0) \\bmod B  ,
\\]
where $s[0],s[1],\ldots,s[n-1]$
are interpreted as the codes of the characters of `s`,
and $A$ and $B$ are pre-chosen constants.

For example, the codes of the characters
of `ALLEY` are:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (5,2);

\node at (0.5, 1.5) {\texttt{A}};
\node at (1.5, 1.5) {\texttt{L}};
\node at (2.5, 1.5) {\texttt{L}};
\node at (3.5, 1.5) {\texttt{E}};
\node at (4.5, 1.5) {\texttt{Y}};

\node at (0.5, 0.5) {65};
\node at (1.5, 0.5) {76};
\node at (2.5, 0.5) {76};
\node at (3.5, 0.5) {69};
\node at (4.5, 0.5) {89};

\end{tikzpicture}
</script>

Thus, if $A=3$ and $B=97$, the hash value
of `ALLEY` is
\\[
(65 \\cdot 3^4 + 76 \\cdot 3^3 + 76 \\cdot 3^2 + 69 \\cdot 3^1 + 89 \\cdot 3^0) \\bmod 97 = 52.
\\]

## Preprocessing

Using polynomial hashing, we can calculate the hash value of any substring
of a string `s` in $O(1)$ time after an $O(n)$ time preprocessing.
The idea is to construct an array `h` such that
$\texttt{h}[k]$ contains the hash value of the prefix $\texttt{s}[0 \ldots k]$.
The array values can be recursively calculated as follows:
\\[
\\begin{array}{lcl}
\\texttt{h}[0] & = & \\texttt{s}[0] \\\\
\\texttt{h}[k] & = & (\\texttt{h}[k-1] A + \\texttt{s}[k]) \\bmod B \\\\
\\end{array}
\\]
In addition, we construct an array $\texttt{p}$
where $\texttt{p}[k]=A^k \bmod B$:
\\[
\\begin{array}{lcl}
\\texttt{p}[0] & = & 1 \\\\
\\texttt{p}[k] & = & (\\texttt{p}[k-1] A) \\bmod B. \\\\
\\end{array}
\\]
Constructing these arrays takes $O(n)$ time. Both arrays and the
substring query look as follows:

```rust
const A: u64 = 911_382_323;
const B: u64 = 972_663_749;

fn preprocess(s: &str) -> (Vec<u64>, Vec<u64>) {
    let s = s.as_bytes();
    let mut h = vec![0u64; s.len()];
    let mut p = vec![1u64; s.len()];
    for k in 0..s.len() {
        h[k] = if k == 0 { s[0] as u64 } else { (h[k-1] * A + s[k] as u64) % B };
        if k > 0 { p[k] = p[k-1] * A % B; }
    }
    (h, p)
}

// hash of s[a..=b]
fn substring(h: &[u64], p: &[u64], a: usize, b: usize) -> u64 {
    if a == 0 { return h[b]; }
    // add B before subtracting: these are unsigned, and the difference
    // would otherwise underflow
    (h[b] + B - h[a-1] * p[b-a+1] % B) % B
}
# let (h, p) = preprocess("ALLALLALLA");
# println!("hash of s[0..=2] = {}", substring(&h, &p, 0, 2));
# println!("hash of s[3..=5] = {}", substring(&h, &p, 3, 5));
# println!("equal substrings hash equally: {}",
#          substring(&h,&p,0,2) == substring(&h,&p,3,5));
```

Every product stays below $B^2 \approx 9.5 \cdot 10^{17}$, inside the
range of a `u64`. Note the `+ B` in the substring formula: C++ would let
the subtraction go negative and correct it afterwards, but `u64` would
underflow and panic, so the modulus is added first.
After this, the hash value of any substring
$\texttt{s}[a \ldots b]$
can be calculated in $O(1)$ time using the formula
\\[
(\\texttt{h}[b]-\\texttt{h}[a-1] \\texttt{p}[b-a+1]) \\bmod B
\\]
assuming that $a>0$.
If $a=0$, the hash value is simply $\texttt{h}[b]$.

## Using hash values

We can efficiently compare strings using hash values.
Instead of comparing the individual characters of the strings,
the idea is to compare their hash values.
If the hash values are equal,
the strings are _probably_ equal,
and if the hash values are different,
the strings are _certainly_ different.

Using hashing, we can often make a brute force
algorithm efficient.
As an example, consider the pattern matching problem:
given a string $s$ and a pattern $p$,
find the positions where $p$ occurs in $s$.
A brute force algorithm goes through all positions
where $p$ may occur and compares the strings
character by character.
The time complexity of such an algorithm is $O(n^2)$.

We can make the brute force algorithm more efficient
by using hashing, because the algorithm compares
substrings of strings.
Using hashing, each comparison only takes $O(1)$ time,
because only hash values of substrings are compared.
This results in an algorithm with time complexity $O(n)$,
which is the best possible time complexity for this problem.

By combining hashing and _binary search_,
it is also possible to find out the lexicographic order of
two strings in logarithmic time.
This can be done by calculating the length
of the common prefix of the strings using binary search.
Once we know the length of the common prefix,
we can just check the next character after the prefix,
because this determines the order of the strings.

## Collisions and parameters

An evident risk when comparing hash values is
a **collision**, which means that two strings have
different contents but equal hash values.
In this case, an algorithm that relies on
the hash values concludes that the strings are equal,
but in reality they are not,
and the algorithm may give incorrect results.

Collisions are always possible,
because the number of different strings is larger
than the number of different hash values.
However, the probability of a collision is small
if the constants $A$ and $B$ are carefully chosen.
A usual way is to choose random constants
near $10^9$, for example as follows:
\\[
\\begin{array}{lcl}
A & = & 911382323 \\\\
B & = & 972663749 \\\\
\\end{array}
\\]

Using such constants,
the `long long` type can be used
when calculating hash values,
because the products $AB$ and $BB$ will fit in `long long`.
But is it enough to have about $10^9$ different hash values?

Let us consider three scenarios where hashing can be used:

_Scenario 1:_ Strings $x$ and $y$ are compared with
each other.
The probability of a collision is $1/B$ assuming that
all hash values are equally probable.

_Scenario 2:_ A string $x$ is compared with strings
$y_1,y_2,\ldots,y_n$.
The probability of one or more collisions is

\\[
1-(1-\\frac{1}{B})^n.
\\]

_Scenario 3:_ All pairs of strings $x_1,x_2,\ldots,x_n$
are compared with each other.
The probability of one or more collisions is
\\[
1 - \\frac{B \\cdot (B-1) \\cdot (B-2) \\cdots (B-n+1)}{B^n}.
\\]

The following table shows the collision probabilities
when $n=10^6$ and the value of $B$ varies:


| constant $B$ | scenario 1 | scenario 2 | scenario 3 |
| ---: | ---: | ---: | ---: |
| $10^3$ | $0.001000$ | $1.000000$ | $1.000000$ |
| $10^6$ | $0.000001$ | $0.632121$ | $1.000000$ |
| $10^9$ | $0.000000$ | $0.001000$ | $1.000000$ |
| $10^{12}$ | $0.000000$ | $0.000000$ | $0.393469$ |
| $10^{15}$ | $0.000000$ | $0.000000$ | $0.000500$ |
| $10^{18}$ | $0.000000$ | $0.000000$ | $0.000001$ |


The table shows that in scenario 1,
the probability of a collision is negligible
when $B \approx 10^9$.
In scenario 2, a collision is possible but the
probability is still quite small.
However, in scenario 3 the situation is very different:
a collision will almost always happen when
$B \approx 10^9$.

The phenomenon in scenario 3 is known as the
**birthday paradox**: if there are $n$ people
in a room, the probability that _some_ two people
have the same birthday is large even if $n$ is quite small.
In hashing, correspondingly, when all hash values are compared
with each other, the probability that some two
hash values are equal is large.

We can make the probability of a collision
smaller by calculating _multiple_ hash values
using different parameters.
It is unlikely that a collision would occur
in all hash values at the same time.
For example, two hash values with parameter
$B \approx 10^9$ correspond to one hash
value with parameter $B \approx 10^{18}$,
which makes the probability of a collision very small.

Some people use constants $B=2^{32}$ and $B=2^{64}$,
which is convenient, because operations with 32 and 64
bit integers are calculated modulo $2^{32}$ and $2^{64}$.
However, this is _not_ a good choice, because it is possible
to construct inputs that always generate collisions when
constants of the form $2^x$ are used [57].

___

[^1]: The technique
was popularized by the Karp–Rabin pattern matching
algorithm [46].
