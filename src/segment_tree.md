# Segment tree

A **segment tree** [^1] is a data structure
that supports two operations:
processing a range query and
updating an array value.
Segment trees can support
sum queries, minimum and maximum queries and many other
queries so that both operations work in $O(\log n)$ time.

Compared to a binary indexed tree,
the advantage of a segment tree is that it is
a more general data structure.
While binary indexed trees only support
sum queries,
segment trees also support other queries.
On the other hand, a segment tree requires more
memory and is a bit more difficult to implement.

## Structure

A segment tree is a binary tree
such that the nodes on the bottom level of the tree
correspond to the array elements,
and the other nodes
contain information needed for processing range queries.

In this section, we assume that the size
of the array is a power of two and zero-based
indexing is used, because it is convenient to build
a segment tree for such an array.
If the size of the array is not a power of two,
we can always append extra elements to it.

We will first discuss segment trees that support sum queries.
As an example, consider the following array:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {5};
\node at (1.5,0.5) {8};
\node at (2.5,0.5) {6};
\node at (3.5,0.5) {3};
\node at (4.5,0.5) {2};
\node at (5.5,0.5) {7};
\node at (6.5,0.5) {2};
\node at (7.5,0.5) {6};

\footnotesize
\node at (0.5,1.4) {0};
\node at (1.5,1.4) {1};
\node at (2.5,1.4) {2};
\node at (3.5,1.4) {3};
\node at (4.5,1.4) {4};
\node at (5.5,1.4) {5};
\node at (6.5,1.4) {6};
\node at (7.5,1.4) {7};
\end{tikzpicture}
</script>

The corresponding segment tree is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node[anchor=center] at (0.5, 0.5) {5};
\node[anchor=center] at (1.5, 0.5) {8};
\node[anchor=center] at (2.5, 0.5) {6};
\node[anchor=center] at (3.5, 0.5) {3};
\node[anchor=center] at (4.5, 0.5) {2};
\node[anchor=center] at (5.5, 0.5) {7};
\node[anchor=center] at (6.5, 0.5) {2};
\node[anchor=center] at (7.5, 0.5) {6};

\node[draw, circle] (a) at (1,2.5) {13};
\path[draw,thick,-] (a) -- (0.5,1);
\path[draw,thick,-] (a) -- (1.5,1);
\node[draw, circle,minimum size=22pt] (b) at (3,2.5) {9};
\path[draw,thick,-] (b) -- (2.5,1);
\path[draw,thick,-] (b) -- (3.5,1);
\node[draw, circle,minimum size=22pt] (c) at (5,2.5) {9};
\path[draw,thick,-] (c) -- (4.5,1);
\path[draw,thick,-] (c) -- (5.5,1);
\node[draw, circle,minimum size=22pt] (d) at (7,2.5) {8};
\path[draw,thick,-] (d) -- (6.5,1);
\path[draw,thick,-] (d) -- (7.5,1);

\node[draw, circle] (i) at (2,4.5) {22};
\path[draw,thick,-] (i) -- (a);
\path[draw,thick,-] (i) -- (b);
\node[draw, circle] (j) at (6,4.5) {17};
\path[draw,thick,-] (j) -- (c);
\path[draw,thick,-] (j) -- (d);

\node[draw, circle] (m) at (4,6.5) {39};
\path[draw,thick,-] (m) -- (i);
\path[draw,thick,-] (m) -- (j);
\end{tikzpicture}
</script>

Each internal tree node
corresponds to an array range
whose size is a power of two.
In the above tree, the value of each internal
node is the sum of the corresponding array values,
and it can be calculated as the sum of
the values of its left and right child node.

It turns out that any range \\( [a,b]\\)
can be divided into $O(\log n)$ ranges
whose values are stored in tree nodes.
For example, consider the range [2,7]:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=gray!50] (2,0) rectangle (8,1);
\draw (0,0) grid (8,1);

