# Working with numbers

## Integers

The most used integer type in competitive programming is _usize_, which size is how many bytes it takes to reference any location in memory.
For example, on a 32 bit target, this is 4 bytes and on a 64 bit target, this is 8 bytes.
This type is very common because it could be used as index for Arrays and Vectors.
The following code defines a `usize` variable in multiple ways:
```rust
let x = 123456789123456789_usize;
let x: usize = 123456789123456789; 
```
The suffix __usize_ means that the type of the number is _usize_.

## Modular arithmetic

We denote by $x mod m$ the remainder when $x$ is divided by $m$.
For example, $17 mod 5 = 2$, because $17 = 3·5+2$.
Sometimes, the answer to a problem is a very large number but it is enough to output it ”modulo m”, i.e., the remainder when the answer is divided by $m$ (for 6 example, ”modulo 109 + 7”). The idea is that even if the actual answer is very large, it suffices to use the types _usize_.
An important property of the remainder is that in addition, subtraction and multiplication, the remainder can be taken before the operation:
$$
(a + b) \mod m = (a \mod m + b \mod m) \mod m \\
(a - b) \mod m = (a \mod m - b \mod m) \mod m \\
(a \cdot b) \mod m = (a \mod m \cdot b \mod m) \mod m \\
$$

Thus, we can take the remainder after every operation and the numbers will never become too large.
For example, the following code calculates n!, the factorial of n, modulo m:

```rust
# let n = 5;
# let m = 9;
let mut x = 1;
for i in (2..=n){
    x = (x*i)%m;
}
# print!("if n = {n} and m = {m} the printed value is ");
println!("{}", x%m);
```
Usually we want the remainder to always be between $0...m-1$. However, in Rust and other languages, the remainder of a negative number is either zero or negative. An easy way to make sure there are no negative remainders is to first calculate the remainder as usual and then add $m$ if the result is negative:
```rust, ignore
x = x%m;
if x<0 {x += m};
```
However, this is only needed when there are subtractions in the code and the remainder may become negative.

## Floating point numbers

The usual floating point types in competitive programming are the 64-bit `f64`.
The required precision of the answer is usually given in the problem statement.
An easy way to output the answer is to use the  function and give the number of decimal places in the formatting string. For example, the following
code prints the value of x with 9 decimal places:
```rust, ignore
println!("x:.9");
```
A difficulty when using floating point numbers is that some numbers cannot be represented accurately as floating point numbers, and there will be rounding errors.
For example, the result of the following code is surprising:
```rust
let x: f64 = 0.3*3.0+0.1;
println!("{x}"); // 0.9999999999999999
```
Due to a rounding error, the value of $x$ is a bit smaller than 1, while the correct value would be 1.

> note that
>   ```rust, compile_fail
>   let x: f64 = 0.3 * 3 * 0.1;
>   //_________________^__it must be 3.0
>   ```
> fails to compile because `3` without the dot is not cast in `f64`

It is risky to compare floating point numbers with the `==` operator, because it is possible that the values should be equal but they are not because of precision errors.
A better way to compare floating point numbers is to assume that two numbers are equal if the difference between them is less than $\epsilon$, where $\epsilon$ is a small number.
In practice, the numbers can be compared as follows ($\epsilon = 10^{-9}$):
```rust, ignore
if (num::abs(a-b) < 1e-9){
    //a and b are aproximately equal
}
```
