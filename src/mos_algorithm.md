# Mo's algorithm

**Mo's algorithm**[^1]
can be used in many problems
that require processing range queries in 
a _static_ array, i.e., the array values
do not change between the queries.
In each query, we are given a range $[a,b]$,
and we should calculate a value based on the
array elements between positions $a$ and $b$.
Since the array is static,
the queries can be processed in any order,
and Mo's algorithm
processes the queries in a special order which guarantees
that the algorithm works efficiently.

Mo's algorithm maintains an _active range_
of the array, and the answer to a query
concerning the active range is known at each moment.
The algorithm processes the queries one by one,
and always moves the endpoints of the
active range by inserting and removing elements.
The time complexity of the algorithm is
$O(n \sqrt n f(n))$ where the array contains
$n$ elements, there are $n$ queries
and each insertion and removal of an element
takes $O(f(n))$ time.

The trick in Mo's algorithm is the order
in which the queries are processed:
The array is divided into blocks of $k=O(\sqrt n)$
elements, and a query $[a_1,b_1]$
is processed before a query $[a_2,b_2]$
if either 
- $\lfloor a_1/k \rfloor < \lfloor a_2/k \rfloor$ or
- $\lfloor a_1/k \rfloor = \lfloor a_2/k \rfloor$ and $b_1 < b_2$.

Thus, all queries whose left endpoints are
in a certain block are processed one after another
sorted according to their right endpoints.
Using this order, the algorithm
only performs $O(n \sqrt n)$ operations,
because the left endpoint moves
$O(n)$ times $O(\sqrt n)$ steps,
and the right endpoint moves
$O(\sqrt n)$ times $O(n)$ steps. Thus, both
endpoints move a total of $O(n \sqrt n)$ steps during the algorithm.

Counting distinct elements in each range, the whole algorithm is:

```rust
fn mo(a: &[usize], queries: &[(usize, usize)]) -> Vec<usize> {
    let k = (a.len() as f64).sqrt() as usize + 1;
    let mut order: Vec<usize> = (0..queries.len()).collect();
    order.sort_by_key(|&i| (queries[i].0 / k, queries[i].1));

    let mut count = vec![0usize; a.iter().max().map_or(0, |m| m + 1)];
    let mut distinct = 0usize;
    let mut answers = vec![0usize; queries.len()];
    let (mut lo, mut hi) = (0usize, 0usize); // active range is lo..hi
    for qi in order {
        let (a1, b1) = (queries[qi].0, queries[qi].1 + 1);
        while hi < b1 { if count[a[hi]] == 0 { distinct += 1 } count[a[hi]] += 1; hi += 1; }
        while lo > a1 { lo -= 1; if count[a[lo]] == 0 { distinct += 1 } count[a[lo]] += 1; }
        while hi > b1 { hi -= 1; count[a[hi]] -= 1; if count[a[hi]] == 0 { distinct -= 1 } }
        while lo < a1 { count[a[lo]] -= 1; if count[a[lo]] == 0 { distinct -= 1 } lo += 1; }
        answers[qi] = distinct;
    }
    answers
}
# // the array used in the example above
# let a = [4,2,5,4,2,4,3,3,4];
# let qs = [(2,5),(3,7),(0,8)];
# for (q, n) in qs.iter().zip(mo(&a, &qs)) {
#     println!("range {:?} -> {} distinct", q, n);
# }
```

The natural C++ shape here is a pair of `add` and `remove` lambdas sharing
`count` and `distinct`. That does not translate: two closures cannot both
hold a mutable borrow of the same state. Writing the four updates inline
in the loop avoids the problem entirely, and is shorter than reaching for
`RefCell` to recover the lambda structure.

## Example

As an example, consider a problem
where we are given a set of queries,
each of them corresponding to a range in an array,
and our task is to calculate for each query
the number of _distinct_ elements in the range.

In Mo's algorithm, the queries are always sorted
in the same way, but it depends on the problem
how the answer to the query is maintained.
In this problem, we can maintain an array 
`count` where $\texttt{count}[x]$
indicates the number of times an element $x$
occurs in the active range.

When we move from one query to another query,
the active range changes.
For example, if the current range is

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (1,0) rectangle (5,1);
\draw (0,0) grid (9,1);
\node at (0.5, 0.5) {4};
\node at (1.5, 0.5) {2};
\node at (2.5, 0.5) {5};
\node at (3.5, 0.5) {4};
\node at (4.5, 0.5) {2};
\node at (5.5, 0.5) {4};
\node at (6.5, 0.5) {3};
\node at (7.5, 0.5) {3};
\node at (8.5, 0.5) {4};
\end{tikzpicture}
</script>

and the next range is

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (2,0) rectangle (7,1);
\draw (0,0) grid (9,1);
\node at (0.5, 0.5) {4};
\node at (1.5, 0.5) {2};
\node at (2.5, 0.5) {5};
\node at (3.5, 0.5) {4};
\node at (4.5, 0.5) {2};
\node at (5.5, 0.5) {4};
\node at (6.5, 0.5) {3};
\node at (7.5, 0.5) {3};
\node at (8.5, 0.5) {4};
\end{tikzpicture}
</script>

there will be three steps:
the left endpoint moves one step to the right,
and the right endpoint moves two steps to the right.

After each step, the array `count`
needs to be updated.
After adding an element $x$,
we increase the value of 
$\texttt{count}[x]$ by 1,
and if $\texttt{count}[x]=1$ after this,
we also increase the answer to the query by 1.
Similarly, after removing an element $x$,
we decrease the value of 
$\texttt{count}[x]$ by 1,
and if $\texttt{count}[x]=0$ after this,
we also decrease the answer to the query by 1.

In this problem, the time needed to perform
each step is $O(1)$, so the total time complexity
of the algorithm is $O(n \sqrt n)$.

___

[^1]: According to [13], this algorithm
is named after Mo Tao, a Chinese competitive programmer, but
the technique has appeared earlier in the literature [48].
