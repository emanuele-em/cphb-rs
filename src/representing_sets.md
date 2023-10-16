#  Representing sets

Every subset of a set
$\{0,1,2,\ldots,n-1\}$
can be represented as an $n$ bit integer
whose one bits indicate which
elements belong to the subset.
This is an efficient way to represent sets because operations can be implemented as bit operations.

For example, since **i32** is a 32-bit type,
an **i32** number can represent any subset
of the set $\{0,1,2,\ldots,31\}$.
The bit representation of the set $\{1,3,4,8\}$ is

$$
00000000000000000000000100011010
$$

which corresponds to the number $2^8+2^4+2^3+2^1=282$.

```rust
println!("{}", 0b00000000000000000000000100011010);
```

## Set implementation

The following code declares an _i32_
variable $x$ that can contain
a subset of $\{0,1,2,\ldots,31\}$.
After this, the code adds the elements 1, 3, 4 and 8
to the set and prints the size of the set.

```rust
let mut x = 0_i32;
x |= (1<<1);
x |= (1<<3);
x |= (1<<4);
x |= (1<<8);
println!("{:?}", x.count_ones());
```
Then, the following code prints all
elements that belong to the set:

```rust
# let mut x = 0;
# x |= (1<<1);
# x |= (1<<3);
# x |= (1<<4);
# x |= (1<<8);
for i in 0..32 {
    if x&(1<<i) != 0 {println!("{i}")}
}
```

## Set operations

Set operations can be implemented as follows as bit operations:


| operation | set syntax | bit syntax |
|---|:---:|:---:|
|intersection | $a \cap b$ | $a$ \& $b$ |
|union | $a \cup b$ | $a$ | $b$ |
|complement | $\bar a$ | ~$a$ |
|difference | $a \setminus b$ | $a$ \& (~$b$) |

For example, the following code first constructs
the sets $x=\{1,3,4,8\}$ and $y=\{3,6,8,9\}$,
and then constructs the set $z = x \cup y = \{1,3,4,6,8,9\}$:

```rust
let x = (1<<1)|(1<<3)|(1<<4)|(1<<8);
let y = (1<<3)|(1<<6)|(1<<8)|(1<<9);
let z: i32 = x|y;
# println!("x => {x:010b}");
# println!("y => {y:b}");
# println!("z => {z:b}");
println!("{}", z.count_ones());
```

## Iterating through subsets

The following code goes through
the subsets of $\{0,1,\ldots,n-1\}$:

```rust
# let n = 10;
let mut b=0;
while b < (1<<n) {
    // process subset b
    # println!("b={b}, n={n}");
    b+=1;
}
```

The following code goes through
the subsets with exactly $k$ elements:

```rust
let mut b = 0_i32;
# let k = 4;
# let n = 10;
while b < (1<<n) {
    if (b.count_ones() == k) {
        # println!("b={b}, k={k}");
        // process subset b
    }
    b+=1;
}
```
The following code goes through the subsets
of a set $x$:

```rust
let mut b = 0;
# let x = 10;
loop {
    // process subset b
    # println!("b={b}, x={x}");
    b = (b-x)&x; 
    if b == 0 {break;}
}
```
