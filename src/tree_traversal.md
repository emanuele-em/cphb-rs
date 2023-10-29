# Tree traversal

General graph traversal algorithms
can be used to traverse the nodes of a tree.
However, the traversal of a tree is easier to implement than
that of a general graph, because
there are no cycles in the tree and it is not
possible to reach a node from multiple directions.

The typical way to traverse a tree is to start
a depth-first search at an arbitrary node.
The following recursive function can be used:

```rust
# let adj = [vec![], vec![2, 3, 4], vec![5, 6], vec![], vec![7], vec![], vec![8], vec![], vec![]];
# dfs(1,0,&adj);
fn dfs(s: usize, e: usize, adj: &[Vec<usize>]) {
    // process node s
# println!("{s}");
    for u in &adj[s] {
        if *u != e {dfs(*u, s, adj)}
    }
}
```

The function is given two parameters: the current node $s$
and the previous node $e$.
The purpose of the parameter $e$ is to make sure
that the search only moves to nodes
that have not been visited yet.

The following function call starts the search
at node $x$:

```rust, ignore
dfs(x, 0, &adg);
```

In the first call $e=0$, because there is no
previous node, and it is allowed
to proceed to any direction in the tree.

## Dynamic programming

Dynamic programming can be used to calculate
some information during a tree traversal.
Using dynamic programming, we can, for example,
calculate in $O(n)$ time for each node of a rooted tree the
number of nodes in its subtree
or the length of the longest path from the node
to a leaf.

As an example, let us calculate for each node $s$
a value `count[s]`: the number of nodes in its subtree.
The subtree contains the node itself and
all nodes in the subtrees of its children,
so we can calculate the number of nodes
recursively using the following code:

```rust
# let adj = [vec![], vec![2, 3, 4], vec![5, 6], vec![], vec![7], vec![], vec![8], vec![], vec![]];
# let mut count = vec![0; 9];
# dfs(1,0,&adj, &mut count);
fn dfs(s: usize, e: usize, adj: &[Vec<usize>], count: &mut [usize]){
# println!("count: {:?}", &count);
    count[s] = 1;
    for u in &adj[s] {
        if *u == e {continue}
        dfs(*u, s, adj, count);
        count[s] += count[*u];
    }
}
```
