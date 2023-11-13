# Eulerian paths

An **Eulerian path**[^1] is a path
that goes exactly once through each edge of the graph.
For example, the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (5);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);
\end{tikzpicture}
</script>

has an Eulerian path from node 2 to node 5:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (5);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);

\path[draw=red,thick,->,line width=2pt] (2) -- node[font=\small,label={[red]north:1.}] {} (1);
\path[draw=red,thick,->,line width=2pt] (1) -- node[font=\small,label={[red]left:2.}] {} (4);
\path[draw=red,thick,->,line width=2pt] (4) -- node[font=\small,label={[red]south:3.}] {} (5);
\path[draw=red,thick,->,line width=2pt] (5) -- node[font=\small,label={[red]left:4.}] {} (2);
\path[draw=red,thick,->,line width=2pt] (2) -- node[font=\small,label={[red]north:5.}] {} (3);
\path[draw=red,thick,->,line width=2pt] (3) -- node[font=\small,label={[red]south:6.}] {} (5);
\end{tikzpicture}
</script>

An **Eulerian circuit**
is an Eulerian path that starts and ends
at the same node.
For example, the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (5);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (2) -- (4);
\end{tikzpicture}
</script>

has an Eulerian circuit that starts and ends at node 1:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (5);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (2) -- (4);

\path[draw=red,thick,->,line width=2pt] (1) -- node[font=\small,label={[red]left:1.}] {} (4);
\path[draw=red,thick,->,line width=2pt] (4) -- node[font=\small,label={[red]south:2.}] {} (2);
\path[draw=red,thick,->,line width=2pt] (2) -- node[font=\small,label={[red]right:3.}] {} (5);
\path[draw=red,thick,->,line width=2pt] (5) -- node[font=\small,label={[red]south:4.}] {} (3);
\path[draw=red,thick,->,line width=2pt] (3) -- node[font=\small,label={[red]north:5.}] {} (2);
\path[draw=red,thick,->,line width=2pt] (2) -- node[font=\small,label={[red]north:6.}] {} (1);
\end{tikzpicture}
</script>

## Existence

The existence of Eulerian paths and circuits
depends on the degrees of the nodes.
First, an undirected graph has an Eulerian path 
exactly when all the edges
belong to the same connected component and

- the degree of each node is even \emph{or}
- the degree of exactly two nodes is odd,
and the degree of all other nodes is even.

In the first case, each Eulerian path is also an Eulerian circuit.
In the second case, the odd-degree nodes are the starting
and ending nodes of an Eulerian path which is not an Eulerian circuit.

For example, in the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (5);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);
\end{tikzpicture}
</script>

nodes 1, 3 and 4 have a degree of 2,
and nodes 2 and 5 have a degree of 3.
Exactly two nodes have an odd degree,
so there is an Eulerian path between nodes 2 and 5,
but the graph does not contain an Eulerian circuit.

In a directed graph,
we focus on indegrees and outdegrees
of the nodes.
A directed graph contains an Eulerian path
exactly when all the edges belong to the same
connected component and

- in each node, the indegree equals the outdegree, _or_
- in one node, the indegree is one larger than the outdegree,
in another node, the outdegree is one larger than the indegree,
and in all other nodes, the indegree equals the outdegree.

In the first case, each Eulerian path
is also an Eulerian circuit,
and in the second case, the graph contains an Eulerian path
that begins at the node whose outdegree is larger
and ends at the node whose indegree is larger.

For example, in the graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};

\path[draw,thick,->,>=latex] (1) -- (2);
\path[draw,thick,->,>=latex] (2) -- (3);
\path[draw,thick,->,>=latex] (4) -- (1);
\path[draw,thick,->,>=latex] (3) -- (5);
\path[draw,thick,->,>=latex] (2) -- (5);
\path[draw,thick,->,>=latex] (5) -- (4);
\end{tikzpicture}
</script>

