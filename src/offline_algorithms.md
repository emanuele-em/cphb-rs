# Offline algorithms

So far, we have discussed _online_ algorithms
for tree queries.
Those algorithms are able to process
queries one after another so that
each query is answered before receiving the next query.

However, in many problems, the online
property is not necessary.
In this section, we focus on _offline_ algorithms.
Those algorithms are given a set of queries which can
be answered in any order.
It is often easier to design an offline algorithm
compared to an online algorithm.

## Merging data and structures

One method to construct an offline algorithm
is to perform a depth-first tree traversal
and maintain data structures in nodes.
At each node $s$, we create a data structure
`d[s]` that is based on the
data structures of the children of $s$.
Then, using this data structure,
all queries related to $s$ are processed.

As an example, consider the following problem:
We are given a tree where each node has some value.
Our task is to process queries of the form
''calculate the number of nodes with value $x$
in the subtree of node $s$''.
For example, in the following tree,
the subtree of node $4$ contains two nodes
whose value is 3.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (-3,1) {2};
\node[draw, circle] (3) at (-1,1) {3};
\node[draw, circle] (4) at (1,1) {4};
\node[draw, circle] (5) at (3,1) {5};
\node[draw, circle] (6) at (-3,-1) {6};
\node[draw, circle] (7) at (-0.5,-1) {7};
\node[draw, circle] (8) at (1,-1) {8};
\node[draw, circle] (9) at (2.5,-1) {9};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (1) -- (5);
\path[draw,thick,-] (2) -- (6);
\path[draw,thick,-] (4) -- (7);
\path[draw,thick,-] (4) -- (8);
\path[draw,thick,-] (4) -- (9);

\node[color=blue] at (0,3+0.65) {2};
\node[color=blue] at (-3-0.65,1) {3};
\node[color=blue] at (-1-0.65,1) {5};
\node[color=blue] at (1+0.65,1) {3};
\node[color=blue] at (3+0.65,1) {1};
\node[color=blue] at (-3,-1-0.65) {4};
\node[color=blue] at (-0.5,-1-0.65) {4};
\node[color=blue] at (1,-1-0.65) {3};
\node[color=blue] at (2.5,-1-0.65) {1};
\end{tikzpicture}
</script>

In this problem, we can use map structures
to answer the queries.
For example, the maps for node 4 and
its children are as follows:

<script type="text/tikz">
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]

%Shape: Rectangle [id:dp6649375887623488] 
\draw   (310,160) -- (390,160) -- (390,200) -- (310,200) -- cycle ;
%Shape: Rectangle [id:dp43769353540608513] 
\draw   (240,240) -- (270,240) -- (270,280) -- (240,280) -- cycle ;
%Straight Lines [id:da3078108338949652] 
\draw    (320,180) -- (380,180) ;
%Straight Lines [id:da199350183956849] 
\draw    (250,260) -- (260,260) ;
%Shape: Rectangle [id:dp2352194846793536] 
\draw   (410,241) -- (440,241) -- (440,281) -- (410,281) -- cycle ;
%Straight Lines [id:da09630126413430129] 
\draw    (420,261) -- (430,261) ;
%Shape: Rectangle [id:dp7955174976158643] 
\draw   (330,241) -- (360,241) -- (360,281) -- (330,281) -- cycle ;
%Straight Lines [id:da30068715064839435] 
\draw    (340,261) -- (350,261) ;
%Straight Lines [id:da8116350023353112] 
\draw    (350,200) -- (420,240) ;
%Straight Lines [id:da8289090311486502] 
\draw    (350,200) -- (340,240) ;
%Straight Lines [id:da4658205008172991] 
\draw    (350,200) -- (250,240) ;

% Text Node
\draw (321,161) node [anchor=north west][inner sep=0.75pt]   [align=left] {1 \ \ \ 3 \ \ \ 4};
% Text Node
\draw (321,181) node [anchor=north west][inner sep=0.75pt]   [align=left] {1 \ \ \ 2 \ \ \ 1};
% Text Node
\draw (248,241) node [anchor=north west][inner sep=0.75pt]   [align=left] {4};
% Text Node
\draw (248,261) node [anchor=north west][inner sep=0.75pt]   [align=left] {1};
% Text Node
\draw (418,242) node [anchor=north west][inner sep=0.75pt]   [align=left] {1};
% Text Node
\draw (418,262) node [anchor=north west][inner sep=0.75pt]   [align=left] {1};
% Text Node
\draw (338,242) node [anchor=north west][inner sep=0.75pt]   [align=left] {3};
% Text Node
\draw (338,262) node [anchor=north west][inner sep=0.75pt]   [align=left] {1};


