# Coin problem

We first focus on a problem that we
have already seen in Chapter 6:
Given a set of coin values $\texttt{coins} = \{c_1,c_2,\ldots,c_k\}$
and a target sum of money $n$, our task is to
form the sum $n$ using as few coins as possible.

In Chapter 6, we solved the problem using a
greedy algorithm that always chooses the largest
possible coin.
The greedy algorithm works, for example,
when the coins are the euro coins,
but in the general case the greedy algorithm
does not necessarily produce an optimal solution.

Now is time to solve the problem efficiently
using dynamic programming, so that the algorithm
works for any coin set.
The dynamic programming
algorithm is based on a recursive function
that goes through all possibilities how to
form the sum, like a brute force algorithm.
However, the dynamic programming
algorithm is efficient because
it uses _memoization_ and
calculates the answer to each subproblem only once.

## Recursive formulation

The idea in dynamic programming is to
formulate the problem recursively so
that the solution to the problem can be
calculated from solutions to smaller
subproblems.
In the coin problem, a natural recursive
problem is as follows:
what is the smallest number of coins
required to form a sum $x$?

Let $\texttt{solve}(x)$
denote the minimum
number of coins required for a sum $x$.
The values of the function depend on the
values of the coins.
For example, if $\texttt{coins} = \{1,3,4\}$,
the first values of the function are as follows:

$$
solve(0) = 0 \\
solve(1) = 1 \\
solve(2) = 2 \\
solve(3) = 1  \\
solve(4) = 1  \\
solve(5) = 2  \\
solve(6) = 2  \\
solve(7) = 2  \\
solve(8) = 2  \\
solve(9) = 3  \\
solve(10) = 3  \\
$$

For example, $\texttt{solve}(10)=3$,
because at least 3 coins are needed
to form the sum 10.
The optimal solution is $3+3+4=10$.

The essential property of $\texttt{solve}$ is
that its values can be
recursively calculated from its smaller values.
The idea is to focus on the _first_
coin that we choose for the sum.
For example, in the above scenario,
the first coin can be either 1, 3 or 4.
If we first choose coin 1,
the remaining task is to form the sum 9
using the minimum number of coins,
which is a subproblem of the original problem.
Of course, the same applies to coins 3 and 4.
Thus, we can use the following recursive formula
to calculate the minimum number of coins:

$\texttt{solve}(x) = \min( \texttt{solve}(x-1)+1, \texttt{solve}(x-3)+1, \texttt{solve}(x-4)+1)$

The base case of the recursion is $\texttt{solve}(0)=0$,
because no coins are needed to form an empty sum.
For example,

$\texttt{solve}(10) = \texttt{solve}(7)+1 = \texttt{solve}(4)+2 = \texttt{solve}(0)+3 = 3$

Now we are ready to give a general recursive function
that calculates the minimum number of
coins needed to form a sum $x$:

\\[
\texttt{solve}(x) = \begin{cases}
               \infty               & x < 0\\\\
               0               & x = 0\\\\
               \min_{ c \in \texttt{coins}} \texttt{solve}(x-c)+1 & x > 0 \\\\
           \end{cases}
\\]

First, if $x<0$, the value is $\infty$,
because it is impossible to form a negative
sum of money.
Then, if $x=0$, the value is $0$,
because no coins are needed to form an empty sum.
Finally, if $x>0$, the variable $c$ goes through
all possibilities how to choose the first coin
of the sum.

Once a recursive function that solves the problem
has been found,
we can directly implement a solution in Rust
(the constant `INF` denotes infinity):

```rust
# use std::cmp::{self, Ordering};
# use std::isize::MAX;
# const INF:isize = 999999;
# let coins = [1,3,4];
# let x = 10;
# println!("coins: {coins:?}");
# println!("x: {x}");
# println!("solution: {}", solve(x, &coins));

fn solve(x: isize, coins: &[isize]) -> isize{
    match x.cmp(&0) {
        Ordering::Equal => 0,
        Ordering::Less => INF,
        _ => {
            let mut best = INF;
            for c in coins {
                best = cmp::min(best, solve(x-c, coins)+1);
            }
            best
        }
    }
}
```

Still, this function is not efficient,
because there may be an exponential number of ways
to construct the sum.
However, next we will see how to make the
function efficient using a technique called memoization.

## Using Memoization

The idea of dynamic programming is to use
**memoization** to efficiently calculate
values of a recursive function.
This means that the values of the function
are stored in an HashMap after calculating them.
For each parameter, the value of the function
is calculated recursively only once, and after this,
the value can be directly retrieved from the HashMap.

In this problem, we use HashMaps
```rust
# const N: usize = 10;
let ready = HashMap::new();
# println!("ready: {ready:?}");
```

where $\texttt{ready}[x]$ indicates
whether the value of $\texttt{solve}(x)$ has been calculated,
and if it is, $\texttt{ready}[x]$
contains this value.

Now the function can be efficiently
implemented as follows:

```rust
# use std::cmp::{self, Ordering};
# use std::isize::MAX;
# use std::collections::HashMap;
# const INF:isize = 999999;
# let coins = [1,3,4];
# let x = 10;
# let mut ready = HashMap::new();
# println!("coins: {coins:?}");
# println!("x: {x}");
# println!("solution: {}", solve(x, &mut ready, &coins));

fn solve(x: isize, ready: &mut HashMap<isize, isize>, coins: &[isize]) -> isize{
    match x.cmp(&0){
        Ordering::Less => INF,
        Ordering::Equal => 0,
        _ => {
            match ready.get(&x) {
                Some(&x) => x,
                _ => {
                    let mut best = INF;
                    for c in coins {
                        best = cmp::min(best, solve(x-c, ready, coins)+1);
                    }
                    ready.insert(x, best);
                    best
                }
            }
        }
    }
}
```

