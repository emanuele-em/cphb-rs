# De Bruijn sequences

A **De Bruijn sequence**
is a string that contains
every string of length $n$
exactly once as a substring, for a fixed
alphabet of $k$ characters.
The length of such a string is 
$k^n+n-1$ characters.
For example, when $n=3$ and $k=2$,
an example of a De Bruijn sequence is

$$
0001011100
$$

The substrings of this string are all
combinations of three bits:
000, 001, 010, 011, 100, 101, 110 and 111.

It turns out that each De Bruijn sequence
corresponds to an Eulerian path in a graph.
The idea is to construct a graph where
each node contains a string of $n-1$ characters
and each edge adds one character to the string.
The following graph corresponds to the above scenario:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.8]
\node[draw, circle] (00) at (-3,0) {00};
\node[draw, circle] (11) at (3,0) {11};
\node[draw, circle] (01) at (0,2) {01};
\node[draw, circle] (10) at (0,-2) {10};

\path[draw,thick,->] (00) edge [bend left=20] node[font=\small,label=1] {} (01);
\path[draw,thick,->] (01) edge [bend left=20] node[font=\small,label=1] {} (11);
\path[draw,thick,->] (11) edge [bend left=20] node[font=\small,label=below:0] {} (10);
\path[draw,thick,->] (10) edge [bend left=20] node[font=\small,label=below:0] {} (00);

\path[draw,thick,->] (01) edge [bend left=30] node[font=\small,label=right:0] {} (10);
\path[draw,thick,->] (10) edge [bend left=30] node[font=\small,label=left:1] {} (01);

\path[draw,thick,-] (00) edge [loop left] node[font=\small,label=below:0] {} (00);
\path[draw,thick,-] (11) edge [loop right] node[font=\small,label=below:1] {} (11);
\end{tikzpicture}
</script>

An Eulerian path in this graph corresponds to a string
that contains all strings of length $n$.
The string contains the characters of the starting node
and all characters of the edges.
The starting node has $n-1$ characters
and there are $k^n$ characters in the edges,
so the length of the string is $k^n+n-1$.
