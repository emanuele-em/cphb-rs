# Segment trees revisited

A segment tree is a versatile data structure
that can be used to solve a large number of algorithm problems.
However, there are many topics related to segment trees
that we have not touched yet.
Now is time to discuss some more advanced variants
of segment trees.

So far, we have implemented the operations
of a segment tree by walking _from bottom to top_
in the tree.
For example, we have calculated
range sums as follows (Chapter 9.3):

```rust
# let n = 8usize;
# // the tree for the array [5,8,6,3,2,7,2,6] of Chapter 9.3
# let tree = vec![0i64,39,22,17,13,9,9,8,5,8,6,3,2,7,2,6];
fn sum(tree: &[i64], n: usize, mut a: usize, mut b: usize) -> i64 {
    a += n;
    b += n;
    let mut s = 0;
    while a <= b {
        if a % 2 == 1 { s += tree[a]; a += 1; }
        if b % 2 == 0 { s += tree[b]; b -= 1; }
        a /= 2;
        b /= 2;
    }
    s
}
# println!("{}", sum(&tree, n, 2, 6));
```

However, in more advanced segment trees,
it is often necessary to implement the operations
in another way, _from top to bottom_.
Using this approach, the function becomes as follows:
```rust
# let n = 8usize;
# // the tree for the array [5,8,6,3,2,7,2,6] of Chapter 9.3
# let tree = vec![0i64,39,22,17,13,9,9,8,5,8,6,3,2,7,2,6];
fn sum(tree: &[i64], a: usize, b: usize, k: usize, x: usize, y: usize) -> i64 {
    if b < x || a > y { return 0; }
    if a <= x && y <= b { return tree[k]; }
    let d = (x + y) / 2;
    sum(tree, a, b, 2*k, x, d) + sum(tree, a, b, 2*k+1, d+1, y)
}
# println!("{}", sum(&tree, 2, 6, 1, 0, n-1));
```

Now we can calculate any value of $\texttt{sum}_q(a,b)$
(the sum of array values in range $[a,b]$) as follows:
```rust, ignore
let s = sum(&tree, a, b, 1, 0, n-1);
```

The parameter $k$ indicates the current position
in `tree`.
Initially $k$ equals 1, because we begin
at the root of the tree.
The range $[x,y]$ corresponds to $k$
and is initially $[0,n-1]$.
When calculating the sum,
if $[x,y]$ is outside $[a,b]$,
the sum is 0,
and if $[x,y]$ is completely inside $[a,b]$,
the sum can be found in `tree`.
If $[x,y]$ is partially inside $[a,b]$,
the search continues recursively to the
left and right half of $[x,y]$.
The left half is $[x,d]$
and the right half is $[d+1,y]$
where $d=\lfloor \frac{x+y}{2} \rfloor$.

The following picture shows how the search proceeds
when calculating the value of $\texttt{sum}_q(a,b)$.
The gray nodes indicate nodes where the recursion
stops and the sum can be found in `tree`.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=gray!50] (5,0) rectangle (6,1);
\draw (0,0) grid (16,1);

\node[anchor=center] at (0.5, 0.5) {5};
\node[anchor=center] at (1.5, 0.5) {8};
\node[anchor=center] at (2.5, 0.5) {6};
\node[anchor=center] at (3.5, 0.5) {3};
\node[anchor=center] at (4.5, 0.5) {2};
\node[anchor=center] at (5.5, 0.5) {7};
\node[anchor=center] at (6.5, 0.5) {2};
\node[anchor=center] at (7.5, 0.5) {6};
\node[anchor=center] at (8.5, 0.5) {7};
\node[anchor=center] at (9.5, 0.5) {1};
\node[anchor=center] at (10.5, 0.5) {7};
\node[anchor=center] at (11.5, 0.5) {5};
\node[anchor=center] at (12.5, 0.5) {6};
\node[anchor=center] at (13.5, 0.5) {2};
\node[anchor=center] at (14.5, 0.5) {3};
\node[anchor=center] at (15.5, 0.5) {2};

