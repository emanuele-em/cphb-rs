# Cycle detection

Consider a successor graph that only contains
a path that ends in a cycle.
We may ask the following questions:
if we begin our walk at the starting node,
what is the first node in the cycle
and how many nodes does the cycle contain?

For example, in the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (5) at (0,0) {5};
\node[draw, circle] (4) at (-2,0) {4};
\node[draw, circle] (6) at (-1,1.5) {6};
\node[draw, circle] (3) at (-4,0) {3};
\node[draw, circle] (2) at (-6,0) {2};
\node[draw, circle] (1) at (-8,0) {1};

\path[draw,thick,->] (1) -- (2);
\path[draw,thick,->] (2) -- (3);
\path[draw,thick,->] (3) -- (4);
\path[draw,thick,->] (4) -- (5);
\path[draw,thick,->] (5) -- (6);
\path[draw,thick,->] (6) -- (4);
\end{tikzpicture}
</script>

we begin our walk at node 1,
the first node that belongs to the cycle is node 4, and the cycle consists
of three nodes (4, 5 and 6).

A simple way to detect the cycle is to walk in the
graph and keep track of
all nodes that have been visited. Once a node is visited
for the second time, we can conclude
that the node is the first node in the cycle.
This method works in $O(n)$ time and also uses
$O(n)$ memory.

However, there are better algorithms for cycle detection.
The time complexity of such algorithms is still $O(n)$,
but they only use $O(1)$ memory.
This is an important improvement if $n$ is large.
Next we will discuss Floyd's algorithm that
achieves these properties.

## Floyd's algorithm

**Floyd's algorithm**[^1] walks forward 
in the graph using two pointers $a$ and $b$.
Both pointers begin at a node $x$ that
is the starting node of the graph.
Then, on each turn, the pointer $a$ walks
one step forward and the pointer $b$
walks two steps forward.
The process continues until
the pointers meet each other:

```rust
#     let s = [0, 2, 3, 4, 5, 6, 4];
# println!("{s:?}");
# fn succ(i: usize) -> usize{
#     let s = [0, 2, 3, 4, 5, 6, 4];
#     s[i] 
# }
# let x = 1;
let mut a = succ(x);
# println!("a = {a}");
let mut b = succ(succ(x));
# println!("       b = {b}");
while a != b {
    a = succ(a);
# println!("a = {a}");
    b = succ(succ(b));
# println!("       b = {b}");
}
```

At this point, the pointer $a$ has walked $k$ steps
and the pointer $b$ has walked $2k$ steps,
so the length of the cycle divides $k$.
Thus, the first node that belongs to the cycle
can be found by moving the pointer $a$ to node $x$
and advancing the pointers
step by step until they meet again.

```rust
#     let s = [0, 2, 3, 4, 5, 6, 4];
# println!("{s:?}");
# fn succ(i: usize) -> usize{
#     let s = [0, 2, 3, 4, 5, 6, 4];
#     s[i] 
# }
# let x = 1;
# let mut a = succ(x);
# let mut b = succ(succ(x));
# while a != b {
#    a = succ(a);
#   b = succ(succ(b));
# }
let mut a = x;
# println!("a = {a}");
while a != b {
    a = succ(a);
# println!("a = {a}");
    b = succ(b);
# println!("       b = {b}");
}
let first = a;
# println!("                first = {first}");
```

After this, the length of the cycle
can be calculated as follows:

```rust
#     let s = [0, 2, 3, 4, 5, 6, 4];
# println!("{s:?}");
# fn succ(i: usize) -> usize{
#     let s = [0, 2, 3, 4, 5, 6, 4];
#     s[i] 
# }
# let x = 1;
# let mut a = succ(x);
# let mut b = succ(succ(x));
# while a != b {
#    a = succ(a);
#   b = succ(succ(b));
# }
# let mut a = x;
# while a != b {
#     a = succ(a);
#     b = succ(b);
# }
let first = a;
let mut b = succ(a);
let mut length = 1;
while a != b {
    b = succ(b);
    length += 1;
}
# println!("cycle length = {length}");
```

___

[^1] The idea of the algorithm is mentioned in [46] and attributed to R. W. Floyd; however, it is not known if Floyd actually discovered the algorithm.