\node[anchor=center] at (0.5, 0.5) {5};
\node[anchor=center] at (1.5, 0.5) {8};
\node[anchor=center] at (2.5, 0.5) {6};
\node[anchor=center] at (3.5, 0.5) {3};
\node[anchor=center] at (4.5, 0.5) {2};
\node[anchor=center] at (5.5, 0.5) {7};
\node[anchor=center] at (6.5, 0.5) {2};
\node[anchor=center] at (7.5, 0.5) {6};

\footnotesize
\node at (0.5,1.4) {0};
\node at (1.5,1.4) {1};
\node at (2.5,1.4) {2};
\node at (3.5,1.4) {3};
\node at (4.5,1.4) {4};
\node at (5.5,1.4) {5};
\node at (6.5,1.4) {6};
\node at (7.5,1.4) {7};
\end{tikzpicture}
</script>

Here $sum_q(2,7)=6+3+2+7+2+6=26$.
In this case, the following two tree nodes
correspond to the range:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node[anchor=center] at (0.5, 0.5) {5};
\node[anchor=center] at (1.5, 0.5) {8};
\node[anchor=center] at (2.5, 0.5) {6};
\node[anchor=center] at (3.5, 0.5) {3};
\node[anchor=center] at (4.5, 0.5) {2};
\node[anchor=center] at (5.5, 0.5) {7};
\node[anchor=center] at (6.5, 0.5) {2};
\node[anchor=center] at (7.5, 0.5) {6};

\node[draw, circle] (a) at (1,2.5) {13};
\path[draw,thick,-] (a) -- (0.5,1);
\path[draw,thick,-] (a) -- (1.5,1);
\node[draw, circle,fill=gray!50,minimum size=22pt] (b) at (3,2.5) {9};
\path[draw,thick,-] (b) -- (2.5,1);
\path[draw,thick,-] (b) -- (3.5,1);
\node[draw, circle,minimum size=22pt] (c) at (5,2.5) {9};
\path[draw,thick,-] (c) -- (4.5,1);
\path[draw,thick,-] (c) -- (5.5,1);
\node[draw, circle,minimum size=22pt] (d) at (7,2.5) {8};
\path[draw,thick,-] (d) -- (6.5,1);
\path[draw,thick,-] (d) -- (7.5,1);

\node[draw, circle] (i) at (2,4.5) {22};
\path[draw,thick,-] (i) -- (a);
\path[draw,thick,-] (i) -- (b);
\node[draw, circle,fill=gray!50] (j) at (6,4.5) {17};
\path[draw,thick,-] (j) -- (c);
\path[draw,thick,-] (j) -- (d);

\node[draw, circle] (m) at (4,6.5) {39};
\path[draw,thick,-] (m) -- (i);
\path[draw,thick,-] (m) -- (j);
\end{tikzpicture}
</script>

Thus, another way to calculate the sum is $9+17=26$.

When the sum is calculated using nodes
located as high as possible in the tree,
at most two nodes on each level
of the tree are needed.
Hence, the total number of nodes
is $O(\log n)$.

After an array update,
we should update all nodes
whose value depends on the updated value.
This can be done by traversing the path
from the updated array element to the top node
and updating the nodes along the path.

The following picture shows which tree nodes
change if the array value 7 changes:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=gray!50] (5,0) rectangle (6,1);
\draw (0,0) grid (8,1);

\node[anchor=center] at (0.5, 0.5) {5};
\node[anchor=center] at (1.5, 0.5) {8};
\node[anchor=center] at (2.5, 0.5) {6};
\node[anchor=center] at (3.5, 0.5) {3};
\node[anchor=center] at (4.5, 0.5) {2};
\node[anchor=center] at (5.5, 0.5) {7};
\node[anchor=center] at (6.5, 0.5) {2};
\node[anchor=center] at (7.5, 0.5) {6};

