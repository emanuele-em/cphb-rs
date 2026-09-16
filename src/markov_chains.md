# Markov chains

A **Markov chain**
is a random process
that consists of states and transitions between them.
For each state, we know the probabilities
for moving to other states.
A Markov chain can be represented as a graph
whose nodes are states and edges are transitions.

As an example, consider a problem
where we are in floor 1 in an $n$ floor building.
At each step, we randomly walk either one floor
up or one floor down, except that we always
walk one floor up from floor 1 and one floor down
from floor $n$.
What is the probability of being in floor $m$
after $k$ steps?

In this problem, each floor of the building
corresponds to a state in a Markov chain.
For example, if $n=5$, the graph is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,0) {$1$};
\node[draw, circle] (2) at (2,0) {$2$};
\node[draw, circle] (3) at (4,0) {$3$};
\node[draw, circle] (4) at (6,0) {$4$};
\node[draw, circle] (5) at (8,0) {$5$};

\path[draw,thick,->] (1) edge [bend left=40] node[font=\small,label=$1$] {} (2);
\path[draw,thick,->] (2) edge [bend left=40] node[font=\small,label=$1/2$] {} (3);
\path[draw,thick,->] (3) edge [bend left=40] node[font=\small,label=$1/2$] {} (4);
\path[draw,thick,->] (4) edge [bend left=40] node[font=\small,label=$1/2$] {} (5);

\path[draw,thick,->] (5) edge [bend left=40] node[font=\small,label=below:$1$] {} (4);
\path[draw,thick,->] (4) edge [bend left=40] node[font=\small,label=below:$1/2$] {} (3);
\path[draw,thick,->] (3) edge [bend left=40] node[font=\small,label=below:$1/2$] {} (2);
\path[draw,thick,->] (2) edge [bend left=40] node[font=\small,label=below:$1/2$] {} (1);

%\path[draw,thick,->] (1) edge [bend left=40] node[font=\small,label=below:$1$] {} (2);
\end{tikzpicture}
</script>

The probability distribution
of a Markov chain is a vector
$[p_1,p_2,\ldots,p_n]$, where $p_k$ is the
probability that the current state is $k$.
The formula $p_1+p_2+\cdots+p_n=1$ always holds.

In the above scenario, the initial distribution is
$[1,0,0,0,0]$, because we always begin in floor 1.
The next distribution is $[0,1,0,0,0]$,
because we can only move from floor 1 to floor 2.
After this, we can either move one floor up
or one floor down, so the next distribution is
$[1/2,0,1/2,0,0]$, and so on.

An efficient way to simulate the walk in
a Markov chain is to use dynamic programming.
The idea is to maintain the probability distribution,
and at each step go through all possibilities
how we can move.
Using this method, we can simulate
a walk of $m$ steps in $O(n^2 m)$ time.

The transitions of a Markov chain can also be
represented as a matrix that updates the
probability distribution.
In the above scenario, the matrix is

\\[
\\begin{bmatrix}
  0 & 1/2 & 0 & 0 & 0 \\\\
  1 & 0 & 1/2 & 0 & 0 \\\\
  0 & 1/2 & 0 & 1/2 & 0 \\\\
  0 & 0 & 1/2 & 0 & 1 \\\\
  0 & 0 & 0 & 1/2 & 0 \\\\
 \\end{bmatrix}.
\\]

When we multiply a probability distribution by this matrix,
we get the new distribution after moving one step.
For example, we can move from the distribution
$[1,0,0,0,0]$ to the distribution
$[0,1,0,0,0]$ as follows:

\\[
\\begin{bmatrix}
  0 & 1/2 & 0 & 0 & 0 \\\\
  1 & 0 & 1/2 & 0 & 0 \\\\
  0 & 1/2 & 0 & 1/2 & 0 \\\\
  0 & 0 & 1/2 & 0 & 1 \\\\
  0 & 0 & 0 & 1/2 & 0 \\\\
 \\end{bmatrix}
 \\begin{bmatrix}
  1 \\\\
  0 \\\\
  0 \\\\
  0 \\\\
  0 \\\\
 \\end{bmatrix} =
 \\begin{bmatrix}
  0 \\\\
  1 \\\\
  0 \\\\
  0 \\\\
  0 \\\\
 \\end{bmatrix}.
\\]

By calculating matrix powers efficiently,
we can calculate the distribution after $m$ steps
in $O(n^3 \log m)$ time.
