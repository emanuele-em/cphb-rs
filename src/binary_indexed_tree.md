# Binary indexed tree

A **binary indexed tree** or a **Fenwick tree** [^1] can be seen as a dynamic variant of a prefix sum array.
It supports two $O(\log n)$ time operations on an array:
processing a range sum query and updating a value.

The advantage of a binary indexed tree is
that it allows us to efficiently update
array values between sum queries.
This would not be possible using a prefix sum array,
because after each update, it would be necessary to build the
whole prefix sum array again in $O(n)$ time.

## Structure

Even if the name of the structure is a binary indexed _tree_,
it is usually represented as an array.
In this section we assume that all arrays are one-indexed,
because it makes the implementation easier.

Let $p(k)$ denote the largest power of two that
divides $k$.
We store a binary indexed tree as an array _tree_
such that

\\[
\\texttt{tree}[k] = \\texttt{sum}_q(k-p(k)+1,k)
\\]

i.e., each position $k$ contains the sum of values
in a range of the original array whose length is $p(k)$
and that ends at position $k$.
For example, since $p(6)=2$, \\( \texttt{tree}[6] \\)
contains the value of $sum_q(5,6)$.

For example, consider the following array:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {8};
\node at (4.5,0.5) {6};
\node at (5.5,0.5) {1};
\node at (6.5,0.5) {4};
\node at (7.5,0.5) {2};

\footnotesize
\node at (0.5,1.4) {1};
\node at (1.5,1.4) {2};
\node at (2.5,1.4) {3};
\node at (3.5,1.4) {4};
\node at (4.5,1.4) {5};
\node at (5.5,1.4) {6};
\node at (6.5,1.4) {7};
\node at (7.5,1.4) {8};
\end{tikzpicture}
</script>

The corresponding binary indexed tree is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {4};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {16};
\node at (4.5,0.5) {6};
\node at (5.5,0.5) {7};
\node at (6.5,0.5) {4};
\node at (7.5,0.5) {29};

\footnotesize
\node at (0.5,1.4) {1};
\node at (1.5,1.4) {2};
\node at (2.5,1.4) {3};
\node at (3.5,1.4) {4};
\node at (4.5,1.4) {5};
\node at (5.5,1.4) {6};
\node at (6.5,1.4) {7};
\node at (7.5,1.4) {8};
\end{tikzpicture}
</script>

The following picture shows more clearly
how each value in the binary indexed tree
corresponds to a range in the original array:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {4};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {16};
\node at (4.5,0.5) {6};
\node at (5.5,0.5) {7};
\node at (6.5,0.5) {4};
\node at (7.5,0.5) {29};

\footnotesize
\node at (0.5,1.4) {1};
\node at (1.5,1.4) {2};
\node at (2.5,1.4) {3};
\node at (3.5,1.4) {4};
\node at (4.5,1.4) {5};
\node at (5.5,1.4) {6};
\node at (6.5,1.4) {7};
\node at (7.5,1.4) {8};

\draw[->,thick] (0.5,-0.9) -- (0.5,-0.1);
\draw[->,thick] (2.5,-0.9) -- (2.5,-0.1);
\draw[->,thick] (4.5,-0.9) -- (4.5,-0.1);
\draw[->,thick] (6.5,-0.9) -- (6.5,-0.1);
\draw[->,thick] (1.5,-1.9) -- (1.5,-0.1);
\draw[->,thick] (5.5,-1.9) -- (5.5,-0.1);
\draw[->,thick] (3.5,-2.9) -- (3.5,-0.1);
\draw[->,thick] (7.5,-3.9) -- (7.5,-0.1);

