# Data compression

A **binary code** assigns for each character
of a string a  **codeword** that consists of bits.
We can _compress_ the string using the binary code
by replacing each character by the
corresponding codeword.
For example, the following binary code
assigns codewords for characters $A-D$:

| character | codeword |
|----------:|---------:|
|A|00|
|B|01|
|C|10|
|D|11|

This is a **constant-length** code which means that the length of each codeword is
the same. For example, we can compress the string _AABACDACA_ as follows:

$$
000001001011001000
$$

Using this code, the length of the compressed
string is 18 bits.
However, we can compress the string better
if we use a **variable-length** code
where codewords may have different lengths.
Then we can give short codewords for
characters that appear often
and long codewords for characters
that appear rarely.
It turns out that an **optimal** code
for the above string is as follows:


| character | codeword |
|----------:|---------:|
|A|0|
|B|110|
|C|10|
|D|111|

An optimal code produces a compressed string that is as short as possible. In this
case, the compressed string using the optimal code is

$$
001100101110100
$$

so only 15 bits are needed instead of 18 bits.
Thus, thanks to a better code it was possible to
save 3 bits in the compressed string.

We require that no codeword
is a prefix of another codeword.
For example, it is not allowed that a code
would contain both codewords 10
and 1011.
The reason for this is that we want
to be able to generate the original string
from the compressed string.
If a codeword could be a prefix of another codeword,
this would not always be possible.

For example, the following code is _not_ valid:

| character | codeword |
|----------:|---------:|
|A|10|
|B|11|
|C|1011|
|D|111|

Using this code, it would not be possible to know if the compressed string 1011
corresponds to the string _AB_ or the string _C_.

## Huffman coding

**Huffman coding** is a greedy algorithm
that constructs an optimal code for
compressing a given string.
The algorithm builds a binary tree
based on the frequencies of the characters
in the string,
and each character's codeword can be read
by following a path from the root to
the corresponding node.
A move to the left corresponds to bit 0,
and a move to the right corresponds to bit 1.

Initially, each character of the string is
represented by a node whose weight is the
number of times the character occurs in the string.
Then at each step two nodes with minimum weights
are combined by creating
a new node whose weight is the sum of the weights
of the original nodes.
The process continues until all nodes have been combined.

Next we will see how Huffman coding creates
the optimal code for the string
_AABACDACA_.
Initially, there are four nodes that correspond
to the characters of the string:


<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,0) {5};
\node[draw, circle] (2) at (2,0) {1};
\node[draw, circle] (3) at (4,0) {2};
\node[draw, circle] (4) at (6,0) {1};

\node[color=blue] at (0,-0.75) {\texttt{A}};
\node[color=blue] at (2,-0.75) {\texttt{B}};
\node[color=blue] at (4,-0.75) {\texttt{C}};
\node[color=blue] at (6,-0.75) {\texttt{D}};

\end{tikzpicture}
</script>

The node that represents character A has weight 5 because character A appears 5
times in the string. The other weights have been calculated in the same way.
The first step is to combine the nodes that correspond to characters B and D,
both with weight 1. The result is:


<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,0) {5};
\node[draw, circle] (3) at (2,0) {2};
\node[draw, circle] (2) at (4,0) {1};
\node[draw, circle] (4) at (6,0) {1};
\node[draw, circle] (5) at (5,1) {2};

\node[color=blue] at (0,-0.75) {\texttt{A}};
\node[color=blue] at (2,-0.75) {\texttt{C}};
\node[color=blue] at (4,-0.75) {\texttt{B}};
\node[color=blue] at (6,-0.75) {\texttt{D}};

\node at (4.3,0.7) {0};
\node at (5.7,0.7) {1};

\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);
\end{tikzpicture}
</script>

After this, the nodes with weight 2 are combined:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,0) {5};
\node[draw, circle] (3) at (3,1) {2};
\node[draw, circle] (2) at (4,0) {1};
\node[draw, circle] (4) at (6,0) {1};
\node[draw, circle] (5) at (5,1) {2};
\node[draw, circle] (6) at (4,2) {4};

\node[color=blue] at (1,-0.75) {\texttt{A}};
\node[color=blue] at (3,1-0.75) {\texttt{C}};
\node[color=blue] at (4,-0.75) {\texttt{B}};
\node[color=blue] at (6,-0.75) {\texttt{D}};

\node at (4.3,0.7) {0};
\node at (5.7,0.7) {1};
\node at (3.3,1.7) {0};
\node at (4.7,1.7) {1};

\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (5) -- (6);
\end{tikzpicture}
</script>

Finally, the two remaining nodes are combined:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (2,2) {5};
\node[draw, circle] (3) at (3,1) {2};
\node[draw, circle] (2) at (4,0) {1};
\node[draw, circle] (4) at (6,0) {1};
\node[draw, circle] (5) at (5,1) {2};
\node[draw, circle] (6) at (4,2) {4};
\node[draw, circle] (7) at (3,3) {9};

\node[color=blue] at (2,2-0.75) {\texttt{A}};
\node[color=blue] at (3,1-0.75) {\texttt{C}};
\node[color=blue] at (4,-0.75) {\texttt{B}};
\node[color=blue] at (6,-0.75) {\texttt{D}};

\node at (4.3,0.7) {0};
\node at (5.7,0.7) {1};
\node at (3.3,1.7) {0};
\node at (4.7,1.7) {1};
\node at (2.3,2.7) {0};
\node at (3.7,2.7) {1};

\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (5) -- (6);
\path[draw,thick,-] (1) -- (7);
\path[draw,thick,-] (6) -- (7);
\end{tikzpicture}
</script>

Now all nodes are in the tree, so the code is ready.
The following codewords can be read from the tree:

| character | codeword |
|----------:|---------:|
|A|0|
|B|110|
|C|10|
|D|111|

___

[^1] D. A. Huffman discovered this method when solving a university course assignment and published the algorithm in 1952 [40].

