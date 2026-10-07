# Lazy propagation

Using **lazy propagation**, we can build
a segment tree that supports _both_ range updates
and range queries in $O(\log n)$ time.
The idea is to perform updates and queries
from top to bottom and perform updates
_lazily_ so that they are propagated
down the tree only when it is necessary.

In a lazy segment tree, nodes contain two types of
information.
Like in an ordinary segment tree,
each node contains the sum or some other value
related to the corresponding subarray.
In addition, the node may contain information
related to lazy updates, which has not been
propagated to its children.

There are two types of range updates:
each array value in the range is either
_increased_ by some value
or _assigned_ some value.
Both operations can be implemented using
similar ideas, and it is even possible to construct
a tree that supports both operations at the same time.

## Lazy segment trees

Let us consider an example where our goal is to
construct a segment tree that supports
two operations: increasing each value in
$[a,b]$ by a constant and calculating the sum of
values in $[a,b]$.

We will construct a tree where each node
has two values $s/z$:
$s$ denotes the sum of values in the range,
and $z$ denotes the value of a lazy update,
which means that all values in the range
should be increased by $z$.
In the following tree, $z=0$ in all nodes,
so there are no ongoing lazy updates.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
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

\node[draw, circle] (a) at (1,2.5) {13/0};
\path[draw,thick,-] (a) -- (0.5,1);
\path[draw,thick,-] (a) -- (1.5,1);
\node[draw, circle,minimum size=32pt] (b) at (3,2.5) {9/0};
\path[draw,thick,-] (b) -- (2.5,1);
\path[draw,thick,-] (b) -- (3.5,1);
\node[draw, circle,minimum size=32pt] (c) at (5,2.5) {9/0};
\path[draw,thick,-] (c) -- (4.5,1);
\path[draw,thick,-] (c) -- (5.5,1);
\node[draw, circle,minimum size=32pt] (d) at (7,2.5) {8/0};
\path[draw,thick,-] (d) -- (6.5,1);
\path[draw,thick,-] (d) -- (7.5,1);
\node[draw, circle,minimum size=32pt] (e) at (9,2.5) {8/0};
\path[draw,thick,-] (e) -- (8.5,1);
\path[draw,thick,-] (e) -- (9.5,1);
\node[draw, circle] (f) at (11,2.5) {12/0};
\path[draw,thick,-] (f) -- (10.5,1);
\path[draw,thick,-] (f) -- (11.5,1);
\node[draw, circle,minimum size=32pt] (g) at (13,2.5) {8/0};
\path[draw,thick,-] (g) -- (12.5,1);
\path[draw,thick,-] (g) -- (13.5,1);
\node[draw, circle,minimum size=32pt] (h) at (15,2.5) {5/0};
\path[draw,thick,-] (h) -- (14.5,1);
\path[draw,thick,-] (h) -- (15.5,1);

\node[draw, circle] (i) at (2,4.5) {22/0};
\path[draw,thick,-] (i) -- (a);
\path[draw,thick,-] (i) -- (b);
\node[draw, circle] (j) at (6,4.5) {17/0};
\path[draw,thick,-] (j) -- (c);
\path[draw,thick,-] (j) -- (d);
\node[draw, circle] (k) at (10,4.5) {20/0};
\path[draw,thick,-] (k) -- (e);
\path[draw,thick,-] (k) -- (f);
\node[draw, circle] (l) at (14,4.5) {13/0};
\path[draw,thick,-] (l) -- (g);
\path[draw,thick,-] (l) -- (h);

\node[draw, circle] (m) at (4,6.5) {39/0};
\path[draw,thick,-] (m) -- (i);
\path[draw,thick,-] (m) -- (j);
\node[draw, circle] (n) at (12,6.5) {33/0};
\path[draw,thick,-] (n) -- (k);
\path[draw,thick,-] (n) -- (l);

\node[draw, circle] (o) at (8,8.5) {72/0};
\path[draw,thick,-] (o) -- (m);
\path[draw,thick,-] (o) -- (n);
\end{tikzpicture}
</script>

