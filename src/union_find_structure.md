# Union-find structure

A **union-find structure** maintains
a collection of sets.
The sets are disjoint, so no element
belongs to more than one set.
Two $O(\log n)$ time operations are supported:
the `unite` operation joins two sets,
and the `find` operation finds the representative
of the set that contains a given element.

## Structure

In a union-find structure, one element in each set
is the representative of the set,
and there is a chain from any other element of the
set to the representative.
For example, assume that the sets are
$\{1,4,7\}$, $\{5\}$ and $\{2,3,6,8\}$:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (0,-1) {1};
\node[draw, circle] (2) at (7,0) {2};
\node[draw, circle] (3) at (7,-1.5) {3};
\node[draw, circle] (4) at (1,0) {4};
\node[draw, circle] (5) at (4,0) {5};
\node[draw, circle] (6) at (6,-2.5) {6};
\node[draw, circle] (7) at (2,-1) {7};
\node[draw, circle] (8) at (8,-2.5) {8};

\path[draw,thick,->] (1) -- (4);
\path[draw,thick,->] (7) -- (4);

\path[draw,thick,->] (3) -- (2);
\path[draw,thick,->] (6) -- (3);
\path[draw,thick,->] (8) -- (3);

\end{tikzpicture}
</script>

In this case the representatives
of the sets are 4, 5 and 2.
We can find the representative of any element
by following the chain that begins at the element.
For example, the element 2 is the representative
for the element 6, because
we follow the chain $6 \rightarrow 3 \rightarrow 2$.
Two elements belong to the same set exactly when
their representatives are the same.

Two sets can be joined by connecting the
representative of one set to the
representative of the other set.
For example, the sets
{1,4,7} and {2,3,6,8}
can be joined as follows:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (2,-1) {1};
\node[draw, circle] (2) at (7,0) {2};
\node[draw, circle] (3) at (7,-1.5) {3};
\node[draw, circle] (4) at (3,0) {4};
\node[draw, circle] (6) at (6,-2.5) {6};
\node[draw, circle] (7) at (4,-1) {7};
\node[draw, circle] (8) at (8,-2.5) {8};

\path[draw,thick,->] (1) -- (4);
\path[draw,thick,->] (7) -- (4);

\path[draw,thick,->] (3) -- (2);
\path[draw,thick,->] (6) -- (3);
\path[draw,thick,->] (8) -- (3);

\path[draw,thick,->] (4) -- (2);
\end{tikzpicture}
</script>

The resulting set contains the elements
{1,2,3,4,6,7,8}.
From this on, the element 2 is the representative
for the entire set and the old representative 4
points to the element 2.

The efficiency of the union-find structure depends on
how the sets are joined.
It turns out that we can follow a simple strategy:
always connect the representative of the
\emph{smaller} set to the representative of the \emph{larger} set
(or if the sets are of equal size,
we can make an arbitrary choice).
Using this strategy, the length of any chain
will be $O(\log n)$, so we can
find the representative of any element
efficiently by following the corresponding chain.

## Implementation

The union-find structure can be implemented
using arrays.
In the following implementation,
the array `link` contains for each element
the next element
in the chain or the element itself if it is
a representative,
and the array `size` indicates for each representative
the size of the corresponding set.

Initially, each element belongs to a separate set:

```rust, ignore
for i in 1..=n {link[i] = i};
for i in 1..=n {size[i] = i};
```

The function `find` returns
the representative for an element $x$.
The representative can be found by following
the chain that begins at $x$.

```rust
fn find(mut x:usize, link: &[usize]) -> usize {
    while x != link[x] {x = link[x]}
    x
}
```

The function `same` checks
whether elements $a$ and $b$ belong to the same set.
This can easily be done by using the
function `find`:
```rust
# fn find(mut x:usize, link: &[usize]) -> usize {
#     while x != link[x] {x = link[x]}
#     x
# }
fn same(a: usize, b: usize, link: &[usize]) -> bool {
    find(a, link) == find(b, link)
}
```

The function `unite` joins the sets
that contain elements $a$ and $b$
(the elements have to be in different sets).
The function first finds the representatives
of the sets and then connects the smaller
set to the larger set.

```rust
# fn find(mut x:usize, link: &[usize]) -> usize {
#     while x != link[x] {x = link[x]}
#     x
# }
# fn swap(a: usize, b: usize){
# todo!();
# }
fn unite(mut a: usize, mut b: usize, link: &mut [usize], size: &mut [usize]) {
    a = find(a, link);
    b = find(b, link);
    if size[a] < size[b] {swap(a,b)}
    size[a] += size[b];
    link[b] = a;
}
```

The time complexity of the function `find`
is $O(\log n)$ assuming that the length of each
chain is $O(\log n)$.
In this case, the functions `same` and `unite`
also work in $O(\log n)$ time.
The function `unite` makes sure that the
length of each chain is $O(\log n)$ by connecting
the smaller set to the larger set.

___

[^1] The structure presented here was introduced in 1971 by J. D. Hopcroft and J. D. Ullman [38].
Later, in 1975, R. E. Tarjan studied a more sophisticated variant of the structure [64] that is discussed in many algorithm textbooks nowadays.
