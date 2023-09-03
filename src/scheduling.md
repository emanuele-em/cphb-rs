# Scheduling

Many scheduling problems can be solved
using greedy algorithms.
A classic problem is as follows:
Given $n$ events with their starting and ending
times, find a schedule
that includes as many events as possible.
It is not possible to select an event partially.
For example, consider the following events:

| event | starting time | ending time |
|:------|:--------------|:------------|
|A|1|3|
|B|2|5|
|C|3|9|
|D|6|8|

In this case the maximum number of events is two.
For example, we can select events $B$ and $D$
as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=.4]
  \begin{scope}
    \draw (2, 0) rectangle (6, -1);
    \draw[fill=lightgray] (4, -1.5) rectangle (10, -2.5);
    \draw (6, -3) rectangle (18, -4);
    \draw[fill=lightgray] (12, -4.5) rectangle (16, -5.5);
    \node at (2.5,-0.5) {A};
    \node at (4.5,-2) {B};
    \node at (6.5,-3.5) {C};
    \node at (12.5,-5) {D};
  \end{scope}
\end{tikzpicture}
</script>

It is possible to invent several greedy algorithms for the problem, but which
of them works in every case?

## Algorithm 1

The first idea is to select as _short_
events as possible.
In the example case this algorithm
selects the following events:

<script type="text/tikz">
\begin{tikzpicture}[scale=.4]
  \begin{scope}
    \draw[fill=lightgray] (2, 0) rectangle (6, -1);
    \draw (4, -1.5) rectangle (10, -2.5);
    \draw (6, -3) rectangle (18, -4);
    \draw[fill=lightgray] (12, -4.5) rectangle (16, -5.5);
    \node at (2.5,-0.5) {A};
    \node at (4.5,-2) {B};
    \node at (6.5,-3.5) {C};
    \node at (12.5,-5) {D};
  \end{scope}
\end{tikzpicture}
</script>

However, selecting short events is not always
a correct strategy. For example, the algorithm fails
in the following case:

<script type="text/tikz">
\begin{tikzpicture}[scale=.4]
  \begin{scope}
    \draw (1, 0) rectangle (7, -1);
    \draw[fill=lightgray] (6, -1.5) rectangle (9, -2.5);
    \draw (8, -3) rectangle (14, -4);
  \end{scope}
\end{tikzpicture}
</script>
If we select the short event, we can only select one event.
However, it would be possible to select both long events.

## Algorithm 2

Another idea is to always select the next possible
event that _begins_ as _early_ as possible.
This algorithm selects the following events:

<script type="text/tikz">
\begin{tikzpicture}[scale=.4]
  \begin{scope}
    \draw[fill=lightgray] (2, 0) rectangle (6, -1);
    \draw (4, -1.5) rectangle (10, -2.5);
    \draw[fill=lightgray] (6, -3) rectangle (18, -4);
    \draw (12, -4.5) rectangle (16, -5.5);
    \node at (2.5,-0.5) {A};
    \node at (4.5,-2) {B};
    \node at (6.5,-3.5) {C};
    \node at (12.5,-5) {D};
  \end{scope}
\end{tikzpicture}
</script>

However, we can find a counterexample
also for this algorithm.
For example, in the following case,
the algorithm only selects one event:

<script type="text/tikz">
\begin{tikzpicture}[scale=.4]
  \begin{scope}
    \draw[fill=lightgray] (1, 0) rectangle (14, -1);
    \draw (3, -1.5) rectangle (7, -2.5);
    \draw (8, -3) rectangle (12, -4);
  \end{scope}
\end{tikzpicture}
</script>

If we select the first event, it is not possible
to select any other events.
However, it would be possible to select the
other two events.

## Algorithm 3

The third idea is to always select the next
possible event that _ends_ as _early_ as possible.
This algorithm selects the following events: 

<script type="text/tikz">
\begin{tikzpicture}[scale=.4]
  \begin{scope}
    \draw[fill=lightgray] (2, 0) rectangle (6, -1);
    \draw (4, -1.5) rectangle (10, -2.5);
    \draw (6, -3) rectangle (18, -4);
    \draw[fill=lightgray] (12, -4.5) rectangle (16, -5.5);
    \node at (2.5,-0.5) {A};
    \node at (4.5,-2) {B};
    \node at (6.5,-3.5) {C};
    \node at (12.5,-5) {D};
  \end{scope}
\end{tikzpicture}
</script>

It turns out that this algorithm
_always_ produces an optimal solution.
The reason for this is that it is always an optimal choice
to first select an event that ends
as early as possible.
After this, it is an optimal choice
to select the next event
using the same strategy, etc.,
until we cannot select any more events.
One way to argue that the algorithm works
is to consider
what happens if we first select an event
that ends later than the event that ends
as early as possible.
Now, we will have at most an equal number of
choices how we can select the next event.
Hence, selecting an event that ends later
can never yield a better solution,
and the greedy algorithm is correct.