When the elements in $[a,b]$ are increased by $u$,
we walk from the root towards the leaves
and modify the nodes of the tree as follows:
If the range $[x,y]$ of a node is
completely inside $[a,b]$,
we increase the $z$ value of the node by $u$ and stop.
If $[x,y]$ only partially belongs to $[a,b]$,
we increase the $s$ value of the node by $hu$,
where $h$ is the size of the intersection of $[a,b]$
and $[x,y]$, and continue our walk recursively in the tree.

For example, the following picture shows the tree after
increasing the elements in $[a,b]$ by 2:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=gray!50] (5,0) rectangle (6,1);
\draw (0,0) grid (16,1);

\node[anchor=center] at (0.5, 0.5) {5};
\node[anchor=center] at (1.5, 0.5) {8};
\node[anchor=center] at (2.5, 0.5) {6};
\node[anchor=center] at (3.5, 0.5) {3};
\node[anchor=center] at (4.5, 0.5) {2};
\node[anchor=center] at (5.5, 0.5) {9};
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

\node[draw, circle] (a) at (1,2.5) {13/0};
\path[draw,thick,-] (a) -- (0.5,1);
\path[draw,thick,-] (a) -- (1.5,1);
\node[draw, circle,minimum size=32pt] (b) at (3,2.5) {9/0};
\path[draw,thick,-] (b) -- (2.5,1);
\path[draw,thick,-] (b) -- (3.5,1);
\node[draw, circle,minimum size=32pt] (c) at (5,2.5) {11/0};
\path[draw,thick,-] (c) -- (4.5,1);
\path[draw,thick,-] (c) -- (5.5,1);
\node[draw, circle,fill=gray!50,minimum size=32pt] (d) at (7,2.5) {8/2};
\path[draw,thick,-] (d) -- (6.5,1);
\path[draw,thick,-] (d) -- (7.5,1);
\node[draw, circle,minimum size=32pt] (e) at (9,2.5) {8/0};
\path[draw,thick,-] (e) -- (8.5,1);
\path[draw,thick,-] (e) -- (9.5,1);
\node[draw, circle] (f) at (11,2.5) {12/0};
\path[draw,thick,-] (f) -- (10.5,1);
\path[draw,thick,-] (f) -- (11.5,1);
\node[draw, circle,fill=gray!50,minimum size=32pt] (g) at (13,2.5) {8/2};
\path[draw,thick,-] (g) -- (12.5,1);
\path[draw,thick,-] (g) -- (13.5,1);
\node[draw, circle,minimum size=32pt] (h) at (15,2.5) {5/0};
\path[draw,thick,-] (h) -- (14.5,1);
\path[draw,thick,-] (h) -- (15.5,1);

\node[draw, circle] (i) at (2,4.5) {22/0};
\path[draw,thick,-] (i) -- (a);
\path[draw,thick,-] (i) -- (b);
\node[draw, circle] (j) at (6,4.5) {23/0};
\path[draw,thick,-] (j) -- (c);
\path[draw,thick,-] (j) -- (d);
\node[draw, circle,fill=gray!50] (k) at (10,4.5) {20/2};
\path[draw,thick,-] (k) -- (e);
\path[draw,thick,-] (k) -- (f);
\node[draw, circle] (l) at (14,4.5) {17/0};
\path[draw,thick,-] (l) -- (g);
\path[draw,thick,-] (l) -- (h);

\node[draw, circle] (m) at (4,6.5) {45/0};
\path[draw,thick,-] (m) -- (i);
\path[draw,thick,-] (m) -- (j);
\node[draw, circle] (n) at (12,6.5) {45/0};
\path[draw,thick,-] (n) -- (k);
\path[draw,thick,-] (n) -- (l);

\node[draw, circle] (o) at (8,8.5) {90/0};
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

We also calculate the sum of elements in a range $[a,b]$
by walking in the tree from top to bottom.
If the range $[x,y]$ of a node completely belongs
to $[a,b]$, we add the $s$ value of the node to the sum.
Otherwise, we continue the search recursively
downwards in the tree.

Both in updates and queries,
the value of a lazy update is always propagated
to the children of the node
before processing the node.
The idea is that updates will be propagated
downwards only when it is necessary,
which guarantees that the operations are always efficient.

The following picture shows how the tree changes
when we calculate the value of $\texttt{sum}_a(a,b)$.
The rectangle shows the nodes whose values change,
because a lazy update is propagated downwards.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (16,1);

