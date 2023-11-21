# Flows and cuts

In this chapter, we focus on the following
two problems:

- **Finding a maximum flow**:
What is the maximum amount of flow we can
send from a node to another node?
- **Finding a minimum cut**:
What is a minimum-weight set of edges
that separates two nodes of the graph?

The input for both these problems is a directed,
weighted graph that contains two special nodes:
the _source_ is a node with no incoming edges,
and the _sink_ is a node with no outgoing edges.

As an example, we will use the following graph
where node 1 is the source and node 6
is the sink:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,2) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (7,2) {6};
\node[draw, circle] (5) at (3,1) {4};
\node[draw, circle] (6) at (5,1) {5};
\path[draw,thick,->] (1) -- node[font=\small,label=5] {} (2);
\path[draw,thick,->] (2) -- node[font=\small,label=6] {} (3);
\path[draw,thick,->] (3) -- node[font=\small,label=5] {} (4);
\path[draw,thick,->] (1) -- node[font=\small,label=below:4] {} (5);
\path[draw,thick,->] (5) -- node[font=\small,label=below:1] {} (6);
\path[draw,thick,->] (6) -- node[font=\small,label=below:2] {} (4);
\path[draw,thick,<-] (2) -- node[font=\small,label=left:3] {} (5);
\path[draw,thick,->] (3) -- node[font=\small,label=left:8] {} (6);
\end{tikzpicture}
</script>

## Maximum Flow

In the **maximum flow** problem,
our task is to send as much flow as possible
from the source to the sink.
The weight of each edge is a capacity that
restricts the flow
that can go through the edge.
In each intermediate node,
the incoming and outgoing
flow has to be equal.

For example, the maximum size of a flow
in the example graph is 7.
The following picture shows how we can
route the flow:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,2) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (7,2) {6};
\node[draw, circle] (5) at (3,1) {4};
\node[draw, circle] (6) at (5,1) {5};
\path[draw,thick,->] (1) -- node[font=\small,label=3/5] {} (2);
\path[draw,thick,->] (2) -- node[font=\small,label=6/6] {} (3);
\path[draw,thick,->] (3) -- node[font=\small,label=5/5] {} (4);
\path[draw,thick,->] (1) -- node[font=\small,label=below:4/4] {} (5);
\path[draw,thick,->] (5) -- node[font=\small,label=below:1/1] {} (6);
\path[draw,thick,->] (6) -- node[font=\small,label=below:2/2] {} (4);
\path[draw,thick,<-] (2) -- node[font=\small,label=left:3/3] {} (5);
\path[draw,thick,->] (3) -- node[font=\small,label=left:1/8] {} (6);
\end{tikzpicture}
</script>

The notation $v/k$ means
that a flow of $v$ units is routed through
an edge whose capacity is $k$ units.
The size of the flow is $7$,
because the source sends $3+4$ units of flow
and the sink receives $5+2$ units of flow.
It is easy see that this flow is maximum,
because the total capacity of the edges
leading to the sink is $7$.

## Minimum Cut

In the **minimum cut** problem,
our task is to remove a set
of edges from the graph
such that there will be no path from the source
to the sink after the removal
and the total weight of the removed edges
is minimum.

The minimum size of a cut in the example graph is 7.
It suffices to remove the edges $2 \rightarrow 3$
and $4 \rightarrow 5$:

<script type="text/tikz">
\begin{center}
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (1,2) {1};
\node[draw, circle] (2) at (3,3) {2};
\node[draw, circle] (3) at (5,3) {3};
\node[draw, circle] (4) at (7,2) {6};
\node[draw, circle] (5) at (3,1) {4};
\node[draw, circle] (6) at (5,1) {5};
\path[draw,thick,->] (1) -- node[font=\small,label=5] {} (2);
\path[draw,thick,->] (2) -- node[font=\small,label=6] {} (3);
\path[draw,thick,->] (3) -- node[font=\small,label=5] {} (4);
\path[draw,thick,->] (1) -- node[font=\small,label=below:4] {} (5);
\path[draw,thick,->] (5) -- node[font=\small,label=below:1] {} (6);
\path[draw,thick,->] (6) -- node[font=\small,label=below:2] {} (4);
\path[draw,thick,<-] (2) -- node[font=\small,label=left:3] {} (5);
\path[draw,thick,->] (3) -- node[font=\small,label=left:8] {} (6);

\path[draw=red,thick,-,line width=2pt] (4-.3,3-.3) -- (4+.3,3+.3);
\path[draw=red,thick,-,line width=2pt] (4-.3,3+.3) -- (4+.3,3-.3);
\path[draw=red,thick,-,line width=2pt] (4-.3,1-.3) -- (4+.3,1+.3);
\path[draw=red,thick,-,line width=2pt] (4-.3,1+.3) -- (4+.3,1-.3);
\end{tikzpicture}
\end{center}
</script>

After removing the edges,
there will be no path from the source to the sink.
The size of the cut is $7$,
because the weights of the removed edges
are $6$ and $1$.
The cut is minimum, because there is no valid
way to remove edges from the graph such that
their total weight would be less than $7$.

It is not a coincidence that
the maximum size of a flow
and the minimum size of a cut
are the same in the above example.
It turns out that a maximum flow
and a minimum cut are
_always_ equally large,
so the concepts are two sides of the same coin.

Next we will discuss the Ford–Fulkerson
algorithm that can be used to find
the maximum flow and minimum cut of a graph.
The algorithm also helps us to understand
_why_ they are equally large.