\end{tikzpicture}
</script>

If we create such a data structure for each node,
we can easily process all given queries,
because we can handle all queries related
to a node immediately after creating its
data structure. For example, the above
map structure for node 4
tells us that its subtree
contains two nodes whose value is 3.

However, it would be too slow to create
all data structures from scratch.
Instead, at each node $s$,
we create an initial data structure `d[s]` 
that only contains the value of $s$.
After this, we go through the children of $s$ and
_merge_ `d[s]` and
all data structures
`d[u]` where $u$ is a child of $s$.

For example, in the above tree, the map
for node $4$ is created by merging the following maps:

<script type="text/tikz">
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]

\draw   (240,240) -- (270,240) -- (270,280) -- (240,280) -- cycle ;
%Straight Lines [id:da199350183956849] 
\draw    (250,260) -- (260,260) ;
%Shape: Rectangle [id:dp2352194846793536] 
\draw   (402,241) -- (432,241) -- (432,281) -- (402,281) -- cycle ;
%Straight Lines [id:da09630126413430129] 
\draw    (412,261) -- (422,261) ;
%Shape: Rectangle [id:dp7955174976158643] 
\draw   (322,241) -- (352,241) -- (352,281) -- (322,281) -- cycle ;
%Straight Lines [id:da30068715064839435] 
\draw    (332,261) -- (342,261) ;
%Shape: Rectangle [id:dp6308684431000902] 
\draw   (160,240) -- (190,240) -- (190,280) -- (160,280) -- cycle ;
%Straight Lines [id:da1683488029506044] 
\draw    (170,260) -- (180,260) ;

% Text Node
\draw (248,241) node [anchor=north west][inner sep=0.75pt]   [align=left] {4};
% Text Node
\draw (248,261) node [anchor=north west][inner sep=0.75pt]   [align=left] {1};
% Text Node
\draw (410,242) node [anchor=north west][inner sep=0.75pt]   [align=left] {1};
% Text Node
\draw (410,262) node [anchor=north west][inner sep=0.75pt]   [align=left] {1};
% Text Node
\draw (330,242) node [anchor=north west][inner sep=0.75pt]   [align=left] {3};
% Text Node
\draw (330,262) node [anchor=north west][inner sep=0.75pt]   [align=left] {1};
% Text Node
\draw (168,241) node [anchor=north west][inner sep=0.75pt]   [align=left] {3};
% Text Node
\draw (168,261) node [anchor=north west][inner sep=0.75pt]   [align=left] {1};

\end{tikzpicture}
</script>

Here the first map is the initial data structure
for node 4,
and the other three maps correspond to nodes 7, 8 and 9.

The merging at node $s$ can be done as follows:
We go through the children of $s$
and at each child $u$ merge `d[s]`
and `d[u]`.
We always copy the contents from `d[u]`
to `d[s]`.
However, before this, we _swap_
the contents of `d[s]` and `d[u]`
if `d[s]` is smaller than `d[u]`.
By doing this, each value is copied only $O(\log n)$
times during the tree traversal,
which ensures that the algorithm is efficient.

To swap the contents of two data structures $a$ and $b$
efficiently, we can just use the following code:

```rust
# let mut a = 5;
# let mut b = 6;
# println!("a:{a}  b:{b}");
(a, b) = (b, a);
# println!("a:{a}  b:{b}");
```

or in alternative:
```rust
# let mut a = 5;
# let mut b = 6;
# println!("a:{a}  b:{b}");
std::mem::swap(&mut a, &mut b);
# println!("a:{a}  b:{b}");
```

## Lowest common ancestor

There is also an offline algorithm
for processing a set of
lowest common ancestor queries[^1].
The algorithm is based on the union-find data structure
(see Chapter 15.2), and the benefit of the algorithm is
that it is easier to implement than the
algorithms discussed earlier in this chapter.

