#  Bit optimizations

Many algorithms can be optimized using
bit operations.
Such optimizations do not change the
time complexity of the algorithm,
but they may have a large impact
on the actual running time of the code.
In this section we discuss examples
of such situations.

## Hamming distance

The **Hamming distance**
$hamming(a,b)$ between two
strings $a$ and $b$ of equal length is
the number of positions where the strings differ.
For example,
$$
hamming(01101,11001)=2
$$

Consider the following problem: Given
a list of $n$ bit strings, each of length $k$,
calculate the minimum Hamming distance
between two strings in the list.
For example, the answer for $[00111,01101,11110]$
is 2, because

- $hamming(00111,01101)=2$
- $hamming(00111,11110)=3$
- $hamming(01101,11110)=3$

A straightforward way to solve the problem is
to go through all pairs of strings and calculate
their Hamming distances,
which yields an $O(n^2 k)$ time algorithm.
The following function can be used to
calculate distances:
```rust
# let a = "00111";
# let b = "01101";
# println!("{}", hamming(a, b));
fn hamming(a: &str, b: &str) -> u32 {
    let mut d = 0;
    for i in 0..a.len() {
        if a.chars().nth(i) != b.chars().nth(i) {d+=1}
    }
    d
}
```

However, if $k$ is small, we can optimize the code
by storing the bit strings as integers and
calculating the Hamming distances using bit operations.
In particular, if $k \le 32$, we can just store
the strings as _i32_ values and use the
following function to calculate distances:

```rust

# let a = 0b00111;
# let b = 0b01101;
# println!("{}", hamming(a, b));
fn hamming(a: i32, b: i32) -> u32 {
    (a^b).count_ones()
}
```

In the above function, the `xor` operation constructs
a bit string that has one bits in positions
where $a$ and $b$ differ.
Then, the number of bits is calculated using
the `count_ones()` function.

To compare the implementations, we generated
a list of 10000 random bit strings of length 30.
The bit optimized code was almost
30 times faster than the original code.

## Counting subgrids

As another example, consider the
following problem:
Given an $n \times n$ grid whose
each square is either black (1) or white (0),
calculate the number of subgrids
whose all corners are black.
For example, the grid

<script type="text/tikz">
\begin{tikzpicture}[scale=0.5]
\fill[black] (1,1) rectangle (2,2);
\fill[black] (1,4) rectangle (2,5);
\fill[black] (4,1) rectangle (5,2);
\fill[black] (4,4) rectangle (5,5);
\fill[black] (1,3) rectangle (2,4);
\fill[black] (2,3) rectangle (3,4);
\fill[black] (2,1) rectangle (3,2);
\fill[black] (0,2) rectangle (1,3);
\draw (0,0) grid (5,5);
\end{tikzpicture}
</script>

contains two such subgrids:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.5]
\fill[black] (1,1) rectangle (2,2);
\fill[black] (1,4) rectangle (2,5);
\fill[black] (4,1) rectangle (5,2);
\fill[black] (4,4) rectangle (5,5);
\fill[black] (1,3) rectangle (2,4);
\fill[black] (2,3) rectangle (3,4);
\fill[black] (2,1) rectangle (3,2);
\fill[black] (0,2) rectangle (1,3);
\draw (0,0) grid (5,5);

\fill[black] (7+1,1) rectangle (7+2,2);
\fill[black] (7+1,4) rectangle (7+2,5);
\fill[black] (7+4,1) rectangle (7+5,2);
\fill[black] (7+4,4) rectangle (7+5,5);
\fill[black] (7+1,3) rectangle (7+2,4);
\fill[black] (7+2,3) rectangle (7+3,4);
\fill[black] (7+2,1) rectangle (7+3,2);
\fill[black] (7+0,2) rectangle (7+1,3);
\draw (7+0,0) grid (7+5,5);

\draw[color=red,line width=1mm] (1,1) rectangle (3,4);
\draw[color=red,line width=1mm] (7+1,1) rectangle (7+5,5);
\end{tikzpicture}
</script>

There is an $O(n^3)$ time algorithm for solving the problem:
go through all $O(n^2)$ pairs of rows and for each pair
$(a,b)$ calculate the number of columns that contain a black
square in both rows in $O(n)$ time.
The following code assumes that `color[y][x]`
denotes the color in row $y$ and column $x$:

```rust, ignore
let mut count = 0;
for i in 0..n{
    if color[a][i] == 1 && color[b][i] == 1 {count+=1};
}
```
account for $count(count-1)/2$ subgrids with black corners,
because we can choose any two of them to form a subgrid.

To optimize this algorithm, we divide the grid into blocks
of columns such that each block consists of $N$
consecutive columns. Then, each row is stored as
a list of $N$-bit numbers that describe the colors
of the squares. Now we can process $N$ columns at the same time
using bit operations. In the following code,

```rust, ignore
let mut count = 0;
for i in 0..n/N {
    count += (color[a][i]&color[b][i]).count_ones();
}
```

The resulting algorithm works in $O(n^3/N)$ time.

We generated a random grid of size $2500 \times 2500$
and compared the original and bit optimized implementation.
The original code is 10 times slower.
