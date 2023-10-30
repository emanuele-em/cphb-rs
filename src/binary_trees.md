# Binary trees

A **binary tree** is a rooted tree
where each node has a left and right subtree.
It is possible that a subtree of a node is empty.
Thus, every node in a binary tree has
zero, one or two children.

For example, the following tree is a binary tree:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,0) {1};
\node[draw, circle] (2) at (-1.5,-1.5) {2};
\node[draw, circle] (3) at (1.5,-1.5) {3};
\node[draw, circle] (4) at (-3,-3) {4};
\node[draw, circle] (5) at (0,-3) {5};
\node[draw, circle] (6) at (-1.5,-4.5) {6};
\node[draw, circle] (7) at (3,-3) {7};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (2) -- (4);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (5) -- (6);
\path[draw,thick,-] (3) -- (7);
\end{tikzpicture}
</script>

The nodes of a binary tree have three natural
orderings that correspond to different ways to 
recursively traverse the tree:

- **pre-order**: first process the root,
then traverse the left subtree, then traverse the right subtree
- **in-order**: first traverse the left subtree,
then process the root, then traverse the right subtree
- **post-order**: first traverse the left subtree,
then traverse the right subtree, then process the root

For the above tree, the nodes in
pre-order are
\\([1,2,4,5,6,3,7]\\),
in in-order \\([4,2,6,5,1,3,7]\\)
and in post-order \\([4,6,5,2,7,3,1]\\).

If we know the pre-order and in-order
of a tree, we can reconstruct the exact structure of the tree.
For example, the above tree is the only possible tree
with pre-order \\([1,2,4,5,6,3,7]\\) and
in-order \\([4,2,6,5,1,3,7]\\).
In a similar way, the post-order and in-order
also determine the structure of a tree.

However, the situation is different if we only know
the pre-order and post-order of a tree.
In this case, there may be more than one tree
that match the orderings.
For example, in both of the trees

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,0) {1};
\node[draw, circle] (2) at (-1.5,-1.5) {2};
\path[draw,thick,-] (1) -- (2);

\node[draw, circle] (1b) at (0+4,0) {1};
\node[draw, circle] (2b) at (1.5+4,-1.5) {2};
\path[draw,thick,-] (1b) -- (2b);
\end{tikzpicture}
</script>

the pre-order is \\([1, 2]\\) and the post-order is \\([2, 1]\\), but the structures of the trees are different


