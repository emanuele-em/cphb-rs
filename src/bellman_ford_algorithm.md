# Bellman–Ford algorithm

The **Bellman–Ford algorithm** finds
shortest paths from a starting node to all
nodes of the graph.
The algorithm can process all kinds of graphs,
provided that the graph does not contain a
cycle with negative length.
If the graph contains a negative cycle,
the algorithm can detect this.

The algorithm keeps track of distances
from the starting node to all nodes of the graph.
Initially, the distance to the starting node is 0
and the distance to all other nodes in infinite.
The algorithm reduces the distances by finding
edges that shorten the paths until it is not
possible to reduce any distance.

## Example 

Let us consider how the Bellman–Ford algorithm
works in the following graph:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\node[draw, circle] (5) at (6,2) {6};
\node[color=red] at (1,3+0.55) {0};
\node[color=red] at (4,3+0.55) { inf };
\node[color=red] at (1,1-0.55) {inf};
\node[color=red] at (4,1-0.55) {inf};
\node[color=red] at (6,2-0.55) {inf};
\path[draw,thick,-] (1) -- node[font=\small,label=above:5] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:3] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:1] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:3] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:2] {} (5);
\path[draw,thick,-] (4) -- node[font=\small,label=below:2] {} (5);
\path[draw,thick,-] (1) -- node[font=\small,label=above:7] {} (4);
\end{tikzpicture}
</script>

Each node of the graph is assigned a distance.
Initially, the distance to the starting node is 0,
and the distance to all other nodes is infinite.

The algorithm searches for edges that reduce distances.
First, all edges from node 1 reduce distances:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\node[draw, circle] (5) at (6,2) {5};
\node[color=red] at (1,3+0.55) {0};
\node[color=red] at (4,3+0.55) {5};
\node[color=red] at (1,1-0.55) {3};
\node[color=red] at (4,1-0.55) {7};
\node[color=red] at (6,2-0.55) {inf};
\path[draw,thick,-] (1) -- node[font=\small,label=above:5] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:3] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:1] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:3] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:2] {} (5);
\path[draw,thick,-] (4) -- node[font=\small,label=below:2] {} (5);
\path[draw,thick,-] (1) -- node[font=\small,label=above:7] {} (4);

\path[draw=red,thick,->,line width=2pt] (1) -- (2);
\path[draw=red,thick,->,line width=2pt] (1) -- (3);
\path[draw=red,thick,->,line width=2pt] (1) -- (4);
\end{tikzpicture}
</script>

After this, edges
$2 \rightarrow 5$ and $3 \rightarrow 4$
reduce distances:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\node[draw, circle] (5) at (6,2) {5};
\node[color=red] at (1,3+0.55) {0};
\node[color=red] at (4,3+0.55) {5};
\node[color=red] at (1,1-0.55) {3};
\node[color=red] at (4,1-0.55) {4};
\node[color=red] at (6,2-0.55) {7};
\path[draw,thick,-] (1) -- node[font=\small,label=above:5] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:3] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:1] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:3] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:2] {} (5);
\path[draw,thick,-] (4) -- node[font=\small,label=below:2] {} (5);
\path[draw,thick,-] (1) -- node[font=\small,label=above:7] {} (4);

\path[draw=red,thick,->,line width=2pt] (2) -- (5);
\path[draw=red,thick,->,line width=2pt] (3) -- (4);
\end{tikzpicture}
</script>

Finally, there is one more change:

<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\node[draw, circle] (5) at (6,2) {5};
\node[color=red] at (1,3+0.55) {0};
\node[color=red] at (4,3+0.55) {5};
\node[color=red] at (1,1-0.55) {3};
\node[color=red] at (4,1-0.55) {4};
\node[color=red] at (6,2-0.55) {6};
\path[draw,thick,-] (1) -- node[font=\small,label=above:5] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:3] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:1] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:3] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:2] {} (5);
\path[draw,thick,-] (4) -- node[font=\small,label=below:2] {} (5);
\path[draw,thick,-] (1) -- node[font=\small,label=above:7] {} (4);

\path[draw=red,thick,->,line width=2pt] (4) -- (5);
\end{tikzpicture}
</script>


After this, no edge can reduce any distance.
This means that the distances are final,
and we have successfully
calculated the shortest distances
from the starting node to all nodes of the graph.

