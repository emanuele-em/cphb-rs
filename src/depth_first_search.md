#  Depth-first search

**Depth-first search** (DFS)
is a straightforward graph traversal technique.
The algorithm begins at a starting node,
and proceeds to all other nodes that are
reachable from the starting node using
the edges of the graph.

Depth-first search always follows a single
path in the graph as long as it finds
new nodes.
After this, it returns to previous
nodes and begins to explore other parts of the graph.
The algorithm keeps track of visited nodes,
so that it processes each node only once.

## Example

Let us consider how depth-first search processes
the following graph:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (5);
\path[draw,thick,-] (2) -- (5);
\end{tikzpicture}
</script>

We may begin the search at any node of the graph;
now we will begin the search at node 1.

The search first proceeds to node 2:


<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle,fill=lightgray] (1) at (1,5) {1};
\node[draw, circle,fill=lightgray] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (5);
\path[draw,thick,-] (2) -- (5);

\path[draw=red,thick,->,line width=2pt] (1) -- (2);
\end{tikzpicture}
</script>

After this, nodes 3 and 5 will be visited:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle,fill=lightgray] (1) at (1,5) {1};
\node[draw, circle,fill=lightgray] (2) at (3,5) {2};
\node[draw, circle,fill=lightgray] (3) at (5,4) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle,fill=lightgray] (5) at (3,3) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (5);
\path[draw,thick,-] (2) -- (5);

\path[draw=red,thick,->,line width=2pt] (1) -- (2);
\path[draw=red,thick,->,line width=2pt] (2) -- (3);
\path[draw=red,thick,->,line width=2pt] (3) -- (5);
\end{tikzpicture}
</script>

The neighbors of node 5 are 2 and 3,
but the search has already visited both of them,
so it is time to return to the previous nodes.
Also the neighbors of nodes 3 and 2
have been visited, so we next move
from node 1 to node 4:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle,fill=lightgray] (1) at (1,5) {1};
\node[draw, circle,fill=lightgray] (2) at (3,5) {2};
\node[draw, circle,fill=lightgray] (3) at (5,4) {3};
\node[draw, circle,fill=lightgray] (4) at (1,3) {4};
\node[draw, circle,fill=lightgray] (5) at (3,3) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (5);
\path[draw,thick,-] (2) -- (5);

\path[draw=red,thick,->,line width=2pt] (1) -- (4);
\end{tikzpicture}
</script>

After this, the search terminates because it has visited
all nodes.

The time complexity of depth-first search is $O(n+m)$
where $n$ is the number of nodes and $m$ is the
number of edges,
because the algorithm processes each node and edge once.

## Implementation

Depth-first search can be conveniently
implemented using recursion.
The following function _dfs_ begins
a depth-first search at a given node.
The function assumes that the graph is
stored as adjacency lists in an array

```rust
# const N:usize = 10;
let mut adj: [Vec<i32>; N]= Default::default();
# println!("{adj:?}");
```

and also maintains an array

```rust
let mut visited: Vec<bool> = Vec::new();
# println!("{visited:?}");
```

that keeps track of the visited nodes.
Initially, each array value is `false`,
and when the search arrives at node $s$,
the value of `visited[s]` becomes `true`.
The function can be implemented as follows:

```rust
# const N:usize = 10;
# let mut adj: [Vec<i32>; N]= Default::default();
# let mut visited: Vec<bool> = Vec::new();
fn dfs(s: usize, adj: &[Vec<i32>],visited: &mut Vec<bool>){
    if visited[s] {return}
    visited[s] = true;
    // process node s
    for &u in &adj[s] {
        dfs(u as usize, adj, visited);
    }
}
```