\draw (0,-1) -- (1,-1) -- (1,-1.5) -- (0,-1.5) -- (0,-1);
\draw (2,-1) -- (3,-1) -- (3,-1.5) -- (2,-1.5) -- (2,-1);
\draw (4,-1) -- (5,-1) -- (5,-1.5) -- (4,-1.5) -- (4,-1);
\draw (6,-1) -- (7,-1) -- (7,-1.5) -- (6,-1.5) -- (6,-1);
\draw (0,-2) -- (2,-2) -- (2,-2.5) -- (0,-2.5) -- (0,-2);
\draw (4,-2) -- (6,-2) -- (6,-2.5) -- (4,-2.5) -- (4,-2);
\draw (0,-3) -- (4,-3) -- (4,-3.5) -- (0,-3.5) -- (0,-3);
\draw (0,-4) -- (8,-4) -- (8,-4.5) -- (0,-4.5) -- (0,-4);
\end{tikzpicture}
</script>

Using a binary indexed tree,
any value of $\texttt{sum}_q(1,k)$
can be calculated in $O(\log n)$ time,
because a range \\( [1,k] \\) can always be divided into
$O(\log n)$ ranges whose sums are stored in the tree.

For example, the range \\( [1,7] \\) consists of
the following ranges:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {4};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {16};
\node at (4.5,0.5) {6};
\node at (5.5,0.5) {7};
\node at (6.5,0.5) {4};
\node at (7.5,0.5) {29};

\footnotesize
\node at (0.5,1.4) {1};
\node at (1.5,1.4) {2};
\node at (2.5,1.4) {3};
\node at (3.5,1.4) {4};
\node at (4.5,1.4) {5};
\node at (5.5,1.4) {6};
\node at (6.5,1.4) {7};
\node at (7.5,1.4) {8};

\draw[->,thick] (0.5,-0.9) -- (0.5,-0.1);
\draw[->,thick] (2.5,-0.9) -- (2.5,-0.1);
\draw[->,thick] (4.5,-0.9) -- (4.5,-0.1);
\draw[->,thick] (6.5,-0.9) -- (6.5,-0.1);
\draw[->,thick] (1.5,-1.9) -- (1.5,-0.1);
\draw[->,thick] (5.5,-1.9) -- (5.5,-0.1);
\draw[->,thick] (3.5,-2.9) -- (3.5,-0.1);
\draw[->,thick] (7.5,-3.9) -- (7.5,-0.1);

\draw (0,-1) -- (1,-1) -- (1,-1.5) -- (0,-1.5) -- (0,-1);
\draw (2,-1) -- (3,-1) -- (3,-1.5) -- (2,-1.5) -- (2,-1);
\draw (4,-1) -- (5,-1) -- (5,-1.5) -- (4,-1.5) -- (4,-1);
\draw[fill=lightgray] (6,-1) -- (7,-1) -- (7,-1.5) -- (6,-1.5) -- (6,-1);
\draw (0,-2) -- (2,-2) -- (2,-2.5) -- (0,-2.5) -- (0,-2);
\draw[fill=lightgray] (4,-2) -- (6,-2) -- (6,-2.5) -- (4,-2.5) -- (4,-2);
\draw[fill=lightgray] (0,-3) -- (4,-3) -- (4,-3.5) -- (0,-3.5) -- (0,-3);
\draw (0,-4) -- (8,-4) -- (8,-4.5) -- (0,-4.5) -- (0,-4);
\end{tikzpicture}
</script>

Thus, we can calculate the corresponding sum as follows:
\\[
\\texttt{sum}_q(1,7)=\\texttt{sum}_q(1,4)+\\texttt{sum}_q(5,6)+\\texttt{sum}_q(7,7)=16+7+4=27
\\]

To calculate the value of $sum_q(a,b)$ where $a>1$,
we can use the same trick that we used with prefix sum arrays:

\\[ \\texttt{sum}_q(a,b) = \\texttt{sum}_q(1,b) - \\texttt{sum}_q(1,a-1).\\]

Since we can calculate both $sum_q(1,b)$
and $sum_q(1,a-1)$ in $O(\log n)$ time,
the total time complexity is $O(\log n)$.

Then, after updating a value in the original array,
several values in the binary indexed tree
should be updated.
For example, if the value at position 3 changes,
the sums of the following ranges change:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {4};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {16};
\node at (4.5,0.5) {6};
\node at (5.5,0.5) {7};
\node at (6.5,0.5) {4};
\node at (7.5,0.5) {29};