\node[draw, circle] (a) at (1,2.5) {13};
\path[draw,thick,-] (a) -- (0.5,1);
\path[draw,thick,-] (a) -- (1.5,1);
\node[draw, circle,minimum size=22pt] (b) at (3,2.5) {9};
\path[draw,thick,-] (b) -- (2.5,1);
\path[draw,thick,-] (b) -- (3.5,1);
\node[draw, circle,minimum size=22pt,fill=gray!50] (c) at (5,2.5) {9};
\path[draw,thick,-] (c) -- (4.5,1);
\path[draw,thick,-] (c) -- (5.5,1);
\node[draw, circle,minimum size=22pt] (d) at (7,2.5) {8};
\path[draw,thick,-] (d) -- (6.5,1);
\path[draw,thick,-] (d) -- (7.5,1);

\node[draw, circle] (i) at (2,4.5) {22};
\path[draw,thick,-] (i) -- (a);
\path[draw,thick,-] (i) -- (b);
\node[draw, circle,fill=gray!50] (j) at (6,4.5) {17};
\path[draw,thick,-] (j) -- (c);
\path[draw,thick,-] (j) -- (d);

\node[draw, circle,fill=gray!50] (m) at (4,6.5) {39};
\path[draw,thick,-] (m) -- (i);
\path[draw,thick,-] (m) -- (j);
\end{tikzpicture}
</script>

The path from bottom to top
always consists of $O(\log n)$ nodes,
so each update changes $O(\log n)$ nodes in the tree.

## Implementation

We store a segment tree as an array
of $2n$ elements where $n$ is the size of
the original array and a power of two.
The tree nodes are stored from top to bottom:
\\( \\texttt{tree}[1]\\)  is the top node,
\\(\\texttt{tree}[2]\\) and \\( \texttt{tree}[3]\\)
are its children, and so on.
Finally, the values from \\(\\texttt{tree}[n]\\)
to \\(\\texttt{tree}[2n-1]\\) correspond to
the values of the original array
on the bottom level of the tree.

For example, the segment tree:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node[anchor=center] at (0.5, 0.5) {5};
\node[anchor=center] at (1.5, 0.5) {8};
\node[anchor=center] at (2.5, 0.5) {6};
\node[anchor=center] at (3.5, 0.5) {3};
\node[anchor=center] at (4.5, 0.5) {2};
\node[anchor=center] at (5.5, 0.5) {7};
\node[anchor=center] at (6.5, 0.5) {2};
\node[anchor=center] at (7.5, 0.5) {6};

\node[draw, circle] (a) at (1,2.5) {13};
\path[draw,thick,-] (a) -- (0.5,1);
\path[draw,thick,-] (a) -- (1.5,1);
\node[draw, circle,minimum size=22pt] (b) at (3,2.5) {9};
\path[draw,thick,-] (b) -- (2.5,1);
\path[draw,thick,-] (b) -- (3.5,1);
\node[draw, circle,minimum size=22pt] (c) at (5,2.5) {9};
\path[draw,thick,-] (c) -- (4.5,1);
\path[draw,thick,-] (c) -- (5.5,1);
\node[draw, circle,minimum size=22pt] (d) at (7,2.5) {8};
\path[draw,thick,-] (d) -- (6.5,1);
\path[draw,thick,-] (d) -- (7.5,1);

\node[draw, circle] (i) at (2,4.5) {22};
\path[draw,thick,-] (i) -- (a);
\path[draw,thick,-] (i) -- (b);
\node[draw, circle] (j) at (6,4.5) {17};
\path[draw,thick,-] (j) -- (c);
\path[draw,thick,-] (j) -- (d);

\node[draw, circle] (m) at (4,6.5) {39};
\path[draw,thick,-] (m) -- (i);
\path[draw,thick,-] (m) -- (j);
\end{tikzpicture}
</script>

is stored as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (15,1);