For example, the shortest distance 3
from node 1 to node 5 corresponds to
the following path:


<script type="text/tikz">
\begin{tikzpicture}
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (4,3) {2};
\node[draw, circle] (3) at (1,1) {3};
\node[draw, circle] (4) at (4,1) {4};
\node[draw, circle] (5) at (6,2) {5};
\node[color=red] at (1,3+0.55) {0};
\node[color=red] at (4,3+0.55) {5};
\node[color=red] at (1,1-0.55) {3};
\node[color=red] at (4,1-0.55) {4};
\node[color=red] at (6,2-0.55) {6};
\path[draw,thick,-] (1) -- node[font=\small,label=above:5] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:3] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:1] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:3] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:2] {} (5);
\path[draw,thick,-] (4) -- node[font=\small,label=below:2] {} (5);
\path[draw,thick,-] (1) -- node[font=\small,label=above:7] {} (4);

\path[draw=red,thick,->,line width=2pt] (1) -- (3);
\path[draw=red,thick,->,line width=2pt] (3) -- (4);
\path[draw=red,thick,->,line width=2pt] (4) -- (5);
\end{tikzpicture}
</script>

## Implementation

The following implementation of the
Bellman–Ford algorithm determines the shortest distances
from a node $x$ to all nodes of the graph.
The code assumes that the graph is stored
as an edge list `edges`
that consists of tuples of the form $(a,b,w)$,
meaning that there is an edge from node $a$ to node $b$
with weight $w$.

The algorithm consists of $n-1$ rounds,
and on each round the algorithm goes through
all edges of the graph and tries to
reduce the distances.
The algorithm constructs an array `distance`
that will contain the distances from $x$
to all nodes of the graph.
The constant `INF` denotes an infinite distance.

```rust
# use std::cmp::Ordering;
# const INF:usize = (1./0.) as u32 as usize;
# let mut x = 1;
# let mut n = 6;
# let mut edges=vec![(1,2,5), (1,4,7), (1,3,3), (2,4,3), (2,5,2), (2, 1, 5), (3, 4, 1), (3, 1, 3), (4,5,2), (4, 1, 7), (4, 3, 1), (4, 2, 3),  (5, 4, 2), (5, 2, 2)];
let mut distance = vec![INF; n];
distance[x] = 0;
for _ in 0..n{
    for e in &edges{
        let (a, b, w) = *e;
        distance[b] = distance[b].min(distance[a]+w);
    }
}
# println!("{:?}", &distance[1..]);
```
The time complexity of the algorithm is $O(nm)$,
because the algorithm consists of $n-1$ rounds and
iterates through all $m$ edges during a round.
If there are no negative cycles in the graph,
all distances are final after $n-1$ rounds,
because each shortest path can contain at most $n-1$ edges.

In practice, the final distances can usually
be found faster than in $n-1$ rounds.
Thus, a possible way to make the algorithm more efficient
is to stop the algorithm if no distance
can be reduced during a round.

## Negative cycles

The Bellman–Ford algorithm can also be used to
check if the graph contains a cycle with negative length.
For example, the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,0) {1};
\node[draw, circle] (2) at (2,1) {2};
\node[draw, circle] (3) at (2,-1) {3};
\node[draw, circle] (4) at (4,0) {4};

\path[draw,thick,-] (1) -- node[font=\small,label=above:3] {} (2);
\path[draw,thick,-] (2) -- node[font=\small,label=above:1] {} (4);
\path[draw,thick,-] (1) -- node[font=\small,label=below:5] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:-7] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=right:2] {} (3);
\end{tikzpicture}
</script>

contains a negative cycle
$2 \rightarrow 3 \rightarrow 4 \rightarrow 2$
with length $-4$.

If the graph contains a negative cycle,
we can shorten infinitely many times
any path that contains the cycle by repeating the cycle
again and again.
Thus, the concept of a shortest path
is not meaningful in this situation.

A negative cycle can be detected
using the Bellman–Ford algorithm by
running the algorithm for $n$ rounds.
If the last round reduces any distance,
the graph contains a negative cycle.
Note that this algorithm can be used to
search for
a negative cycle in the whole graph
regardless of the starting node.

___

[^1] The algorithm is named after R. E. Bellman and L. R. Ford who published it independently in 1958 and 1956, respectively [5, 24]
