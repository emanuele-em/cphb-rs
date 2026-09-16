# Trie structure

A **trie** is a rooted tree that
maintains a set of strings.
Each string in the set is stored as
a chain of characters that starts at the root.
If two strings have a common prefix,
they also have a common chain in the tree.

For example, consider the following trie:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,20) {$\phantom{1}$};
\node[draw, circle] (2) at (-1.5,19) {$\phantom{1}$};
\node[draw, circle] (3) at (1.5,19) {$\phantom{1}$};
\node[draw, circle] (4) at (-1.5,17.5) {$\phantom{1}$};
\node[draw, circle] (5) at (-1.5,16) {$\phantom{1}$};
\node[draw, circle] (6) at (-2.5,14.5) {$\phantom{1}$};
\node[draw, circle] (7) at (-0.5,14.5) {$\phantom{1}$};
\node[draw, circle] (8) at (-2.5,13) {*};
\node[draw, circle] (9) at (-0.5,13) {*};
\node[draw, circle] (10) at (1.5,17.5) {$\phantom{1}$};
\node[draw, circle] (11) at (1.5,16) {*};
\node[draw, circle] (12) at (1.5,14.5) {$\phantom{1}$};
\node[draw, circle] (13) at (1.5,13) {*};

\path[draw,thick,->] (1) -- node[font=\small,label=\texttt{C}] {} (2);
\path[draw,thick,->] (1) -- node[font=\small,label=\texttt{T}] {} (3);
\path[draw,thick,->] (2) -- node[font=\small,label=left:\texttt{A}] {} (4);
\path[draw,thick,->] (4) -- node[font=\small,label=left:\texttt{N}] {} (5);
\path[draw,thick,->] (5) -- node[font=\small,label=left:\texttt{A}] {} (6);
\path[draw,thick,->] (5) -- node[font=\small,label=right:\texttt{D}] {} (7);
\path[draw,thick,->] (6) -- node[font=\small,label=left:\texttt{L}] {}(8);
\path[draw,thick,->] (7) -- node[font=\small,label=right:\texttt{Y}] {} (9);
\path[draw,thick,->] (3) -- node[font=\small,label=right:\texttt{H}] {} (10);
\path[draw,thick,->] (10) -- node[font=\small,label=right:\texttt{E}] {} (11);
\path[draw,thick,->] (11) -- node[font=\small,label=right:\texttt{R}] {} (12);
\path[draw,thick,->] (12) -- node[font=\small,label=right:\texttt{E}] {} (13);
\end{tikzpicture}
</script>

This trie corresponds to the set
$\\{\texttt{CANAL},\texttt{CANDY},\texttt{THE},\texttt{THERE}\\}$.
The character * in a node means that
a string in the set ends at the node.
Such a character is needed, because a string
may be a prefix of another string.
For example, in the above trie, `THE`
is a prefix of `THERE`.

We can check in $O(n)$ time whether a trie
contains a string of length $n$,
because we can follow the chain that starts at the root node.
We can also add a string of length $n$ to the trie
in $O(n)$ time by first following the chain
and then adding new nodes to the trie if necessary.

Using a trie, we can find
the longest prefix of a given string
such that the prefix belongs to the set.
Moreover, by storing additional information
in each node,
we can calculate the number of
strings that belong to the set and have a
given string as a prefix.

A trie can be stored in an array
```rust
# const A: usize = 26;
// one row per node; 0 means "no child", so the root must be node 0
let mut trie: Vec<[usize; A]> = vec![[0; A]];
# // insert a word, creating nodes as needed
# let mut add = |trie: &mut Vec<[usize; A]>, word: &str| {
#     let mut node = 0usize;
#     for &c in word.as_bytes() {
#         let c = (c - b'a') as usize;
#         if trie[node][c] == 0 {
#             trie.push([0; A]);
#             let fresh = trie.len() - 1;
#             trie[node][c] = fresh;
#         }
#         node = trie[node][c];
#     }
# };
# add(&mut trie, "canal");
# add(&mut trie, "candy");
# add(&mut trie, "the");
# println!("{} nodes after inserting 3 words", trie.len());
```
where $A$ is the size of the alphabet. The vector grows as nodes are
added, so unlike the C++ array there is no maximum node count $N$ to
choose in advance.
The nodes of a trie are numbered
$0,1,2,\ldots$ so that the number of the root is 0,
and $\texttt{trie}[s][c]$ is the next node in the chain
when we move from node $s$ using character $c$.
