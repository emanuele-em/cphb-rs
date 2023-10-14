#  Bit operations

## `and` operation

The `and` operation `x & y` produces a number
that has one bits in positions where both
$x$ and $y$ have one bits.
For example:

```rust
println!("{}", 22 & 26);
# println!("The result is {} because:", 22 & 26);
# println!("   {:032b} => ({})", 22, 22);
# println!(" & {:032b} => ({})", 26, 26);
# println!("{}", vec!['_';43].iter().collect::<String>());
# println!(" = {:032b} => ({})", 22 & 26, 22 & 26);
```

| | bin | dec |
| --- | :---: | --- |
| | 10110 | (22) |
| & | 11010 | (26) |
| = | 11110 | (30) |

Using the `and` operation, we can check if a number
$x$ is even because

- `x & 1 = 0` if $x$ is even
- `x & 1 = 1` if $x$ is odd.

More generally, $x$ is divisible by $2^k$
exactly when `x & (2^k-1) = 0`.

## `or` operation

The `or` operation `x | y` produces a number
that has one bits in positions where at least one of
$x$ and $y$ have one bits.
For example:

```rust
println!("{}", 22 | 26);
# println!("The result is {} because:", 22 | 26);
# println!("   {:032b} => ({})", 22, 22);
# println!(" | {:032b} => ({})", 26, 26);
# println!("{}", vec!['_';43].iter().collect::<String>());
# println!(" = {:032b} => ({})", 22 | 26, 22 | 26);
```

| | bin | dec |
| --- | :---: | --- |
| | 10110 | (22) |
| \| | 11010 | (26) |
| = | 11100 | (30) |

## `xor` operation

The `xor` operation `x ^ y` produces a number
that has one bits in positions where exactly one of `x` and `y` have one bits.
For example:

```rust
println!("{}", 22 ^ 26);
# println!("The result is {} because:", 22 ^ 26);
# println!("   {:032b} => ({})", 22, 22);
# println!(" ^ {:032b} => ({})", 26, 26);
# println!("{}", vec!['_';43].iter().collect::<String>());
# println!(" = {:032b} => ({})", 22 ^ 26, 22 ^ 26);
```

| | bin | dec |
| --- | :---: | --- |
| | 10110 | (22) |
| ^ | 11010 | (26) |
| = | 01100 | (12) |

## `not` operation

The `not` operation `x ! y` produces a number
where all the bits of `x` have been inverted.
For example:

```rust
println!("{}", !22);
# println!("The result is {} because:", !22);
# println!(" ! {:032b} => ({})", 22, 22);
# println!("{}", vec!['_';43].iter().collect::<String>());
# println!(" = {:032b} => ({})", !22, !22);
```

| | bin | dec |
| --- | :---: | --- |
| ! | 00000000000000000000000000010110 | (22) |
| = | 11111111111111111111111111101001 | (30) |

## Bit shifts

The left bit shift `x < < k` appends $k$
zero bits to the number,
and the right bit shift `x > > k`
removes the $k$ last bits from the number.
For example:

```rust
println!("{}", 14<<2);
# println!("The result is {} because:", 14<<2);
# println!("{:032b} => ({})", 14, 14);
# println!("{:032b} => ({})", 14<<2, 14<<2);
```

Note that `x << k`
corresponds to multiplying `x` by `2^k`,
and `x > > k`
corresponds to dividing `x` by `2^k`
rounded down to an integer.

## Applications

A number of the form `1 << k` has a one bit
in position $k$ and all other bits are zero,
so we can use such numbers to access single bits of numbers.
In particular, the $k$th bit of a number is one
exactly when `x & (1 << k)` is not zero.
The following code print a `u32` bit by bit:

```rust
# let x = 43;
for i in (0..31).rev() {
    print!("{}", if x&(1<<i) != 0 {1} else {0});
}

```

It is also possible to modify single bits
of numbers using similar ideas.
For example, the formula `x | (1 << k)`
sets the $k$th bit of $x$ to one,
the formula `x & !(1 << k)`
sets the $k$th bit of $x$ to zero,
and the formula
`x^(1 << k)`
inverts the $k$th bit of $x$.

The formula `x & (x-1)` sets the last
one bit of $x$ to zero,
and the formula `x & -x` sets all the
one bits to zero, except for the last one bit.
The formula `x | (x-1)`
inverts all the bits after the last one bit.
Also note that a positive number $x$ is
a power of two exactly when `x & (x-1) = 0`.
