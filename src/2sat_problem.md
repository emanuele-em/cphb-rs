# 2SAT problem

Strong connectivity is also linked with the
**2SAT problem** [^1].
In this problem, we are given a logical formula
\\[
(a_1 \\lor b_1) \\land (a_2 \\lor b_2) \\land \\cdots \\land (a_m \\lor b_m),
\\]
where each $a_i$ and $b_i$ is either a logical variable
($x_1,x_2,\ldots,x_n$)
or a negation of a logical variable
($\lnot x_1, \lnot x_2, \ldots, \lnot x_n$).
The symbols "$\land$" and "$\lor$" denote
logical operators "and" and "or".
Our task is to assign each variable a value
so that the formula is true, or state
that this is not possible.

For example, the formula
\\[
L_1 = (x_2 \\lor \\lnot x_1) \\land
      (\\lnot x_1 \\lor \\lnot x_2) \\land
      (x_1 \\lor x_3) \\land
      (\\lnot x_2 \\lor \\lnot x_3) \\land
      (x_1 \\lor x_4)
\\]
is true when the variables are assigned as follows:

\\[
\\begin{cases}
x_1 = \\textrm{false} \\\\
x_2 = \\textrm{false} \\\\
x_3 = \\textrm{true} \\\\
x_4 = \\textrm{true} \\\\
\\end{cases}
\\]

However, the formula
\\[
L_2 = (x_1 \\lor x_2) \\land
      (x_1 \\lor \\lnot x_2) \\land
      (\\lnot x_1 \\lor x_3) \land
      (\\lnot x_1 \\lor \\lnot x_3)
\\]
is always false, regardless of how we
assign the values.
The reason for this is that we cannot
choose a value for $x_1$
without creating a contradiction.
If $x_1$ is false, both $x_2$ and $\lnot x_2$
should be true which is impossible,
and if $x_1$ is true, both $x_3$ and $\lnot x_3$
should be true which is also impossible.

The 2SAT problem can be represented as a graph
whose nodes correspond to
variables $x_i$ and negations $\lnot x_i$,
and edges determine the connections
between the variables.
Each pair $(a_i \lor b_i)$ generates two edges:
$\lnot a_i \to b_i$ and $\lnot b_i \to a_i$.
This means that if $a_i$ does not hold,
$b_i$ must hold, and vice versa.

The graph for the formula $L_1$ is:

<script type="text/tikz">
\begin{tikzpicture}[scale=1.0,minimum size=2pt]
\node[draw, circle, inner sep=1.3pt] (1) at (1,2) {\( \lnot x_3 \)};
\node[draw, circle] (2) at (3,2) {\( x_2 \)};
\node[draw, circle, inner sep=1.3pt] (3) at (1,0) {\( \lnot x_4 \)};
\node[draw, circle] (4) at (3,0) {\( x_1 \)};
\node[draw, circle, inner sep=1.3pt] (5) at (5,2) {\( \lnot x_1 \)};
\node[draw, circle] (6) at (7,2) {\( x_4 \)};
\node[draw, circle, inner sep=1.3pt] (7) at (5,0) {\( \lnot x_2 \)};
\node[draw, circle] (8) at (7,0) {\( x_3 \)};
 
\path[draw,thick,->] (1) -- (4);
\path[draw,thick,->] (4) -- (2);
\path[draw,thick,->] (2) -- (1);
\path[draw,thick,->] (3) -- (4);
\path[draw,thick,->] (2) -- (5);
\path[draw,thick,->] (4) -- (7);
\path[draw,thick,->] (5) -- (6);
\path[draw,thick,->] (5) -- (8);
\path[draw,thick,->] (8) -- (7);
\path[draw,thick,->] (7) -- (5);
\end{tikzpicture}
</script>

And the graph for the formula $L_2$ is:

<script type="text/tikz">
\begin{tikzpicture}[scale=1.0,minimum size=2pt]
\node[draw, circle] (1) at (1,2) {\(x_3\)};
\node[draw, circle] (2) at (3,2) {\(x_2\)};
\node[draw, circle, inner sep=1.3pt] (3) at (5,2) {\( \lnot x_2 \)};
\node[draw, circle, inner sep=1.3pt] (4) at (7,2) {\( \lnot x_3 \)};
\node[draw, circle, inner sep=1.3pt] (5) at (4,3.5) {\( \lnot x_1 \)};
\node[draw, circle] (6) at (4,0.5) {\( x_1 \)};

\path[draw,thick,->] (1) -- (5);
\path[draw,thick,->] (4) -- (5);
\path[draw,thick,->] (6) -- (1);
\path[draw,thick,->] (6) -- (4);
\path[draw,thick,->] (5) -- (2);
\path[draw,thick,->] (5) -- (3);
\path[draw,thick,->] (2) -- (6);
\path[draw,thick,->] (3) -- (6);
\end{tikzpicture}
</script>

The structure of the graph tells us whether
it is possible to assign the values
of the variables so
that the formula is true.
It turns out that this can be done
exactly when there are no nodes
$x_i$ and $\lnot x_i$ such that
both nodes belong to the
same strongly connected component.
If there are such nodes,
the graph contains
a path from $x_i$ to $\lnot x_i$
and also a path from $\lnot x_i$ to $x_i$,
so both $x_i$ and $\lnot x_i$ should be true
which is not possible.

In the graph of the formula $L_1$
there are no nodes $x_i$ and $\lnot x_i$
such that both nodes 
belong to the same strongly connected component,
so a solution exists.
In the graph of the formula $L_2$
all nodes belong to the same strongly connected component,
so a solution does not exist.

If a solution exists, the values for the variables
can be found by going through the nodes of the
component graph in a reverse topological sort order.
At each step, we process a component 
that does not contain edges that lead to an
unprocessed component.
If the variables in the component
have not been assigned values,
their values will be determined
according to the values in the component,
and if they already have values,
they remain unchanged.
The process continues until each variable
has been assigned a value.

The component graph for the formula $L_1$ is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=1.0]
\node[draw, circle] (1) at (0,0) {A};
\node[draw, circle] (2) at (2,0) {B};
\node[draw, circle] (3) at (4,0) {C};
\node[draw, circle] (4) at (6,0) {D};

\path[draw,thick,->] (1) -- (2);
\path[draw,thick,->] (2) -- (3);
\path[draw,thick,->] (3) -- (4);
\end{tikzpicture}
</script>

The components are
$A = \{\lnot x_4\}$,
$B = \{x_1, x_2, \lnot x_3\}$,
$C = \{\lnot x_1, \lnot x_2, x_3\}$ and
$D = \{x_4\}$.
When constructing the solution,
we first process the component $D$
where $x_4$ becomes true.
After this, we process the component $C$
where $x_1$ and $x_2$ become false
and $x_3$ becomes true.
All variables have been assigned values,
so the remaining components $A$ and $B$
do not change the variables.

Note that this method works, because the
graph has a special structure:
if there are paths from node $x_i$ to node $x_j$
and from node $x_j$ to node $\lnot x_j$,
then node $x_i$ never becomes true.
The reason for this is that there is also
a path from node $\lnot x_j$ to node $\lnot x_i$,
and both $x_i$ and $x_j$ become false.

A more difficult problem is the **3SAT problem**,
where each part of the formula is of the form
$(a_i \lor b_i \lor c_i)$.
This problem is NP-hard, so no efficient algorithm
for solving the problem is known.

___

[^1] The algorithm presented here was introduced in [4].  There is also another well-known linear-time algorithm [19] that is based on backtracking.