The function handles the base cases
$x<0$ and $x=0$ as previously.
Then the function checks if
$\texttt{solve}(x)$ has already been stored
in $\texttt{ready}[x]$,
and if it is, the function directly returns it.
Otherwise the function calculates the value
of $\texttt{solve}(x)$
recursively and stores it in $\texttt{ready}[x]$.

This function works efficiently,
because the answer for each parameter $x$
is calculated recursively only once.
After a value of $\texttt{solve}(x)$ has been stored in $\texttt{ready}[x]$,
it can be efficiently retrieved whenever the
function will be called again with the parameter $x$.
The time complexity of the algorithm is $O(nk)$,
where $n$ is the target sum and $k$ is the number of coins.

Note that we can also _iteratively_
construct the HashMap _value_ using
a loop that simply calculates all the values
of $\texttt{solve}$ for parameters $0 \ldots n$:
```rust
# use std::collections::HashMap;
# use std::cmp;
# const INF:isize = 999999;
# let coins = [1,3,4];
# let x = 10;
# println!("coins: {coins:?}");
# println!("x: {x}");
let mut ready = HashMap::new();
ready.insert(0, 0);
for i in 1..=x {
    let mut best = INF;
    for c in coins {
        if i >= c {
            if let Some(&value) = ready.get(&(i - c)) {
                ready.insert(i, cmp::min(best, value + 1));
            }
        }
    }
}
# println!("solution: {ready:#?}");
```


In fact, most competitive programmers prefer this
implementation, because it is shorter and has
lower constant factors.
From now on, we also use iterative implementations
in our examples.
Still, it is often easier to think about
dynamic programming solutions
in terms of recursive functions.

## Constructing a Solution

Sometimes we are asked both to find the value
of an optimal solution and to give
an example how such a solution can be constructed.
In the coin problem, for example,
we can declare another collection
that indicates for
each sum of money the first coin 
in an optimal solution:
```rust, ignore
let mut first = HashMap::new();
```
Then, we can modify the algorithm as follows:
```rust
# use std::collections::HashMap;
# use std::cmp;
# const INF:isize = 999999;
# let coins = [1,3,4];
# let x = 10;
# println!("coins: {coins:?}");
# println!("x: {x}");
let mut ready = HashMap::new();
let mut first = HashMap::new();
ready.insert(0, 0);
for i in 1..=x {
    let mut best = INF;
    for c in coins {
        if i >= c {
            if let Some(&value) = ready.get(&(i - c)) {
                ready.insert(i, cmp::min(best, value + 1));
                first.insert(i, c);
            }
        }
    }
}
# println!("Solution: {ready:#?}");
# println!("First: {first:#?}");
```

## Counting the number of solutions

Let us now consider another version
of the coin problem where our task is to
calculate the total number of ways
to produce a sum $x$ using the coins.
For example, if $\texttt{coins}=\{1,3,4\}$ and
$x=5$, there are a total of 6 ways:

- $1+1+1+1+1$
- $1+1+3$
- $1+3+1$
- $3+1+1$
- $1+4$
- $4+1$

Again, we can solve the problem recursively.
Let $\texttt{solve}(x)$ denote the number of ways
we can form the sum $x$.
For example, if $\texttt{coins}=\{1,3,4\}$,
then $\texttt{solve}(5)=6$ and the recursive formula is:

$$
\begin{equation*}
\begin{split}
\texttt{solve}(x) = & \texttt{solve}(x-1) + \\\\
                    & \texttt{solve}(x-3) + \\\\
                    & \texttt{solve}(x-4)  .
\end{split}
\end{equation*}
$$

Then, the general recursive function is as follows:

$$
\begin{equation*}
    \texttt{solve}(x) = \begin{cases}
               0               & x < 0\\\\
               1               & x = 0\\\\
               \sum_{c \in \texttt{coins}} \texttt{solve}(x-c) & x > 0 \\\\
           \end{cases}
\end{equation*}
$$

If $x<0$, the value is 0, because there are no solutions.
If $x=0$, the value is 1, because there is only one way
to form an empty sum.
Otherwise we calculate the sum of all values
of the form $\texttt{solve}(x-c)$ where $c$ is in \texttt{coins}.

The following code constructs an array
$\texttt{count}$ such that
$\texttt{count}[x]$ equals
the value of $\texttt{solve}(x)$
for $0 \le x \le n$:

```rust
# use std::collections::HashMap;
# use std::cmp;
# const INF:isize = 999999;
# let coins = [1,3,4];
# let x = 10;
# println!("coins: {coins:?}");
# println!("x: {x}");
let mut ready = HashMap::new();
let mut first = HashMap::new();
let mut count = HashMap::new();
ready.insert(0, 0);
for i in 1..=x {
    let mut best = INF;
    for c in coins {
        if i >= c {
            if let Some(&value) = ready.get(&(i - c)) {
                ready.insert(i, cmp::min(best, value + 1));
                first.insert(i, c);
                *count.entry(i).or_insert(1) += value;
            }
        }
    }
}
# println!("Solution: {ready:#?}");
# println!("First: {first:#?}");
# println!("Count: {count:#?}");
```