\footnotesize
\node at (0.5,1.4) {1};
\node at (1.5,1.4) {2};
\node at (2.5,1.4) {3};
\node at (3.5,1.4) {4};
\node at (4.5,1.4) {5};
\node at (5.5,1.4) {6};
\node at (6.5,1.4) {7};
\node at (7.5,1.4) {8};

\draw[->,thick] (0.5,-0.9) -- (0.5,-0.1);
\draw[->,thick] (2.5,-0.9) -- (2.5,-0.1);
\draw[->,thick] (4.5,-0.9) -- (4.5,-0.1);
\draw[->,thick] (6.5,-0.9) -- (6.5,-0.1);
\draw[->,thick] (1.5,-1.9) -- (1.5,-0.1);
\draw[->,thick] (5.5,-1.9) -- (5.5,-0.1);
\draw[->,thick] (3.5,-2.9) -- (3.5,-0.1);
\draw[->,thick] (7.5,-3.9) -- (7.5,-0.1);

\draw (0,-1) -- (1,-1) -- (1,-1.5) -- (0,-1.5) -- (0,-1);
\draw[fill=lightgray] (2,-1) -- (3,-1) -- (3,-1.5) -- (2,-1.5) -- (2,-1);
\draw (4,-1) -- (5,-1) -- (5,-1.5) -- (4,-1.5) -- (4,-1);
\draw (6,-1) -- (7,-1) -- (7,-1.5) -- (6,-1.5) -- (6,-1);
\draw (0,-2) -- (2,-2) -- (2,-2.5) -- (0,-2.5) -- (0,-2);
\draw (4,-2) -- (6,-2) -- (6,-2.5) -- (4,-2.5) -- (4,-2);
\draw[fill=lightgray] (0,-3) -- (4,-3) -- (4,-3.5) -- (0,-3.5) -- (0,-3);
\draw[fill=lightgray] (0,-4) -- (8,-4) -- (8,-4.5) -- (0,-4.5) -- (0,-4);
\end{tikzpicture}
</script>

Since each array element belongs to $O(\log n)$
ranges in the binary indexed tree,
it suffices to update $O(\log n)$ values in the tree.

## Implementation

The operations of a binary indexed tree can be
efficiently implemented using bit operations.
The key fact needed is that we can
calculate any value of $p(k)$ using the formula
\\[p(k) = k \\& -k.\\]

The following function calculates the value of $sum_q(1,k)$:

```rust
# let v = vec![1,3,4,8,6,1,4,2];
# let tree = vec![1,4,4,16,6,7,4,29];
# let mut k = 7;
# println!{"{:?}", tree.clone()};
# println!{"k = {k}"};
# let sum = sum(k, tree);
# println!{"{:?}", sum};

fn sum(mut k: isize, tree: Vec<isize>) -> isize{
    let mut s = 0;
    while k>=1 {
        s += tree[k as usize -1];
        k -= k & -k;
    }
    s
}
```

The following function increases the
array value at position $k$ by $x$
($x$ can be positive or negative):
```rust
# let v = vec![1,3,4,8,6,1,4,2];
# let mut tree = vec![1,4,4,16,6,7,4,29];
# let mut k = 1;
# let mut x = 2;
# println!{"before: {:?}", tree.clone()};
# println!{"k = {k}"};
# println!{"x = {x}"};
# let sum = add(&mut tree, k, x);
# println!{"after: {:?}", tree};
fn add(tree: &mut Vec<isize>, mut k: isize, x: isize){
    while (k as usize <= tree.len()) {
        tree[k as usize -1] += x;
        k += k&-k;
    }
}
```

The time complexity of both the functions is
$O(\log n)$, because the functions access $O(\log n)$
values in the binary indexed tree, and each move
to the next position takes $O(1)$ time.


__

[^1] The binary indexed tree structure was presented by P. M. Fenwick in 1994 [21].