\node at (0.5,0.5) {39};
\node at (1.5,0.5) {22};
\node at (2.5,0.5) {17};
\node at (3.5,0.5) {13};
\node at (4.5,0.5) {9};
\node at (5.5,0.5) {9};
\node at (6.5,0.5) {8};
\node at (7.5,0.5) {5};
\node at (8.5,0.5) {8};
\node at (9.5,0.5) {6};
\node at (10.5,0.5) {3};
\node at (11.5,0.5) {2};
\node at (12.5,0.5) {7};
\node at (13.5,0.5) {2};
\node at (14.5,0.5) {6};

\footnotesize
\node at (0.5,1.4) {1};
\node at (1.5,1.4) {2};
\node at (2.5,1.4) {3};
\node at (3.5,1.4) {4};
\node at (4.5,1.4) {5};
\node at (5.5,1.4) {6};
\node at (6.5,1.4) {7};
\node at (7.5,1.4) {8};
\node at (8.5,1.4) {9};
\node at (9.5,1.4) {10};
\node at (10.5,1.4) {11};
\node at (11.5,1.4) {12};
\node at (12.5,1.4) {13};
\node at (13.5,1.4) {14};
\node at (14.5,1.4) {15};
\end{tikzpicture}
</script>

Using this representation,
the parent of \\(\\texttt{tree}[k]\\)
is \\(\\texttt{tree}[\\lfloor k/2 \\rfloor]\\),
and its children are \\(\\texttt{tree}[2k]\\)
and \\(\\texttt{tree}[2k+1]\\).
Note that this implies that the position of a node
is even if it is a left child and odd if it is a right child.

The following function
calculates the value of \\(\\texttt{sum}_q(a,b)\\):

```rust
# let tree = vec![39, 22, 17, 13, 9, 9, 8, 5, 8, 6, 3, 2, 7, 2, 6];
# let a = 2;
# let b = 7;
# let n = 8;
# println!("tree => {:?}", tree);
# println!("a =>{a}");
# println!("b =>{b}");
# println!("n =>{n}");
# println!("sum_q({},{}) = {}", a,b,sum(tree, 2, 7, 8));
fn sum(tree: Vec<usize>, mut a: usize, mut b: usize, n:usize) -> usize{
   a += n; 
   b += n;
   let mut s = 0;
   while a<=b {
       if a%2 == 1 { s += tree[a as usize -1]; a+=1;}
       if b%2 == 0 { s += tree[b as usize -1]; b-=1;}
       a/=2;
       b/=2;
   }

   s
}
```
The function maintains a range
that is initially \\([a+n,b+n]\\).
Then, at each step, the range is moved
one level higher in the tree,
and before that, the values of the nodes that do not
belong to the higher range are added to the sum.

The following function increases the array value
at position $k$ by $x$:
```rust
# let mut tree = vec![39, 22, 17, 13, 9, 9, 8, 5, 8, 6, 3, 2, 7, 2, 6];
# let k = 5;
# let x = 4;
# let n = 8;
# println!("before => {:?}", tree);
# println!("k =>{k}");
# println!("x =>{x}");
# println!("n =>{n}");
add(&mut tree, k, x, n);
# println!("after => {:?}", tree);
fn add(tree: &mut Vec<usize>, mut k: usize, mut x: usize, n:usize){
    k += n;
    tree[k-1] += x;
    k/=2;
    while k>= 1 {
        tree[k-1] = tree[2*k-1]+tree[2*k];
        k/=2;
    }
}
```
First the function updates the value
at the bottom level of the tree.
After this, the function updates the values of all
internal tree nodes, until it reaches
the top node of the tree.

Both the above functions work
in $O(\log n)$ time, because a segment tree
of $n$ elements consists of $O(\log n)$ levels,
and the functions move one level higher
in the tree at each step.

___

[^1] The bottom-up-implementation in this chapter corresponds to that in [62]. Similar structures were used in late 1970's to solve geometric problems [9].

[^2] In fact, using _two_ binary indexed trees it is possible to support minimum queries [16], but this is more complicated than to use a segment tree.


