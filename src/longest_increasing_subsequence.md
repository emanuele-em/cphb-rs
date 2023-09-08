# Longest increasing subsequence

Our first problem is to find the
**longest increasing subsequence**
in an array of $n$ elements.
This is a maximum-length
sequence of array elements
that goes from left to right,
and each element in the sequence is larger
than the previous element.
For example, in the array

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);
\node at (0.5,0.5) {6};
\node at (1.5,0.5) {2};
\node at (2.5,0.5) {5};
\node at (3.5,0.5) {1};
\node at (4.5,0.5) {7};
\node at (5.5,0.5) {4};
\node at (6.5,0.5) {8};
\node at (7.5,0.5) {3};

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

the longest increasing subsequence
contains 4 elements:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (1,0) rectangle (2,1);
\fill[color=lightgray] (2,0) rectangle (3,1);
\fill[color=lightgray] (4,0) rectangle (5,1);
\fill[color=lightgray] (6,0) rectangle (7,1);
\draw (0,0) grid (8,1);
\node at (0.5,0.5) {6};
\node at (1.5,0.5) {2};
\node at (2.5,0.5) {5};
\node at (3.5,0.5) {1};
\node at (4.5,0.5) {7};
\node at (5.5,0.5) {4};
\node at (6.5,0.5) {8};
\node at (7.5,0.5) {3};

\draw[thick,->] (1.5,-0.25) .. controls (1.75,-1.00) and (2.25,-1.00) .. (2.4,-0.25);
\draw[thick,->] (2.6,-0.25) .. controls (3.0,-1.00) and (4.0,-1.00) .. (4.4,-0.25);
\draw[thick,->] (4.6,-0.25) .. controls (5.0,-1.00) and (6.0,-1.00) .. (6.5,-0.25);

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

Let $\texttt{length}(k)$ denote
the length of the
longest increasing subsequence
that ends at position $k$.
Thus, if we calculate all values of
$\texttt{length}(k)$ where $0 \le k \le n-1$,
we will find out the length of the
longest increasing subsequence.
For example, the values of the function
for the above array are as follows:

\\[
\begin{array}{lcl}
\texttt{length}(0) & = & 1 \\\\
\texttt{length}(1) & = & 1 \\\\
\texttt{length}(2) & = & 2 \\\\
\texttt{length}(3) & = & 1 \\\\
\texttt{length}(4) & = & 3 \\\\
\texttt{length}(5) & = & 2 \\\\
\texttt{length}(6) & = & 4 \\\\
\texttt{length}(7) & = & 2 \\\\
\end{array}
\\]

For example, $\texttt{length}(6)=4$,
because the longest increasing subsequence
that ends at position 6 consists of 4 elements.

To calculate a value of $\texttt{length}(k)$,
we should find a position $i<k$
for which $\texttt{array}[i]<\texttt{array}[k]$
and $\texttt{length}(i)$ is as large as possible.
Then we know that
$\texttt{length}(k)=\texttt{length}(i)+1$,
because this is an optimal way to add
$\texttt{array}[k]$ to a subsequence.
However, if there is no such position $i$,
then $\texttt{length}(k)=1$,
which means that the subsequence only contains
$\texttt{array}[k]$.

Since all values of the function can be calculated
from its smaller values,
we can use dynamic programming.
In the following code, the values
of the function will be stored in an array
$\texttt{length}$.

```rust
# use std::cmp;
# let array = vec![6,2,5,1,7,4,8,3];
# let mut length = Vec::new();
for k in 0..array.len(){
    length.push(1);
    for i in 0..k{
        if (array[i] < array[k]) {
            length[k] = cmp::max(length[k], length[i]+1);
        }
    }
}
# println!("{length:?}")
```

This code works in $O(n^2)$ time,
because it consists of two nested loops.
However, it is also possible to implement
the dynamic programming calculation
more efficiently in $O(n \log n)$ time:

```rust
# use std::cmp;
# let array = vec![6,2,5,1,7,4,8,3];
# let mut length = Vec::new();
fn find_len(k: usize, array: &Vec<usize>, length: &mut Vec<usize>) -> usize{
    match length.get(k) {
        Some(&len) => len,
        _ => {
            length.push(1);
            for i in 0..k{
                if array[i] < array[k] {
                    let max_len = cmp::max(length[k], find_len(i, array, length)+1);
                    length[k] = max_len; 
                }
            }
            length[k]
        }
    }
}

let mut max_len = 0;
for i in 0..array.len(){
    max_len = cmp::max(max_len, find_len(i, &array, &mut length));
}
# println!("{length:?}")
```
