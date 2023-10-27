# Dijkstra’s algorithm

**Dijkstra's algorithm**
finds shortest
paths from the starting node to all nodes of the graph,
like the Bellman–Ford algorithm.
The benefit of Dijsktra's algorithm is that
it is more efficient and can be used for
processing large graphs.
However, the algorithm requires that there
are no negative weight edges in the graph.

Like the Bellman–Ford algorithm,
Dijkstra's algorithm maintains distances
to the nodes and reduces them during the search.
Dijkstra's algorithm is efficient, because
it only processes
each edge in the graph once, using the fact
that there are no negative edges.

## Example

Let us consider how Dijkstra's algorithm
works in the following graph when the
starting node is node 1:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {3};
\node[draw, circle] (2) at (4,3) {4};
\node[draw, circle] (3) at (1,1) {2};
\node[draw, circle] (4) at (4,1) {1};
\node[draw, circle] (5) at (6,2) {5};

\node[color=red] at (1,3+0.6) {inf};
\node[color=red] at (4,3+0.6) {inf};
\node[color=red] at (1,1-0.6) {inf};
\node[color=red] at (4,1-0.6) {0};
\node[color=red] at (6,2-0.6) {inf};

\path[draw,thick,-] (1) -- node[font=\small,label=above:6] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:2] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:5] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:9] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:2] {} (5);
\path[draw,thick,-] (4) -- node[font=\small,label=below:1] {} (5);
\end{tikzpicture}
</script>

Like in the Bellman–Ford algorithm,
initially the distance to the starting node is 0
and the distance to all other nodes is infinite.

At each step, Dijkstra's algorithm selects a node
that has not been processed yet and whose distance
is as small as possible.
The first such node is node 1 with distance 0.

When a node is selected, the algorithm
goes through all edges that start at the node
and reduces the distances using them:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {3};
\node[draw, circle] (2) at (4,3) {4};
\node[draw, circle] (3) at (1,1) {2};
\node[draw, circle, fill=lightgray] (4) at (4,1) {1};
\node[draw, circle] (5) at (6,2) {5};

\node[color=red] at (1,3+0.6) {inf};
\node[color=red] at (4,3+0.6) {9};
\node[color=red] at (1,1-0.6) {5};
\node[color=red] at (4,1-0.6) {0};
\node[color=red] at (6,2-0.6) {1};

\path[draw,thick,-] (1) -- node[font=\small,label=above:6] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:2] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:5] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:9] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:2] {} (5);
\path[draw,thick,-] (4) -- node[font=\small,label=below:1] {} (5);

\path[draw=red,thick,->,line width=2pt] (4) -- (2);
\path[draw=red,thick,->,line width=2pt] (4) -- (3);
\path[draw=red,thick,->,line width=2pt] (4) -- (5);
\end{tikzpicture}
</script>

In this case,
the edges from node 1 reduced the distances of
nodes 2, 4 and 5, whose distances are now 5, 9 and 1.

The next node to be processed is node 5 with distance 1.
This reduces the distance to node 4 from 9 to 3:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (1,3) {3};
\node[draw, circle] (2) at (4,3) {4};
\node[draw, circle] (3) at (1,1) {2};
\node[draw, circle, fill=lightgray] (4) at (4,1) {1};
\node[draw, circle, fill=lightgray] (5) at (6,2) {5};

\node[color=red] at (1,3+0.6) {inf};
\node[color=red] at (4,3+0.6) {3};
\node[color=red] at (1,1-0.6) {5};
\node[color=red] at (4,1-0.6) {0};
\node[color=red] at (6,2-0.6) {1};

\path[draw,thick,-] (1) -- node[font=\small,label=above:6] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:2] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:5] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:9] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:2] {} (5);
\path[draw,thick,-] (4) -- node[font=\small,label=below:1] {} (5);

\path[draw=red,thick,->,line width=2pt] (5) -- (2);
\end{tikzpicture}
</script>

After this, the next node is node 4, which reduces
the distance to node 3 to 9:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {3};
\node[draw, circle, fill=lightgray] (2) at (4,3) {4};
\node[draw, circle] (3) at (1,1) {2};
\node[draw, circle, fill=lightgray] (4) at (4,1) {1};
\node[draw, circle, fill=lightgray] (5) at (6,2) {5};
\node[color=red] at (1,3+0.6) {9};
\node[color=red] at (4,3+0.6) {3};
\node[color=red] at (1,1-0.6) {5};
\node[color=red] at (4,1-0.6) {0};
\node[color=red] at (6,2-0.6) {1};
\path[draw,thick,-] (1) -- node[font=\small,label=above:6] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:2] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:5] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:9] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:2] {} (5);
\path[draw,thick,-] (4) -- node[font=\small,label=below:1] {} (5);
\path[draw=red,thick,->,line width=2pt] (2) -- (1);
\end{tikzpicture}
</script>

