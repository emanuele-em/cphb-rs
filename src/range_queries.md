# Range queries

In this chapter, we discuss data structures
that allow us to efficiently process range queries.
In a **range query**,
our task is to calculate a value
based on a subarray of an array.
Typical range queries are:

- $\texttt{sum}_q(a,b)$: calculate the sum of values in range \\([a,b]\\)
- $\texttt{min}_q(a,b)$: find the minimum value in range \\([a,b]\\)
- $\texttt{max}_q(a,b)$: find the maximum value in range \\([a,b]\\)

For example, consider the range \\([3,6]\\) in the following array:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (3,0) rectangle (7,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {8};
\node at (3.5,0.5) {4};
\node at (4.5,0.5) {6};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {3};
\node at (7.5,0.5) {4};

\footnotesize
\node at (0.5,1.4) {0};
\node at (1.5,1.4) {1};
\node at (2.5,1.4) {2};
\node at (3.5,1.4) {3};
\node at (4.5,1.4) {4};
\node at (5.5,1.4) {5};
\node at (6.5,1.4) {6};
\node at (7.5,1.4) {7};
\end{tikzpicture}
</script>

In this case, $sum_q(3,6)=14$,
$min_q(3,6)=1$ and $max_q(3,6)=6$.

Best way to work with ranges in Rust is to use iterators.
For example, the following function can be
used to process sum queries on an array:

```rust
# let array = vec![1,3,8,4,6,1,3,4];
# let a = 3;
# let b = 6;
fn sum(array: Vec<i32>, a:usize, b:usize) -> i32{
    array[a..=b].iter().sum()
}
# println!("array: {array:?}");
# println!("sum from index {} to index {}: {}",a,b,sum(array, a,b));
```