The algorithm is given as input a set of pairs of nodes,
and it determines for each such pair the
lowest common ancestor of the nodes.
The algorithm performs a depth-first tree traversal
and maintains disjoint sets of nodes.
Initially, each node belongs to a separate set.
For each set, we also store the highest node in the
tree that belongs to the set.

When the algorithm visits a node $x$,
it goes through all nodes $y$ such that
the lowest common ancestor of $x$ and $y$
has to be found.
If $y$ has already been visited,
the algorithm reports that the 
lowest common ancestor of $x$ and $y$
is the highest node in the set of $y$.
Then, after processing node $x$,
the algorithm joins the sets of $x$ and its parent.

For example, suppose that we want to find the lowest
common ancestors of node pairs $(5,8)$
and $(2,7)$ in the following tree:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.85]
\node[draw, circle] (1) at (0,3) {1};
\node[draw, circle] (2) at (2,1) {4};
\node[draw, circle] (3) at (-2,1) {2};
\node[draw, circle] (4) at (0,1) {3};
\node[draw, circle] (5) at (2,-1) {7};
\node[draw, circle] (6) at (-3,-1) {5};
\node[draw, circle] (7) at (-1,-1) {6};
\node[draw, circle] (8) at (-1,-3) {8};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);
\path[draw,thick,-] (7) -- (8);
\end{tikzpicture}
</script>

In the following trees, gray nodes denote visited nodes
and dashed groups of nodes belong to the same set.
When the algorithm visits node 8, it notices that
node 5 has been visited and the highest node
in its set is 2. Thus, the lowest common ancestor
of nodes 5 and 8 is 2:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.85]
\node[draw, circle, fill=lightgray] (1) at (0,3) {1};
\node[draw, circle] (2) at (2,1) {4};
\node[draw, circle, fill=lightgray] (3) at (-2,1) {2};
\node[draw, circle] (4) at (0,1) {3};
\node[draw, circle] (5) at (2,-1) {7};
\node[draw, circle, fill=lightgray] (6) at (-3,-1) {5};
\node[draw, circle, fill=lightgray] (7) at (-1,-1) {6};
\node[draw, circle, fill=gray] (8) at (-1,-3) {8};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);
\path[draw,thick,-] (7) -- (8);

\draw [red,thick,dashed,line width=2pt,rotate around={-28:(-2,0)}] (-2.9,1.5) rectangle (-1.9,-2);


\draw [red,thick,dashed,line width=2pt] (-1.5,-0.5) rectangle (-0.5,-1.5);
\draw [red,thick,dashed,line width=2pt] (-1.5,-2.5) rectangle (-0.5,-3.5);

\draw [red,thick,dashed,line width=2pt] (0.5,3.5) rectangle (-0.5,2.5);
\draw [red,thick,dashed,line width=2pt] (0.5,1.5) rectangle (-0.5,0.5);
\draw [red,thick,dashed,line width=2pt] (2.5,1.5) rectangle (1.5,0.5);
\draw [red,thick,dashed,line width=2pt] (2.5,-0.5) rectangle (1.5,-1.5);
\end{tikzpicture}
</script>

Later, when visiting node 7,
the algorithm determines that
the lowest common ancestor of nodes 2 and 7 is 1:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.85]
\node[draw, circle, fill=lightgray] (1) at (0,3) {1};
\node[draw, circle, fill=lightgray] (2) at (2,1) {4};
\node[draw, circle, fill=lightgray] (3) at (-2,1) {2};
\node[draw, circle, fill=lightgray] (4) at (0,1) {3};
\node[draw, circle, fill=gray] (5) at (2,-1) {7};
\node[draw, circle, fill=lightgray] (6) at (-3,-1) {5};
\node[draw, circle, fill=lightgray] (7) at (-1,-1) {6};
\node[draw, circle, fill=lightgray] (8) at (-1,-3) {8};
\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (3) -- (7);
\path[draw,thick,-] (7) -- (8);

\draw [red,thick,dashed,line width=2pt] (0.5,3.5) rectangle (-3.5,-3.5);
\draw [red,thick,dashed,line width=2pt] (2.5,1.5) rectangle (1.5,0.5);
\draw [red,thick,dashed,line width=2pt] (2.5,-0.5) rectangle (1.5,-1.5);

\end{tikzpicture}
</script>

___

[^1] This algorithm was published by R. E. Tarjan in 1979 [65].
