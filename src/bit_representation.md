#  Bit representation

In programming, an $n$ bit integer is internally
stored as a binary number that consists of $n$ bits.
For example, the Rust type `i32` is
a 32-bit type, which means that every `i32`
number consists of 32 bits.

Here is the bit representation of
the `i32` number 43: 
```rust
let number: i32 = 43;
println!("{number:032b}");
```

The bits in the representation are indexed from right to left.
To convert a bit representation $b_k \cdots b_2 b_1 b_0$ into a number,
we can use the formula
\\[
b_k 2^k + \\ldots + b_2 2^2 + b_1 2^1 + b_0 2^0
\\]

For example,
\\[
1 \\cdot 2^5 + 1 \\cdot 2^3 + 1 \\cdot 2^1 + 1 \\cdot 2^0 = 43
\\]

The bit representation of a number is either
**signed** or **unsigned**.
Usually a signed representation is used,
which means that both negative and positive
numbers can be represented.
A signed variable of $n$ bits can contain any
integer between $-2^{n-1}$ and $2^{n-1}-1$.
For example, the `i32` type in Rust is
a signed type, so an `i32` variable can contain any
integer between $-2^{31}$ and $2^{31}-1$.

The first bit in a signed representation
is the sign of the number (0 for nonnegative numbers
and 1 for negative numbers), and
the remaining $n-1$ bits contain the magnitude of the number.
**Two's complement** is used, which means that the
opposite number of a number is calculated by first
inverting all the bits in the number,
and then increasing the number by one.

For example, the bit representation of
the `i32` number $-43$ is

```rust
let number: i32 = -43;
println!("{number:032b}");
```

In an unsigned representation, only nonnegative
numbers can be used, but the upper bound for the values is larger.
An unsigned variable of $n$ bits can contain any
integer between $0$ and $2^n-1$.
For example, in Rust, an `u32` variable
can contain any integer between $0$ and $2^{32}-1$.

