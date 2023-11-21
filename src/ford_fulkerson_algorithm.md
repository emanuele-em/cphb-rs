# Ford–Fulkerson algorithm

The **Ford–Fulkerson algorithm** [25] finds
the maximum flow in a graph.
The algorithm begins with an empty flow,
and at each step finds a path from the source
to the sink that generates more flow.
Finally, when the algorithm cannot increase the flow
anymore, the maximum flow has been found.

The algorithm uses a special representation
of the graph where each original edge has a reverse
edge in another direction.
The weight of each edge indicates how much more flow
we could route through it.
At the beginning of the algorithm, the weight of each original edge
equals the capacity of the edge
and the weight of each reverse edge is zero.

The new representation for the example graph is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9,label distance=-2mm]
\node[draw, circle] (1) at (1,1.3) {1};
\node[draw, circle] (2) at (3,2.6) {2};
\node[draw, circle] (3) at (5,2.6) {3};
\node[draw, circle] (4) at (7,1.3) {6};
\node[draw, circle] (5) at (3,0) {4};
\node[draw, circle] (6) at (5,0) {5};

\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=5] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=below:0] {} (1);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=6] {} (3);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=below:0] {} (2);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=5] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:0] {} (3);
\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=4] {} (5);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=below:0] {} (1);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=1] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=below:0] {} (5);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=2] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:0] {} (6);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=left:3] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=right:0] {} (5);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=right:8] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=left:0] {} (3);
\end{tikzpicture}
</script>

## Algorithm description

The Ford–Fulkerson algorithm consists of several
rounds.
On each round, the algorithm finds
a path from the source to the sink
such that each edge on the path has a positive weight.
If there is more than one possible path available,
we can choose any of them.

For example, suppose we choose the following path:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9,label distance=-2mm]
\node[draw, circle] (1) at (1,1.3) {1};
\node[draw, circle] (2) at (3,2.6) {2};
\node[draw, circle] (3) at (5,2.6) {3};
\node[draw, circle] (4) at (7,1.3) {6};
\node[draw, circle] (5) at (3,0) {4};
\node[draw, circle] (6) at (5,0) {5};

\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=5] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=below:0] {} (1);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=6] {} (3);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=below:0] {} (2);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=5] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:0] {} (3);
\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=4] {} (5);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=below:0] {} (1);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=1] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=below:0] {} (5);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=2] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:0] {} (6);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=left:3] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=right:0] {} (5);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=right:8] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=left:0] {} (3);

\path[draw=red,thick,->,line width=2pt] (1) edge [bend left=10] (2);
\path[draw=red,thick,->,line width=2pt] (2) edge [bend left=10] (3);
\path[draw=red,thick,->,line width=2pt] (3) edge [bend left=10] (6);
\path[draw=red,thick,->,line width=2pt] (6) edge [bend left=10] (4);
\end{tikzpicture}
</script>

After choosing the path, the flow increases by $x$ units,
where $x$ is the smallest edge weight on the path.
In addition, the weight of each edge on the path
decreases by $x$ and the weight of each reverse edge
increases by $x$.

In the above path, the weights of the
edges are 5, 6, 8 and 2.
The smallest weight is 2,
so the flow increases by 2
and the new graph is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9,label distance=-2mm]
\node[draw, circle] (1) at (1,1.3) {1};
\node[draw, circle] (2) at (3,2.6) {2};
\node[draw, circle] (3) at (5,2.6) {3};
\node[draw, circle] (4) at (7,1.3) {6};
\node[draw, circle] (5) at (3,0) {4};
\node[draw, circle] (6) at (5,0) {5};

\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=3] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=below:2] {} (1);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=4] {} (3);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=below:2] {} (2);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=5] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:0] {} (3);
\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=4] {} (5);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=below:0] {} (1);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=1] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=below:0] {} (5);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=0] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:2] {} (6);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=left:3] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=right:0] {} (5);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=right:6] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=left:2] {} (3);
\end{tikzpicture}
</script>

The idea is that increasing the flow decreases the amount of
flow that can go through the edges in the future.
On the other hand, it is possible to cancel
flow later using the reverse edges of the graph
if it turns out that
it would be beneficial to route the flow in another way.

