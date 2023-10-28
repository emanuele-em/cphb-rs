# Floyd–Warshall algorithm

The **Floyd–Warshall algorithm**
provides an alternative way to approach the problem
of finding shortest paths.
Unlike the other algorithms of this chapter,
it finds all shortest paths between the nodes
in a single run.

The algorithm maintains a two-dimensional array
that contains distances between the nodes.
First, distances are calculated only using
direct edges between the nodes,
and after this, the algorithm reduces distances
by using intermediate nodes in paths.

## Example

Let us consider how the Floyd–Warshall algorithm
works in the following graph:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {3};
\node[draw, circle] (2) at (4,3) {4};
\node[draw, circle] (3) at (1,1) {2};
\node[draw, circle] (4) at (4,1) {1};
\node[draw, circle] (5) at (6,2) {5};

\path[draw,thick,-] (1) -- node[font=\small,label=above:7] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:2] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:5] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:9] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:2] {} (5);
\path[draw,thick,-] (4) -- node[font=\small,label=below:1] {} (5);
\end{tikzpicture}
</script>

Initially, the distance from each node to itself is $0$,
and the distance between nodes $a$ and $b$ is $x$
if there is an edge between nodes $a$ and $b$ with weight $x$.
All other distances are infinite.

|   | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 5 | inf | 9 | 1 |
| 2 | 5 | 0 | 2 | inf | inf |
| 3 | inf | 2 | 0 | 7 | inf |
| 4 | 9 | inf | 7 | 0 | 2 |
| 5 | 1 | inf | inf | 2 | 0 | 

The algorithm consists of consecutive rounds.
On each round, the algorithm selects a new node
that can act as an intermediate node in paths from now on,
and distances are reduced using this node.

On the first round, node 1 is the new intermediate node.
There is a new path between nodes 2 and 4
with length 14, because node 1 connects them.
There is also a new path 
between nodes 2 and 5 with length 6.

| | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
|1 | 0 | 5 | inf | 9 | 1 |
|2 | 5 | 0 | 2 | **14** | **6** |
|3 | inf | 2 | 0 | 7 | inf |
|4 | 9 | **14** | 7 | 0 | 2 |
|5 | 1 | **6** | inf | 2 | 0 |

On the second round, node 2 is the new intermediate node.
This creates new paths between nodes 1 and 3
and between nodes 3 and 5:

| | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 5 | **7** | 9 | 1 |
| 2 | 5 | 0 | 2 | 14 | 6 |
| 3 | **7** | 2 | 0 | 7 | **8** |
| 4 | 9 | 14 | 7 | 0 | 2 |
| 5 | 1 | 6 | **8** | 2 | 0 |

On the third round, node 3 is the new intermediate round.
There is a new path between nodes 2 and 4:

| | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 5 | 7 | 9 | 1 |
| 2 | 5 | 0 | 2 | **9** | 6 |
| 3 | 7 | 2 | 0 | 7 | 8 |
| 4 | 9 | **9** | 7 | 0 | 2 |
| 5 | 1 | 6 | 8 | 2 | 0 |

The algorithm continues like this,
until all nodes have been appointed intermediate nodes.
After the algorithm has finished, the array contains
the minimum distances between any two nodes:

| | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 5 | 7 | 3 | 1 |
| 2 | 5 | 0 | 2 | 8 | 6 |
| 3 | 7 | 2 | 0 | 7 | 8 |
| 4 | 3 | 8 | 7 | 0 | 2 |
| 5 | 1 | 6 | 8 | 2 | 0 |

For example, the array tells us that the
shortest distance between nodes 2 and 4 is 8.
This corresponds to the following path:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {3};
\node[draw, circle] (2) at (4,3) {4};
\node[draw, circle] (3) at (1,1) {2};
\node[draw, circle] (4) at (4,1) {1};
\node[draw, circle] (5) at (6,2) {5};

\path[draw,thick,-] (1) -- node[font=\small,label=above:7] {} (2);
\path[draw,thick,-] (1) -- node[font=\small,label=left:2] {} (3);
\path[draw,thick,-] (3) -- node[font=\small,label=below:5] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=left:9] {} (4);
\path[draw,thick,-] (2) -- node[font=\small,label=above:2] {} (5);
\path[draw,thick,-] (4) -- node[font=\small,label=below:1] {} (5);

\path[draw=red,thick,->,line width=2pt] (3) -- (4);
\path[draw=red,thick,->,line width=2pt] (4) -- (5);
\path[draw=red,thick,->,line width=2pt] (5) -- (2);
\end{tikzpicture}
</script>

## Implementation

The advantage of the
Floyd–Warshall algorithm that it is
easy to implement.
The following code constructs a
distance matrix where `distance[a][b]`
is the shortest distance between nodes $a$ and $b$.
First, the algorithm initializes `distance`
using the adjacency matrix `adj` of the graph:

```rust
# const INF:isize = (1./0.) as u32 as isize;
# let mut n = 5;
let mut adj = [[INF, INF, INF, INF, INF, INF], [INF, INF, 5, INF, 9, 1], [INF, 5, INF, 2, INF, INF], [INF, INF, 2, INF, 7, INF], [INF, 9, INF, 7, INF, 2], [INF, 1, INF, INF, 2, INF]];
let mut distance = adj;
for i in 1..=n{
    for j in 1..=n {
        if i == j {distance[i][j] = 0}
        else if adj[i][j] != INF {distance[i][j] = adj[i][j]}
        else {distance[i][j] = INF}
    }
}
# for i in 1..=n {
#     for j in 1..=n{
          let d = distance[i][j].clone().to_string();
#         print!("{} ", if distance[i][j] > 10 { "∞" } else { &d });
#     }
#   println!("");
# }
```

After this, the shortest distances can be found as follows:

```rust
# use std::cmp::Ordering;
# const INF:isize = (1./0.) as u32 as isize;
# let mut n = 5;
# let mut adj = [[INF, INF, INF, INF, INF, INF], [INF, INF, 5, INF, 9, 1], [INF, 5, INF, 2, INF, INF], [INF, INF, 2, INF, 7, INF], [INF, 9, INF, 7, INF, 2], [INF, 1, INF, INF, 2, INF]];
# let mut distance = adj;
# for i in 1..=n{
#     for j in 1..=n {
#         if i == j {distance[i][j] = 0}
#         else if adj[i][j] != INF {distance[i][j] = adj[i][j]}
#         else {distance[i][j] = INF}
#     }
# }
for k in 1..=n{
    for i in 1..=n{
        for j in 1..=n{
            distance[i][j] = distance[i][j].min(distance[i][k]+distance[k][j]);
        }
    }
}
# for i in 1..=n {
#     for j in 1..=n{
#         print!("{} ", distance[i][j]);
#     }
#   println!("");
# }
```

The time complexity of the algorithm is $O(n^3)$,
because it contains three nested loops
that go through the nodes of the graph.

Since the implementation of the Floyd–Warshall
algorithm is simple, the algorithm can be
a good choice even if it is only needed to find a
single shortest path in the graph.
However, the algorithm can only be used when the graph
is so small that a cubic time complexity is fast enough.
___

[^1] The algorithm is named after R. W. Floyd and S. Warshall who published it independently in 1962 [23, 70].