nodes 1, 3 and 4 have both indegree 1 and outdegree 1,
node 2 has indegree 1 and outdegree 2,
and node 5 has indegree 2 and outdegree 1.
Hence, the graph contains an Eulerian path
from node 2 to node 5:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,5) {1};
\node[draw, circle] (2) at (3,5) {2};
\node[draw, circle] (3) at (5,4) {3};
\node[draw, circle] (4) at (1,3) {4};
\node[draw, circle] (5) at (3,3) {5};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (1) -- (4);
\path[draw,thick,-] (3) -- (5);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (4) -- (5);

\path[draw=red,thick,->,line width=2pt] (2) -- node[font=\small,label={[red]north:1.}] {} (3);
\path[draw=red,thick,->,line width=2pt] (3) -- node[font=\small,label={[red]south:2.}] {} (5);
\path[draw=red,thick,->,line width=2pt] (5) -- node[font=\small,label={[red]south:3.}] {} (4);
\path[draw=red,thick,->,line width=2pt] (4) -- node[font=\small,label={[red]left:4.}] {} (1);
\path[draw=red,thick,->,line width=2pt] (1) -- node[font=\small,label={[red]north:5.}] {} (2);
\path[draw=red,thick,->,line width=2pt] (2) -- node[font=\small,label={[red]left:6.}] {} (5);
\end{tikzpicture}
</script>

## Hierholzer's algorithm

**Hierholzer's algorithm**[^2] is an efficient
method for constructing
an Eulerian circuit.
The algorithm consists of several rounds,
each of which adds new edges to the circuit.
Of course, we assume that the graph contains
an Eulerian circuit; otherwise Hierholzer's
algorithm cannot find it.

First, the algorithm constructs a circuit that contains
some (not necessarily all) of the edges of the graph.
After this, the algorithm extends the circuit
step by step by adding subcircuits to it.
The process continues until all edges have been added
to the circuit.

The algorithm extends the circuit by always finding
a node $x$ that belongs to the circuit but has
an outgoing edge that is not included in the circuit.
The algorithm constructs a new path from node $x$
that only contains edges that are not yet in the circuit.
Sooner or later,
the path will return to node $x$,
which creates a subcircuit.

If the graph only contains an Eulerian path,
we can still use Hierholzer's algorithm
to find it by adding an extra edge to the graph
and removing the edge after the circuit
has been constructed.
For example, in an undirected graph,
we add the extra edge between the two
odd-degree nodes.

Next we will see how Hierholzer's algorithm
constructs an Eulerian circuit for an undirected graph.

## Example

Let us consider the following graph:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (3,5) {1};
\node[draw, circle] (2) at (1,3) {2};
\node[draw, circle] (3) at (3,3) {3};
\node[draw, circle] (4) at (5,3) {4};
\node[draw, circle] (5) at (1,1) {5};
\node[draw, circle] (6) at (3,1) {6};
\node[draw, circle] (7) at (5,1) {7};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (2) -- (6);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (4) -- (7);
\path[draw,thick,-] (5) -- (6);
\path[draw,thick,-] (6) -- (7);
\end{tikzpicture}
</script>

Suppose that the algorithm first creates a circuit
that begins at node 1.
A possible circuit is
$1 \rightarrow 2 \rightarrow 3 \rightarrow 1$:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (3,5) {1};
\node[draw, circle] (2) at (1,3) {2};
\node[draw, circle] (3) at (3,3) {3};
\node[draw, circle] (4) at (5,3) {4};
\node[draw, circle] (5) at (1,1) {5};
\node[draw, circle] (6) at (3,1) {6};
\node[draw, circle] (7) at (5,1) {7};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (2) -- (6);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (4) -- (7);
\path[draw,thick,-] (5) -- (6);
\path[draw,thick,-] (6) -- (7);

\path[draw=red,thick,->,line width=2pt] (1) -- node[font=\small,label={[red]north:1.}] {} (2);
\path[draw=red,thick,->,line width=2pt] (2) -- node[font=\small,label={[red]north:2.}] {} (3);
\path[draw=red,thick,->,line width=2pt] (3) -- node[font=\small,label={[red]east:3.}] {} (1);
\end{tikzpicture}
</script>