The algorithm increases the flow as long as
there is a path from the source
to the sink through positive-weight edges.
In the present example, our next path can be as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9,label distance=-2mm]
\node[draw, circle] (1) at (1,1.3) {1};
\node[draw, circle] (2) at (3,2.6) {2};
\node[draw, circle] (3) at (5,2.6) {3};
\node[draw, circle] (4) at (7,1.3) {6};
\node[draw, circle] (5) at (3,0) {4};
\node[draw, circle] (6) at (5,0) {5};

\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=3] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=below:2] {} (1);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=4] {} (3);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=below:2] {} (2);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=5] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:0] {} (3);
\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=4] {} (5);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=below:0] {} (1);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=1] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=below:0] {} (5);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=0] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:2] {} (6);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=left:3] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=right:0] {} (5);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=right:6] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=left:2] {} (3);

\path[draw=red,thick,->,line width=2pt] (1) edge [bend left=10] (5);
\path[draw=red,thick,->,line width=2pt] (5) edge [bend left=10] (2);
\path[draw=red,thick,->,line width=2pt] (2) edge [bend left=10] (3);
\path[draw=red,thick,->,line width=2pt] (3) edge [bend left=10] (4);
\end{tikzpicture}
</script>

The minimum edge weight on this path is 3,
so the path increases the flow by 3,
and the total flow after processing the path is 5.

The new graph will be as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9,label distance=-2mm]
\node[draw, circle] (1) at (1,1.3) {1};
\node[draw, circle] (2) at (3,2.6) {2};
\node[draw, circle] (3) at (5,2.6) {3};
\node[draw, circle] (4) at (7,1.3) {6};
\node[draw, circle] (5) at (3,0) {4};
\node[draw, circle] (6) at (5,0) {5};

\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=3] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=below:2] {} (1);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=1] {} (3);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=below:5] {} (2);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=2] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:3] {} (3);
\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=1] {} (5);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=below:3] {} (1);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=1] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=below:0] {} (5);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=0] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:2] {} (6);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=left:0] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=right:3] {} (5);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=right:6] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=left:2] {} (3);
\end{tikzpicture}
</script>

We still need two more rounds before reaching the maximum flow.
For example, we can choose the paths
$1 \rightarrow 2 \rightarrow 3 \rightarrow 6$ and
$1 \rightarrow 4 \rightarrow 5 \rightarrow 3 \rightarrow 6$.
Both paths increase the flow by 1,
and the final graph is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9,label distance=-2mm]
\node[draw, circle] (1) at (1,1.3) {1};
\node[draw, circle] (2) at (3,2.6) {2};
\node[draw, circle] (3) at (5,2.6) {3};
\node[draw, circle] (4) at (7,1.3) {6};
\node[draw, circle] (5) at (3,0) {4};
\node[draw, circle] (6) at (5,0) {5};

\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=2] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=below:3] {} (1);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=0] {} (3);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=below:6] {} (2);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=0] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:5] {} (3);
\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=0] {} (5);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=below:4] {} (1);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=0] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=below:1] {} (5);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=0] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:2] {} (6);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=left:0] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=right:3] {} (5);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=right:7] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=left:1] {} (3);
\end{tikzpicture}
</script>

It is not possible to increase the flow anymore,
because there is no path from the source
to the sink with positive edge weights.
Hence, the algorithm terminates and the maximum flow is 7.

## Finding paths

The Ford–Fulkerson algorithm does not specify
how we should choose the paths that increase the flow.
In any case, the algorithm will terminate sooner or later
and correctly find the maximum flow.
However, the efficiency of the algorithm depends on
the way the paths are chosen.

A simple way to find paths is to use depth-first search.
Usually, this works well, but in the worst case,
each path only increases the flow by 1
and the algorithm is slow.
Fortunately, we can avoid this situation
by using one of the following techniques:

The **Edmonds–Karp algorithm** [18]
chooses each path so that the number of edges
on the path is as small as possible.
This can be done by using breadth-first search
instead of depth-first search for finding paths.
It can be proven that this guarantees that
the flow increases quickly, and the time complexity
of the algorithm is $O(m^2 n)$.