\node[anchor=center] at (0.5, 0.5) {5};
\node[anchor=center] at (1.5, 0.5) {8};
\node[anchor=center] at (2.5, 0.5) {6};
\node[anchor=center] at (3.5, 0.5) {3};
\node[anchor=center] at (4.5, 0.5) {2};
\node[anchor=center] at (5.5, 0.5) {9};
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

\node[draw, circle] (a) at (1,2.5) {13/0};
\path[draw,thick,-] (a) -- (0.5,1);
\path[draw,thick,-] (a) -- (1.5,1);
\node[draw, circle,minimum size=32pt] (b) at (3,2.5) {9/0};
\path[draw,thick,-] (b) -- (2.5,1);
\path[draw,thick,-] (b) -- (3.5,1);
\node[draw, circle,minimum size=32pt] (c) at (5,2.5) {11/0};
\path[draw,thick,-] (c) -- (4.5,1);
\path[draw,thick,-] (c) -- (5.5,1);
\node[draw, circle,minimum size=32pt] (d) at (7,2.5) {8/2};
\path[draw,thick,-] (d) -- (6.5,1);
\path[draw,thick,-] (d) -- (7.5,1);
\node[draw, circle,minimum size=32pt] (e) at (9,2.5) {8/2};
\path[draw,thick,-] (e) -- (8.5,1);
\path[draw,thick,-] (e) -- (9.5,1);
\node[draw, circle,fill=gray!50,] (f) at (11,2.5) {12/2};
\path[draw,thick,-] (f) -- (10.5,1);
\path[draw,thick,-] (f) -- (11.5,1);
\node[draw, circle,fill=gray!50,minimum size=32pt] (g) at (13,2.5) {8/2};
\path[draw,thick,-] (g) -- (12.5,1);
\path[draw,thick,-] (g) -- (13.5,1);
\node[draw, circle,minimum size=32pt] (h) at (15,2.5) {5/0};
\path[draw,thick,-] (h) -- (14.5,1);
\path[draw,thick,-] (h) -- (15.5,1);

\node[draw, circle] (i) at (2,4.5) {22/0};
\path[draw,thick,-] (i) -- (a);
\path[draw,thick,-] (i) -- (b);
\node[draw, circle] (j) at (6,4.5) {23/0};
\path[draw,thick,-] (j) -- (c);
\path[draw,thick,-] (j) -- (d);
\node[draw, circle] (k) at (10,4.5) {28/0};
\path[draw,thick,-] (k) -- (e);
\path[draw,thick,-] (k) -- (f);
\node[draw, circle] (l) at (14,4.5) {17/0};
\path[draw,thick,-] (l) -- (g);
\path[draw,thick,-] (l) -- (h);

\node[draw, circle] (m) at (4,6.5) {45/0};
\path[draw,thick,-] (m) -- (i);
\path[draw,thick,-] (m) -- (j);
\node[draw, circle] (n) at (12,6.5) {45/0};
\path[draw,thick,-] (n) -- (k);
\path[draw,thick,-] (n) -- (l);

\node[draw, circle] (o) at (8,8.5) {90/0};
\path[draw,thick,-] (o) -- (m);
\path[draw,thick,-] (o) -- (n);

\path[draw=red,thick,->,line width=2pt] (o) -- (n);

\path[draw=red,thick,->,line width=2pt] (n) -- (k);
\path[draw=red,thick,->,line width=2pt] (n) -- (l);

\path[draw=red,thick,->,line width=2pt] (k) -- (f);
\path[draw=red,thick,->,line width=2pt] (l) -- (g);

\draw [decoration={brace}, decorate, line width=0.5mm] (14,-0.25) -- (10,-0.25);

\draw[color=blue,thick] (8,1.5) rectangle (12,5.5);

\node at (10.5,-0.75) {$a$};
\node at (13.5,-0.75) {$b$};
\end{tikzpicture}
</script>

Note that sometimes it is needed to combine lazy updates.
This happens when a node that already has a lazy update
is assigned another lazy update.
When calculating sums, it is easy to combine lazy updates,
because the combination of updates $z_1$ and $z_2$
corresponds to an update $z_1+z_2$.

Here is the whole structure, with a range increment and a range sum:

```rust
struct Lazy { sum: Vec<i64>, add: Vec<i64>, n: usize }

impl Lazy {
    fn new(n: usize) -> Lazy {
        Lazy { sum: vec![0; 4 * n], add: vec![0; 4 * n], n }
    }

    // push this node's pending update down to its two children
    fn push(&mut self, k: usize, x: usize, y: usize) {
        if self.add[k] == 0 || x == y { return; }
        let d = (x + y) / 2;
        for (c, len) in [(2*k, d - x + 1), (2*k + 1, y - d)] {
            self.add[c] += self.add[k];
            self.sum[c] += self.add[k] * len as i64;
        }
        self.add[k] = 0;
    }

    fn update(&mut self, a: usize, b: usize, z: i64,
              k: usize, x: usize, y: usize) {
        if b < x || a > y { return; }
        if a <= x && y <= b {
            self.add[k] += z;
            self.sum[k] += z * (y - x + 1) as i64;
            return;
        }
        self.push(k, x, y);
        let d = (x + y) / 2;              // compute before recursing
        self.update(a, b, z, 2*k, x, d);
        self.update(a, b, z, 2*k + 1, d + 1, y);
        self.sum[k] = self.sum[2*k] + self.sum[2*k + 1];
    }

    fn query(&mut self, a: usize, b: usize,
             k: usize, x: usize, y: usize) -> i64 {
        if b < x || a > y { return 0; }
        if a <= x && y <= b { return self.sum[k]; }
        self.push(k, x, y);
        let d = (x + y) / 2;
        self.query(a, b, 2*k, x, d) + self.query(a, b, 2*k + 1, d + 1, y)
    }
}
# let n = 8;
# let mut t = Lazy::new(n);
# t.update(1, 5, 3, 1, 0, n-1);
# t.update(3, 7, 2, 1, 0, n-1);
# println!("sum(0..=7) = {}", t.query(0, n-1, 1, 0, n-1));
# println!("sum(2..=4) = {}", t.query(2, 4, 1, 0, n-1));
```

Recursive `&mut self` methods are perfectly legal in Rust, but only if no
borrow is held across the recursive call. That is why `d` is computed
before recursing and why the two children are visited one after the
other. Taking a reference into the tree first, as in
`let node = &mut self.sum[k];`, would hold the borrow for the whole
recursion and be rejected. Splitting `sum` and `add` into two parallel
vectors rather than a `Vec<Node>` keeps each borrow narrow for the same
reason.

## Polynomial updates

Lazy updates can be generalized so that it is
possible to update ranges using polynomials of the form
\\[
p(u) = t_k u^k + t_{k-1} u^{k-1} + \\cdots + t_0.
\\]

In this case, the update for a value
at position $i$ in $[a,b]$ is $p(i-a)$.
For example, adding the polynomial $p(u)=u+1$
to $[a,b]$ means that the value at position $a$
increases by 1, the value at position $a+1$
increases by 2, and so on.

To support polynomial updates,
each node is assigned $k+2$ values,
where $k$ equals the degree of the polynomial.
The value $s$ is the sum of the elements in the range,
and the values $z_0,z_1,\ldots,z_k$ are the coefficients
of a polynomial that corresponds to a lazy update.

Now, the sum of values in a range $[x,y]$ equals
\\[
s+\\sum_{u=0}^{y-x} z_k u^k + z_{k-1} u^{k-1} + \\cdots + z_0.
\\]

The value of such a sum
can be efficiently calculated using sum formulas.
For example, the term $z_0$ corresponds to the sum
$(y-x+1)z_0$, and the term $z_1 u$ corresponds to the sum
\\[
z_1(0+1+\\cdots+y-x) = z_1 \\frac{(y-x)(y-x+1)}{2} .
\\]

When propagating an update in the tree,
the indices of $p(u)$ change,
because in each range $[x,y]$,
the values are
calculated for $u=0,1,\ldots,y-x$.
However, this is not a problem, because
$p'(u)=p(u+h)$ is a polynomial
of equal degree as $p(u)$.
For example, if $p(u)=t_2 u^2+t_1 u-t_0$, then
\\[
p'(u)=t_2(u+h)^2+t_1(u+h)-t_0=t_2 u^2 + (2ht_2+t_1)u+t_2h^2+t_1h-t_0.
\\]