%\node[anchor=center] at (1,2.5) {13};

\node[draw, circle] (a) at (1,2.5) {13};
\path[draw,thick,-] (a) -- (0.5,1);
\path[draw,thick,-] (a) -- (1.5,1);
\node[draw, circle,minimum size=22pt] (b) at (3,2.5) {9};
\path[draw,thick,-] (b) -- (2.5,1);
\path[draw,thick,-] (b) -- (3.5,1);
\node[draw, circle,minimum size=22pt] (c) at (5,2.5) {9};
\path[draw,thick,-] (c) -- (4.5,1);
\path[draw,thick,-] (c) -- (5.5,1);
\node[draw, circle,fill=gray!50,minimum size=22pt] (d) at (7,2.5) {8};
\path[draw,thick,-] (d) -- (6.5,1);
\path[draw,thick,-] (d) -- (7.5,1);
\node[draw, circle,minimum size=22pt] (e) at (9,2.5) {8};
\path[draw,thick,-] (e) -- (8.5,1);
\path[draw,thick,-] (e) -- (9.5,1);
\node[draw, circle] (f) at (11,2.5) {12};
\path[draw,thick,-] (f) -- (10.5,1);
\path[draw,thick,-] (f) -- (11.5,1);
\node[draw, circle,fill=gray!50,minimum size=22pt] (g) at (13,2.5) {8};
\path[draw,thick,-] (g) -- (12.5,1);
\path[draw,thick,-] (g) -- (13.5,1);
\node[draw, circle,minimum size=22pt] (h) at (15,2.5) {5};
\path[draw,thick,-] (h) -- (14.5,1);
\path[draw,thick,-] (h) -- (15.5,1);

\node[draw, circle] (i) at (2,4.5) {22};
\path[draw,thick,-] (i) -- (a);
\path[draw,thick,-] (i) -- (b);
\node[draw, circle] (j) at (6,4.5) {17};
\path[draw,thick,-] (j) -- (c);
\path[draw,thick,-] (j) -- (d);
\node[draw, circle,fill=gray!50] (k) at (10,4.5) {20};
\path[draw,thick,-] (k) -- (e);
\path[draw,thick,-] (k) -- (f);
\node[draw, circle] (l) at (14,4.5) {13};
\path[draw,thick,-] (l) -- (g);
\path[draw,thick,-] (l) -- (h);

\node[draw, circle] (m) at (4,6.5) {39};
\path[draw,thick,-] (m) -- (i);
\path[draw,thick,-] (m) -- (j);
\node[draw, circle] (n) at (12,6.5) {33};
\path[draw,thick,-] (n) -- (k);
\path[draw,thick,-] (n) -- (l);

\node[draw, circle] (o) at (8,8.5) {72};
\path[draw,thick,-] (o) -- (m);
\path[draw,thick,-] (o) -- (n);

\path[draw=red,thick,->,line width=2pt] (o) -- (m);
\path[draw=red,thick,->,line width=2pt] (o) -- (n);

\path[draw=red,thick,->,line width=2pt] (m) -- (j);
\path[draw=red,thick,->,line width=2pt] (j) -- (c);
\path[draw=red,thick,->,line width=2pt] (j) -- (d);
\path[draw=red,thick,->,line width=2pt] (c) -- (5.5,1);

\path[draw=red,thick,->,line width=2pt] (n) -- (k);
\path[draw=red,thick,->,line width=2pt] (n) -- (l);

\path[draw=red,thick,->,line width=2pt] (l) -- (g);

\draw [decoration={brace}, decorate, line width=0.5mm] (14,-0.25) -- (5,-0.25);

\node at (5.5,-0.75) {$a$};
\node at (13.5,-0.75) {$b$};
\end{tikzpicture}
</script>

Also in this implementation,
operations take $O(\log n)$ time,
because the total number of visited nodes is $O(\log n)$.