The **scaling algorithm** [2] uses depth-first
search to find paths where each edge weight is
at least a threshold value.
Initially, the threshold value is
some large number, for example the sum of all
edge weights of the graph.
Always when a path cannot be found,
the threshold value is divided by 2.
The time complexity of the algorithm is $O(m^2 \log c)$,
where $c$ is the initial threshold value.

In practice, the scaling algorithm is easier to implement,
because depth-first search can be used for finding paths.
Both algorithms are efficient enough for problems
that typically appear in programming contests.

## Minimum Cuts

It turns out that once the Ford–Fulkerson algorithm
has found a maximum flow,
it has also determined a minimum cut.
Let $A$ be the set of nodes
that can be reached from the source
using positive-weight edges.
In the example graph, $A$ contains nodes 1, 2 and 4:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9,label distance=-2mm]
\node[draw, circle,fill=lightgray] (1) at (1,1.3) {1};
\node[draw, circle,fill=lightgray] (2) at (3,2.6) {2};
\node[draw, circle] (3) at (5,2.6) {3};
\node[draw, circle] (4) at (7,1.3) {6};
\node[draw, circle,fill=lightgray] (5) at (3,0) {4};
\node[draw, circle] (6) at (5,0) {5};

\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=2] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=below:3] {} (1);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=0] {} (3);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=below:6] {} (2);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=0] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:5] {} (3);
\path[draw,thick,->] (1) edge [bend left=10] node[font=\small,label=0] {} (5);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=below:4] {} (1);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=0] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=below:1] {} (5);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=0] {} (4);
\path[draw,thick,->] (4) edge [bend left=10] node[font=\small,label=below:2] {} (6);
\path[draw,thick,->] (5) edge [bend left=10] node[font=\small,label=left:0] {} (2);
\path[draw,thick,->] (2) edge [bend left=10] node[font=\small,label=right:3] {} (5);
\path[draw,thick,->] (3) edge [bend left=10] node[font=\small,label=right:7] {} (6);
\path[draw,thick,->] (6) edge [bend left=10] node[font=\small,label=left:1] {} (3);
\end{tikzpicture}
</script>

Now the minimum cut consists of the edges of the original graph
that start at some node in $A$, end at some node outside $A$,
and whose capacity is fully
used in the maximum flow.
In the above graph, such edges are
$2 \rightarrow 3$ and $4 \rightarrow 5$,
that correspond to the minimum cut $6+1=7$.

Why is the flow produced by the algorithm maximum
and why is the cut minimum?
The reason is that a graph cannot
contain a flow whose size is larger
than the weight of any cut of the graph.
Hence, always when a flow and a cut are equally large,
they are a maximum flow and a minimum cut.

Let us consider any cut of the graph
such that the source belongs to $A$,
the sink belongs to $B$
and there are some edges between the sets:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\draw[dashed] (-2,0) circle (1.5);
\draw[dashed] (2,0) circle (1.5);

\node at (-2,-1) {A};
\node at (2,-1) {B};

\node[draw, circle] (1) at (-1,0.5) {};
\node[draw, circle] (2) at (-1,0) {};
\node[draw, circle] (3) at (-1,-0.5) {};
\node[draw, circle] (4) at (1,0.5) {};
\node[draw, circle] (5) at (1,0) {};
\node[draw, circle] (6) at (1,-0.5) {};

\path[draw,thick,->] (1) -- (4);
\path[draw,thick,->] (5) -- (2);
\path[draw,thick,->] (3) -- (6);

\end{tikzpicture}
</script>

The size of the cut is the sum of the edges
that go from $A$ to $B$.
This is an upper bound for the flow
in the graph, because the flow has to proceed
from $A$ to $B$.
Thus, the size of a maximum flow is smaller than or equal to
the size of any cut in the graph.

On the other hand, the Ford–Fulkerson algorithm
produces a flow whose size is _exactly_ as large
as the size of a cut in the graph.
Thus, the flow has to be a maximum flow
and the cut has to be a minimum cut.
