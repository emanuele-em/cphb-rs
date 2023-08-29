# Time complexity

The efficiency of algorithms is important in competitive programming.
Usually, it is easy to design an algorithm that solves the problem slowly, but the real challenge is to invent a fast algorithm.
If the algorithm is too slow, it will get only partial points or no points at all.
The time complexity of an algorithm estimates how much time the algorithm will use for some input.
The idea is to represent the efficiency as a function whose parameter is the size of the input.
By calculating the time complexity, we can find out whether the algorithm is fast enough without implementing it.


## Calculation rules

The time complexity of an algorithm is denoted $O(\cdots)$ where the three dots represent some function.
Usually, the variable $n$ denotes the input size.
For example, if the input is an array of numbers, $n$ will be the size of the array, and if the input is a string, $n$ will be the length of the string.

## Loops

A common reason why an algorithm is slow is that it contains many loops that go through the input.
The more nested loops the algorithm contains, the slower it is.
If there are $k$ nested loops, the time complexity is $O(n^k)$.

For example, the time complexity of the following code is $O(n)$:
```rust
# let n = 10;
for i in 1..=n {
    // code
}
```
And the time complexity of the following code is $O(n^2)$:
```rust
# let n = 10;
for i in 1..=n {
    for j in 1..=n {
        // code
    }
}
```
## Order of magnitude
A time complexity does not tell us the exact number of times the code inside a loop is executed, but it only shows the order of magnitude.
In the following examples, the code inside the loop is executed $3n$, $n+5$ and $\lceil n/2 \rceil$ times,
but the time complexity of each code is $O(n)$.

```rust
# let n = 10;
for i in 1..=n {
    // code
}
for i in 0..=n {
    // code
}
```
As another example, the time complexity of the following code is $O(n^2)$:
```rust
# let n = 10;
 for i in 1..=n {
    for j in i+1..=n {
        // code
    }
}
```
## Phases

If the algorithm consists of consecutive phases, the total time complexity is the largest time complexity of a single phase.
The reason for this is that the slowest phase is usually the bottleneck of the code.

For example, the following code consists of three phases with time complexities
$O(n)$, $O(n^2)$ and $O(n)$.
Thus, the total time complexity is $O(n^2)$.

```rust
# let n = 10;
for i in 1..=n {
    // code
}
for i in 1..=n {
    for j in 1..=n {
        // code
    }
}
for i in 1..=n {
    // code
}
```
## Several Variables

Sometimes the time complexity depends on several factors.
In this case, the time complexity formula contains several variables.

For example, the time complexity of the following code is $O(nm)$:

```rust
# let n = 10; let m = 10;
for i in 1..=n {
    for j in 1..=m {
        // code
    }
}
```
## Recursion

The time complexity of a recursive function depends on the number of times the function is called and the time complexity of a single call.
The total time complexity is the product of these values.

For example, consider the following function:
```rust
fn f(n: i32){
    if n == 1 {return}
    f(n-1);
}
```
The call $\texttt{f}(n)$ causes $n$ function calls, and the time complexity of each call is $O(1)$.
Thus, the total time complexity is $O(n)$.

As another example, consider the following function:
```rust
fn g(n: i32){
    if n == 1 {return}
    g(n-1);
    g(n-1);
}
```
In this case each function call generates two other calls, except for $n=1$.
Let us see what happens when $g$ is called with parameter $n$.
The following table shows the function calls produced by this single call:

| function call | number of calls |
| ------------: | :---------------: |
| $g(n)$ | 1 |
| $g(n-1)$ | 2 |
| $g(n-2)$ | 4 |
| $\cdots$ | $\cdots$ |
| $g(1)$ | $2^{n-1}$ |

Based on this, the time complexity is
$$
1+2+4+\cdots+2^{n-1} = 2^n-1 = O(2^n)
$$
