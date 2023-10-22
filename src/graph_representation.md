#  Graph representation

There are several ways to represent graphs
in algorithms.
The choice of a data structure
depends on the size of the graph and
the way the algorithm processes it.
Next we will go through three common representations.

## Adjacency list representation

In the adjacency list representation,
each node $x$ in the graph is assigned an **adjacency list**
that consists of nodes
to which there is an edge from $x$.
Adjacency lists are the most popular
way to represent graphs, and most algorithms can be
efficiently implemented using them.

A convenient way to store the adjacency lists is to declare
an array of vectors as follows:

```rust
# const N:usize = 10;
let mut adj: [Vec<i32>; N]= Default::default();
# println!("{adj:?}");
```

The constant $N$ is chosen so that all
adjacency lists can be stored.
For example, the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (3,1) {4};

\path[draw,thick,->,>=latex] (1) -- (2);
\path[draw,thick,->,>=latex] (2) -- (3);
\path[draw,thick,->,>=latex] (2) -- (4);
\path[draw,thick,->,>=latex] (3) -- (4);
\path[draw,thick,->,>=latex] (4) -- (1);
\end{tikzpicture}
</script>

can be stored as follows:

```rust
# const N:usize = 5;
# let mut adj: [Vec<i32>; N]= Default::default();
adj[1].push(2);
adj[2].push(3);
adj[2].push(4);
adj[3].push(4);
adj[4].push(1);
# println!("{:?}", adj);
```

If the graph is undirected, it can be stored in a similar way,
but each edge is added in both directions.

For a weighted graph, the structure can be extended
as follows:

```rust
# const N:usize = 5;
let mut adj: [Vec<(i32, i32)>; N] = Default::default();
# println!("{:?}", adj);
```

In this case, the adjacency list of node $a$
contains the pair $(b,w)$
always when there is an edge from node $a$ to node $b$
with weight $w$. For example, the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (3,1) {4};

\path[draw,thick,->,>=latex] (1) -- node[font=\small,label=above:5] {} (2);
\path[draw,thick,->,>=latex] (2) -- node[font=\small,label=above:7] {} (3);
\path[draw,thick,->,>=latex] (2) -- node[font=\small,label=left:6] {} (4);
\path[draw,thick,->,>=latex] (3) -- node[font=\small,label=right:5] {} (4);
\path[draw,thick,->,>=latex] (4) -- node[font=\small,label=left:2] {} (1);
\end{tikzpicture}
</script>

can be stored as follows:

```rust
# const N:usize = 5;
# let mut adj: [Vec<(i32, i32)>; N] = Default::default();
adj[1].push((2,5));
adj[2].push((3,7));
adj[2].push((4,6));
adj[3].push((4,5));
adj[4].push((1,2));
# println!("{:?}", adj);
```

The benefit of using adjacency lists is that
we can efficiently find the nodes to which
we can move from a given node through an edge.
For example, the following loop goes through all nodes
to which we can move from node $s$:

```rust
# const N:usize = 5;
# let mut adj: [Vec<(i32, i32)>; N] = Default::default();
# adj[1].push((2,5));
# adj[2].push((3,7));
# adj[2].push((4,6));
# adj[3].push((4,5));
# adj[4].push((1,2));
# let mut i=0;
for u in adj{
    // process node u
# if i > 0 {println!("node {i}: {u:?}")}
# i +=1;
}
```

## Adjacency matrix representation

An **adjacency matrix** is a two-dimensional array
that indicates which edges the graph contains.
We can efficiently check from an adjacency matrix
if there is an edge between two nodes.
The matrix can be stored as an array

```rust
# const N:usize =4;
let adj: Vec<Vec<i32>> = Vec::new();
# println!("{adj:?}");
```

where each value \\(\\texttt{adj}[a][b]\\) indicates
whether the graph contains an edge from
node $a$ to node $b$.
If the edge is included in the graph,
then \\(\\texttt{adj}[a][b]=1\\),
and otherwise \\(\\texttt{adj}[a][b]=0\\).
For example, the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (3,1) {4};

\path[draw,thick,->,>=latex] (1) -- (2);
\path[draw,thick,->,>=latex] (2) -- (3);
\path[draw,thick,->,>=latex] (2) -- (4);
\path[draw,thick,->,>=latex] (3) -- (4);
\path[draw,thick,->,>=latex] (4) -- (1);
\end{tikzpicture}
\end{center}
can be represented as follows:
\begin{center}
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (4,4);
\node at (0.5,0.5) {1};
\node at (1.5,0.5) {0};
\node at (2.5,0.5) {0};
\node at (3.5,0.5) {0};
\node at (0.5,1.5) {0};
\node at (1.5,1.5) {0};
\node at (2.5,1.5) {0};
\node at (3.5,1.5) {1};
\node at (0.5,2.5) {0};
\node at (1.5,2.5) {0};
\node at (2.5,2.5) {1};
\node at (3.5,2.5) {1};
\node at (0.5,3.5) {0};
\node at (1.5,3.5) {1};
\node at (2.5,3.5) {0};
\node at (3.5,3.5) {0};
\node at (-0.5,0.5) {4};
\node at (-0.5,1.5) {3};
\node at (-0.5,2.5) {2};
\node at (-0.5,3.5) {1};
\node at (0.5,4.5) {1};
\node at (1.5,4.5) {2};
\node at (2.5,4.5) {3};
\node at (3.5,4.5) {4};
\end{tikzpicture}
</script>