A remarkable property in Dijkstra's algorithm is that
whenever a node is selected, its distance is final.
For example, at this point of the algorithm,
the distances 0, 1 and 3 are the final distances
to nodes 1, 5 and 4.

After this, the algorithm processes the two
remaining nodes, and the final distances are as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle, fill=lightgray] (1) at (1,3) {3};
\node[draw, circle, fill=lightgray] (2) at (4,3) {4};
\node[draw, circle, fill=lightgray] (3) at (1,1) {2};
\node[draw, circle, fill=lightgray] (4) at (4,1) {1};
\node[draw, circle, fill=lightgray] (5) at (6,2) {5};

\node[color=red] at (1,3+0.6) {7};
\node[color=red] at (4,3+0.6) {3};
\node[color=red] at (1,1-0.6) {5};
\node[color=red] at (4,1-0.6) {0};
\node[color=red] at (6,2-0.6) {1};

\path[draw,thick,-] (1) -- node[font=\small,label=above:6] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:2] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:5] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:9] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:2] {} (5);
\path[draw,thick,-] (4) -- node[font=\small,label=below:1] {} (5);
\end{tikzpicture}
</script>

## Negative edges

The efficiency of Dijkstra's algorithm is
based on the fact that the graph does not
contain negative edges.
If there is a negative edge,
the algorithm may give incorrect results.
As an example, consider the following graph:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,0) {1};
\node[draw, circle] (2) at (2,1) {2};
\node[draw, circle] (3) at (2,-1) {3};
\node[draw, circle] (4) at (4,0) {4};

\path[draw,thick,-] (1) -- node[font=\small,label=above:2] {} (2);
\path[draw,thick,-] (2) -- node[font=\small,label=above:3] {} (4);
\path[draw,thick,-] (1) -- node[font=\small,label=below:6] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:-5] {} (4);
\end{tikzpicture}
</script>

The shortest path from node 1 to node 4 is
$1 \rightarrow 3 \rightarrow 4$
and its length is 1.
However, Dijkstra's algorithm
finds the path $1 \rightarrow 2 \rightarrow 4$
by following the minimum weight edges.
The algorithm does not take into account that
on the other path, the weight $-5$
compensates the previous large weight $6$.

## Implementation

The following implementation of Dijkstra's algorithm
calculates the minimum distances from a node `x`
to other nodes of the graph.
The graph is stored as adjacency lists
so that `adj[$a$]` contains a pair `(b,w)`
always when there is an edge from node `a` to node `b`
with weight `w`.

An efficient implementation of Dijkstra's algorithm
requires that it is possible to efficiently find the
minimum distance node that has not been processed.
An appropriate data structure for this is a priority queue
that contains the nodes ordered by their distances.
Using a priority queue, the next node to be processed
can be retrieved in logarithmic time.

In the following code, the priority queue
`q` contains pairs of the form `(-d,x)`,
meaning that the current distance to node `x` is `d`.
The array `distance` contains the distance to
each node, and the array `processed` indicates
whether a node has been processed.
Initially the distance is `0` to `x` and `INF` to all other nodes.

```rust
# use std::cmp::Reverse;
# const INF:isize = (1./0.) as u32 as isize;
# let mut x = 1;
# let mut n = 6;
# let mut adj: [Vec<_>; 6]=[vec![], vec![(2,5), (4,7), (3,3)], vec![(4,3), (5,2), (1, 5)], vec![(4, 1), (1, 3)], vec![(5,2), (1, 7), (3, 1), (2, 3)],  vec![(4, 2), (2, 2)]];
let mut q = std::collections::BinaryHeap::new();
let mut processed = vec![false; n];
let mut distance = vec![INF; n];
distance[x] = 0;
q.push((Reverse(0),x));
while !q.is_empty(){
    let a = q.pop().unwrap().1;
    if processed[a] {continue}
    processed[a] = true;
    for &u in &adj[a]{
        let (b, w) = u;
        if (distance[a] + w) < distance[b] {
            distance[b] = distance[a] + w;
            q.push((Reverse(distance[b]), b));
        }
    }
}
# println!("{:?}", &distance[1..]);
```

Note that the priority queue push with `Reverse()`.
The reason for this is that the
default version of the Rust `BinaryHeap` finds maximum
elements (max-heap), while we want to find minimum elements (min-heap).
By using `std::Comparing::Reverse` helper the cmp Ordering is considered in reverse order.
Also note that there may be several instances of the same
node in the priority queue; however, only the instance with the
minimum distance will be processed.

The time complexity of the above implementation is
$O(n+m \log m)$, because the algorithm goes through
all nodes of the graph and adds for each edge
at most one distance to the priority queue.

___

[^1] E. W. Dijkstra published the algorithm in 1959 [14]; however, his original paper does not mention how to implement the algorithm efficiently.
