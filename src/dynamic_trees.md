# Dynamic trees

An ordinary segment tree is static,
which means that each node has a fixed position
in the array and the tree requires
a fixed amount of memory.
In a **dynamic segment tree**,
memory is allocated only for nodes that
are actually accessed during the algorithm,
which can save a large amount of memory.

The C++ version links nodes with raw pointers. In Rust the nodes go into
an **arena** -- a single `Vec` that owns them all -- and children are
referred to by index, with 0 standing for "no child":

```rust
#[derive(Clone, Copy, Debug)]
struct Node {
    value: i64,
    x: usize,
    y: usize,        // the range [x, y] this node covers
    left: usize,     // 0 means no child
    right: usize,
}

struct Tree { nodes: Vec<Node> }

impl Tree {
    fn new(x: usize, y: usize) -> Tree {
        // index 0 is the reserved null slot, index 1 is the root
        let null = Node { value: 0, x: 0, y: 0, left: 0, right: 0 };
        Tree { nodes: vec![null, Node { value: 0, x, y, left: 0, right: 0 }] }
    }

    fn add(&mut self, x: usize, y: usize) -> usize {
        self.nodes.push(Node { value: 0, x, y, left: 0, right: 0 });
        self.nodes.len() - 1
    }
}
# let mut t = Tree::new(0, 15);
# t.nodes[1].value = 5;
# let child = t.add(0, 7);
# println!("root {:?}", t.nodes[1]);
# println!("new child at index {child}");
```

This is worth dwelling on, because it is not merely a way to avoid raw
pointers. `Box<Node>` would express a dynamic tree perfectly well, but it
**cannot express the persistent tree** described later in this section:
persistence works by having several versions share the same unchanged
subtrees, and `Box` is unique ownership. `Rc<Node>` could share, but then
dropping a deep tree recurses and can overflow the stack. Indices into a
`Vec` share freely, cost nothing to copy, and match the way the book
already numbers its nodes.

## Sparse segment trees

A dynamic segment tree is useful when
the underlying array is _sparse_,
i.e., the range $[0,n-1]$
of allowed indices is large,
but most array values are zeros.
While an ordinary segment tree uses $O(n)$ memory,
a dynamic segment tree only uses $O(k \log n)$ memory,
where $k$ is the number of operations performed.

A **sparse segment tree** initially has
only one node $[0,n-1]$ whose value is zero,
which means that every array value is zero.
After updates, new nodes are dynamically added
to the tree.
For example, if $n=16$ and the elements
in positions 3 and 10 have been modified,
the tree contains the following nodes:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\scriptsize
\node[draw, circle,minimum size=35pt] (1) at (0,0) {$[0,15]$};
\node[draw, circle,minimum size=35pt] (2) at (-4,-2) {$[0,7]$};
\node[draw, circle,minimum size=35pt] (3) at (-6,-4) {$[0,3]$};
\node[draw, circle,minimum size=35pt] (4) at (-4,-6) {$[2,3]$};
\node[draw, circle,minimum size=35pt] (5) at (-2,-8) {$[3]$};
\node[draw, circle,minimum size=35pt] (6) at (4,-2) {$[8,15]$};
\node[draw, circle,minimum size=35pt] (7) at (2,-4) {$[8,11]$};
\node[draw, circle,minimum size=35pt] (8) at (4,-6) {$[10,11]$};
\node[draw, circle,minimum size=35pt] (9) at (2,-8) {$[10]$};

\path[draw,thick,->] (1) -- (2);
\path[draw,thick,->] (2) -- (3);
\path[draw,thick,->] (3) -- (4);
\path[draw,thick,->] (4) -- (5);

\path[draw,thick,->] (1) -- (6);
\path[draw,thick,->] (6) -- (7);
\path[draw,thick,->] (7) -- (8);
\path[draw,thick,->] (8) -- (9);
\end{tikzpicture}
</script>

Any path from the root node to a leaf contains
$O(\log n)$ nodes,
so each operation adds at most $O(\log n)$
new nodes to the tree.
Thus, after $k$ operations, the tree contains
at most $O(k \log n)$ nodes.

Note that if we know all elements to be updated
at the beginning of the algorithm,
a dynamic segment tree is not necessary,
because we can use an ordinary segment tree with
index compression (Chapter 9.4).
However, this is not possible when the indices
are generated during the algorithm.

## Persistent segment trees

Using a dynamic implementation,
it is also possible to create a
**persistent segment tree** that stores
the _modification history_ of the tree.
In such an implementation, we can
efficiently access
all versions of the tree that have
existed during the algorithm.

When the modification history is available,
we can perform queries in any previous tree
like in an ordinary segment tree, because the
full structure of each tree is stored.
We can also create new trees based on previous
trees and modify them independently.

Consider the following sequence of updates,
where red nodes change
and other nodes remain the same:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.8]
\node[draw, circle,minimum size=13pt] (1a) at (3,0) {};
\node[draw, circle,minimum size=13pt] (2a) at (2,-1) {};
\node[draw, circle,minimum size=13pt] (3a) at (4,-1) {};
\node[draw, circle,minimum size=13pt] (4a) at (1.5,-2) {};
\node[draw, circle,minimum size=13pt] (5a) at (2.5,-2) {};
\node[draw, circle,minimum size=13pt] (6a) at (3.5,-2) {};
\node[draw, circle,minimum size=13pt] (7a) at (4.5,-2) {};
\path[draw,thick,->] (1a) -- (2a);
\path[draw,thick,->] (1a) -- (3a);
\path[draw,thick,->] (2a) -- (4a);
\path[draw,thick,->] (2a) -- (5a);
\path[draw,thick,->] (3a) -- (6a);
\path[draw,thick,->] (3a) -- (7a);