If the graph is weighted, the adjacency matrix
representation can be extended so that
the matrix contains the weight of the edge
if the edge exists.
Using this representation, the graph


<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (3,1) {4};

\path[draw,thick,->,>=latex] (1) -- node[font=\small,label=above:5] {} (2);
\path[draw,thick,->,>=latex] (2) -- node[font=\small,label=above:7] {} (3);
\path[draw,thick,->,>=latex] (2) -- node[font=\small,label=left:6] {} (4);
\path[draw,thick,->,>=latex] (3) -- node[font=\small,label=right:5] {} (4);
\path[draw,thick,->,>=latex] (4) -- node[font=\small,label=left:2] {} (1);
\end{tikzpicture}
</script>

corresponds to the following matrix:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (4,4);
\node at (0.5,0.5) {2};
\node at (1.5,0.5) {0};
\node at (2.5,0.5) {0};
\node at (3.5,0.5) {0};
\node at (0.5,1.5) {0};
\node at (1.5,1.5) {0};
\node at (2.5,1.5) {0};
\node at (3.5,1.5) {5};
\node at (0.5,2.5) {0};
\node at (1.5,2.5) {0};
\node at (2.5,2.5) {7};
\node at (3.5,2.5) {6};
\node at (0.5,3.5) {0};
\node at (1.5,3.5) {5};
\node at (2.5,3.5) {0};
\node at (3.5,3.5) {0};
\node at (-0.5,0.5) {4};
\node at (-0.5,1.5) {3};
\node at (-0.5,2.5) {2};
\node at (-0.5,3.5) {1};
\node at (0.5,4.5) {1};
\node at (1.5,4.5) {2};
\node at (2.5,4.5) {3};
\node at (3.5,4.5) {4};
\end{tikzpicture}
</script>

The drawback of the adjacency matrix representation
is that the matrix contains $n^2$ elements,
and usually most of them are zero.
For this reason, the representation cannot be used
if the graph is large.

## Edge list representation

An **edge list** contains all edges of a graph
in some order.
This is a convenient way to represent a graph
if the algorithm processes all edges of the graph
and it is not needed to find edges that start
at a given node.

The edge list can be stored in a vector

```rust
let mut edges: Vec<(i32, i32)> = Vec::new();
# println!("{edges:?}");
```

where each pair $(a,b)$ denotes that
there is an edge from node $a$ to node $b$.
Thus, the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (3,1) {4};

\path[draw,thick,->,>=latex] (1) -- (2);
\path[draw,thick,->,>=latex] (2) -- (3);
\path[draw,thick,->,>=latex] (2) -- (4);
\path[draw,thick,->,>=latex] (3) -- (4);
\path[draw,thick,->,>=latex] (4) -- (1);
\end{tikzpicture}
</script>

can be represented as follows:

```rust
# let mut edges: Vec<(i32, i32)> = Vec::new();
edges.push((1,2));
edges.push((2,3));
edges.push((2,4));
edges.push((3,4));
edges.push((4,1));
# println!("{edges:?}");
```

If the graph is weighted, the structure can
be extended as follows:

```rust
let mut edges: Vec<(i32, i32, i32)> = Vec::new();
# println!("{edges:?}");
```

Each element in this list is of the
form $(a,b,w)$, which means that there
is an edge from node $a$ to node $b$ with weight $w$.
For example, the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,3) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (3,1) {4};

\path[draw,thick,->,>=latex] (1) -- node[font=\small,label=above:5] {} (2);
\path[draw,thick,->,>=latex] (2) -- node[font=\small,label=above:7] {} (3);
\path[draw,thick,->,>=latex] (2) -- node[font=\small,label=left:6] {} (4);
\path[draw,thick,->,>=latex] (3) -- node[font=\small,label=right:5] {} (4);
\path[draw,thick,->,>=latex] (4) -- node[font=\small,label=left:2] {} (1);
\end{tikzpicture}
</script>

can be represented as follows:

```rust
# let mut edges: Vec<(i32, i32, i32)> = Vec::new();
edges.push((1,2,5));
edges.push((2,3,7));
edges.push((2,4,6));
edges.push((3,4,5));
edges.push((4,1,2));
# println!("{edges:?}");
```
