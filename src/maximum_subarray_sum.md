# Maximum subarray sum

There are often several possible algorithms for solving a problem such that their
time complexities are different.
This section discusses a classic problem that has a straightforward $O(n^3)$ solution.
However, by designing a better algorithm, it is possible to solve the problem in $O(n^2)$ time and even in $O(n)$ time.

Given an array of $n$ numbers, our task is to calculate the _maximum subarray sum_, i.e., the largest possible sum of a sequence of consecutive values in the array[^1].

The problem is interesting when there may be negative values in the array.
For example, in the array

| -1 | 2 | 4 | -3 | 5 | 2 | -5 | 2 |
| --- | --- | --- | --- | --- | --- | --- | --- |

the following subarray produces the maximum sum $10$:

| --- | 2 | 4 | -3 | 5 | 2 | --- | --- |
| --- | --- | --- | --- | --- | --- | --- | --- |

We assume that an empty subarray is allowed,
so the maximum subarray sum is always at least $0$.

## Algorithm 1

A straightforward way to solve the problem is to go through all possible subarrays, calculate the sum of values in each subarray and maintain the maximum sum.
The following code implements this algorithm:

```rust
# use std::cmp::max;
# use std::time::Instant;
# let array: Vec<i32> = vec![-1, 2, 4, -3, 5, 2, -5, 2];
# let n = array.len();
# let start = Instant::now();
let mut best = 0;
for a in 0..n{
    for b in a..n {
        let mut sum = 0;
        for k in a..b{
            sum += array[k];
        }
        best = max(best, sum);
    }
}
println!("{best}");
# println!("Execution time: {:?}", start.elapsed());
```
The variables `a` and `b` fix the first and last index of the subarray,
and the sum of values is calculated to the variable `sum`.
The variable `best` contains the maximum sum found during the search.

The time complexity of the algorithm is $O(n^3)$, because it consists of three nested loops that go through the input.


## Algorithm 2

It is easy to make Algorithm 1 more efficient
by removing one loop from it.
This is possible by calculating the sum at the same
time when the right end of the subarray moves.
The result is the following code:

```rust
# use std::cmp::max;
# use std::time::Instant;
# let array: Vec<i32> = vec![-1, 2, 4, -3, 5, 2, -5, 2];
# let n = array.len();
# let start = Instant::now();
let mut best = 0;
for a in 0..n {
    let mut sum = 0;
    for b in a..n {
        sum += array[b];
        best = max(best,sum);
    }
}
println!("{best}");
# println!("Execution time: {:?}", start.elapsed());
```
After this change, the time complexity is $O(n^2)$.

## Algorithm 3

Surprisingly, it is possible to solve the problem in $O(n)$ time[^2], which means
that just one loop is enough.
The idea is to calculate, for each array position, the maximum sum of a subarray that ends at that position.
After this, the answer for the problem is the maximum of those sums.

Consider the subproblem of finding the maximum-sum subarray that ends at position $k$.
There are two possibilities:
1. The subarray only contains the element at position $k$.
2. The subarray consists of a subarray that ends
at position $k-1$, followed by the element at position $k$.

In the latter case, since we want to find a subarray with maximum sum, the subarray that ends at position $k-1$ should also have the maximum sum.
Thus, we can solve the problem efficiently by calculating the maximum subarray sum
for each ending position from left to right.

The following code implements the algorithm:
```rust
# use std::cmp::max;
# use std::time::Instant;
# let array: Vec<i32> = vec![-1, 2, 4, -3, 5, 2, -5, 2];
# let n = array.len();
# let start = Instant::now();
let mut best = 0;
let mut sum = 0;
for k in 0..n {
    sum = max(array[k],sum+array[k]);
    best = max(best,sum);
}
println!("{best}");
# println!("Execution time: {:?}", start.elapsed());
```

The algorithm only contains one loop that goes through the input, so the time complexity is $O(n)$.
This is also the best possible time complexity, because any algorithm for the problem has to examine all array elements at least once.

## Efficiency comparison

It is interesting to study how efficient algorithms are in practice.
The following table shows the running times of the above algorithms for different
values of $n$ on a modern computer.

In each test, the input was generated randomly.
The time needed for reading the input was not measured.

| array size $n$ | Algorithm 1 | Algorithm 2 | Algorithm 3 |
| ---: | ---: | ---: | ---: |
| $10^2$ | $0.0$ s | $0.0$ s | $0.0$ s |
| $10^3$ | $0.1$ s | $0.0$ s | $0.0$ s |
| $10^4$ | > $10.0$ s | $0.1$ s | $0.0$ s |
| $10^5$ | > $10.0$ s | $5.3$ s | $0.0$ s |
| $10^6$ | > $10.0$ s | > $10.0$ s | $0.0$ s |
| $10^7$ | > $10.0$ s | > $10.0$ s | $0.0$ s |

The comparison shows that all algorithms are efficient when the input size is small, but larger inputs bring out remarkable differences in the running times of the algorithms.
Algorithm 1 becomes slow when $n=10^4$, and Algorithm 2 becomes slow when $n=10^5$.
Only Algorithm 3 is able to process even the largest inputs instantly.

___

[^1] J. Bentley's book _Programming Pearls_ [8] made the problem popular.

[^2] In [8], this linear-time algorithm is attributed to J. B. Kadane, and the algorithm is sometimes called **Kadane’s algorithm**.