\node[draw, circle,minimum size=13pt,fill=red] (1b) at (3+5,0) {};
\node[draw, circle,minimum size=13pt,fill=red] (2b) at (2+5,-1) {};
\node[draw, circle,minimum size=13pt] (3b) at (4+5,-1) {};
\node[draw, circle,minimum size=13pt] (4b) at (1.5+5,-2) {};
\node[draw, circle,minimum size=13pt,fill=red] (5b) at (2.5+5,-2) {};
\node[draw, circle,minimum size=13pt] (6b) at (3.5+5,-2) {};
\node[draw, circle,minimum size=13pt] (7b) at (4.5+5,-2) {};
\path[draw,thick,->] (1b) -- (2b);
\path[draw,thick,->] (1b) -- (3b);
\path[draw,thick,->] (2b) -- (4b);
\path[draw,thick,->] (2b) -- (5b);
\path[draw,thick,->] (3b) -- (6b);
\path[draw,thick,->] (3b) -- (7b);

\node[draw, circle,minimum size=13pt,fill=red] (1c) at (3+10,0) {};
\node[draw, circle,minimum size=13pt] (2c) at (2+10,-1) {};
\node[draw, circle,minimum size=13pt,fill=red] (3c) at (4+10,-1) {};
\node[draw, circle,minimum size=13pt] (4c) at (1.5+10,-2) {};
\node[draw, circle,minimum size=13pt] (5c) at (2.5+10,-2) {};
\node[draw, circle,minimum size=13pt] (6c) at (3.5+10,-2) {};
\node[draw, circle,minimum size=13pt,fill=red] (7c) at (4.5+10,-2) {};
\path[draw,thick,->] (1c) -- (2c);
\path[draw,thick,->] (1c) -- (3c);
\path[draw,thick,->] (2c) -- (4c);
\path[draw,thick,->] (2c) -- (5c);
\path[draw,thick,->] (3c) -- (6c);
\path[draw,thick,->] (3c) -- (7c);

\node at (3,-3) {step 1};
\node at (3+5,-3) {step 2};
\node at (3+10,-3) {step 3};
\end{tikzpicture}
</script>

After each update, most nodes of the tree
remain the same,
so an efficient way to store the modification history
is to represent each tree in the history as a combination
of new nodes and subtrees of previous trees.
In this example, the modification history can be
stored as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.8]
\path[use as bounding box] (0, 1) rectangle (16, -3.5);

\node[draw, circle,minimum size=13pt] (1a) at (3,0) {};
\node[draw, circle,minimum size=13pt] (2a) at (2,-1) {};
\node[draw, circle,minimum size=13pt] (3a) at (4,-1) {};
\node[draw, circle,minimum size=13pt] (4a) at (1.5,-2) {};
\node[draw, circle,minimum size=13pt] (5a) at (2.5,-2) {};
\node[draw, circle,minimum size=13pt] (6a) at (3.5,-2) {};
\node[draw, circle,minimum size=13pt] (7a) at (4.5,-2) {};
\path[draw,thick,->] (1a) -- (2a);
\path[draw,thick,->] (1a) -- (3a);
\path[draw,thick,->] (2a) -- (4a);
\path[draw,thick,->] (2a) -- (5a);
\path[draw,thick,->] (3a) -- (6a);
\path[draw,thick,->] (3a) -- (7a);

\node[draw, circle,minimum size=13pt,fill=red] (1b) at (3+5,0) {};
\node[draw, circle,minimum size=13pt,fill=red] (2b) at (2+5,-1) {};
\node[draw, circle,minimum size=13pt,fill=red] (5b) at (2.5+5,-2) {};
\path[draw,thick,->] (1b) -- (2b);

\draw[thick,->] (1b) .. controls (3+5+2,0-1) and (3+5,2.5) .. (3a);

\draw[thick,->] (2b) .. controls (2+5-0.5,-1-0.5) and (2,4.5) .. (4a);


\path[draw,thick,->] (2b) -- (5b);

\node[draw, circle,minimum size=13pt,fill=red] (1c) at (3+10,0) {};
\node[draw, circle,minimum size=13pt,fill=red] (3c) at (4+10,-1) {};
\node[draw, circle,minimum size=13pt,fill=red] (7c) at (4.5+10,-2) {};
\path[draw,thick,->] (1c) -- (2b);
\path[draw,thick,->] (1c) -- (3c);

\draw[thick,->] (3c) .. controls (2.5+5,-3) and (3.5,-3) .. (6a);

\path[draw,thick,->] (3c) -- (7c);

\node at (3,-3) {step 1};
\node at (3+5,-3) {step 2};
\node at (3+10,-3) {step 3};
\end{tikzpicture}
</script>

The structure of each previous tree can be
reconstructed by following the pointers
starting at the corresponding root node.
Since each operation
adds only $O(\log n)$ new nodes to the tree,
it is possible to store the full modification history of the tree.