After this, the algorithm adds
the subcircuit
$2 \rightarrow 5 \rightarrow 6 \rightarrow 2$
to the circuit:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (3,5) {1};
\node[draw, circle] (2) at (1,3) {2};
\node[draw, circle] (3) at (3,3) {3};
\node[draw, circle] (4) at (5,3) {4};
\node[draw, circle] (5) at (1,1) {5};
\node[draw, circle] (6) at (3,1) {6};
\node[draw, circle] (7) at (5,1) {7};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (2) -- (6);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (4) -- (7);
\path[draw,thick,-] (5) -- (6);
\path[draw,thick,-] (6) -- (7);

\path[draw=red,thick,->,line width=2pt] (1) -- node[font=\small,label={[red]north:1.}] {} (2);
\path[draw=red,thick,->,line width=2pt] (2) -- node[font=\small,label={[red]west:2.}] {} (5);
\path[draw=red,thick,->,line width=2pt] (5) -- node[font=\small,label={[red]south:3.}] {} (6);
\path[draw=red,thick,->,line width=2pt] (6) -- node[font=\small,label={[red]north:4.}] {} (2);
\path[draw=red,thick,->,line width=2pt] (2) -- node[font=\small,label={[red]north:5.}] {} (3);
\path[draw=red,thick,->,line width=2pt] (3) -- node[font=\small,label={[red]east:6.}] {} (1);
\end{tikzpicture}
</script>

Finally, the algorithm adds the subcircuit
$6 \rightarrow 3 \rightarrow 4 \rightarrow 7 \rightarrow 6$
to the circuit:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (3,5) {1};
\node[draw, circle] (2) at (1,3) {2};
\node[draw, circle] (3) at (3,3) {3};
\node[draw, circle] (4) at (5,3) {4};
\node[draw, circle] (5) at (1,1) {5};
\node[draw, circle] (6) at (3,1) {6};
\node[draw, circle] (7) at (5,1) {7};

\path[draw,thick,-] (1) -- (2);
\path[draw,thick,-] (1) -- (3);
\path[draw,thick,-] (2) -- (3);
\path[draw,thick,-] (2) -- (5);
\path[draw,thick,-] (2) -- (6);
\path[draw,thick,-] (3) -- (4);
\path[draw,thick,-] (3) -- (6);
\path[draw,thick,-] (4) -- (7);
\path[draw,thick,-] (5) -- (6);
\path[draw,thick,-] (6) -- (7);

\path[draw=red,thick,->,line width=2pt] (1) -- node[font=\small,label={[red]north:1.}] {} (2);
\path[draw=red,thick,->,line width=2pt] (2) -- node[font=\small,label={[red]west:2.}] {} (5);
\path[draw=red,thick,->,line width=2pt] (5) -- node[font=\small,label={[red]south:3.}] {} (6);
\path[draw=red,thick,->,line width=2pt] (6) -- node[font=\small,label={[red]east:4.}] {} (3);
\path[draw=red,thick,->,line width=2pt] (3) -- node[font=\small,label={[red]north:5.}] {} (4);
\path[draw=red,thick,->,line width=2pt] (4) -- node[font=\small,label={[red]east:6.}] {} (7);
\path[draw=red,thick,->,line width=2pt] (7) -- node[font=\small,label={[red]south:7.}] {} (6);
\path[draw=red,thick,->,line width=2pt] (6) -- node[font=\small,label={[red]right:8.}] {} (2);
\path[draw=red,thick,->,line width=2pt] (2) -- node[font=\small,label={[red]north:9.}] {} (3);
\path[draw=red,thick,->,line width=2pt] (3) -- node[font=\small,label={[red]east:10.}] {} (1);
\end{tikzpicture}
</script>

Now all edges are included in the circuit,
so we have successfully constructed an Eulerian circuit.

___

[^1] L. Euler studied such paths in 1736 when he solved the famous Königsberg bridge problem.  This was the birth of graph theory.
[^2] The algorithm was published in 1873 after Hierholzer's death [35].
