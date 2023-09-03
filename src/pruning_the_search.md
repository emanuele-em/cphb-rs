# Pruning the search

We can often optimize backtracking
by pruning the search tree.
The idea is to add _intelligence_ to the algorithm
so that it will notice as soon as possible
if a partial solution cannot be extended
to a complete solution.
Such optimizations can have a tremendous
effect on the efficiency of the search.

Let us consider the problem
of calculating the number of paths
in an $n \times n$ grid from the upper-left corner
to the lower-right corner such that the
path visits each square exactly once.
For example, in a $7 \times 7$ grid,
there are 111712 such paths.
One of the paths is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=.55]
  \begin{scope}
    \draw (0, 0) grid (7, 7);
    \draw[thick,->] (0.5,6.5) -- (0.5,4.5) -- (2.5,4.5) --
          (2.5,3.5) -- (0.5,3.5) -- (0.5,0.5) --
          (3.5,0.5) -- (3.5,1.5) -- (1.5,1.5) --
          (1.5,2.5) -- (4.5,2.5) -- (4.5,0.5) --
          (5.5,0.5) -- (5.5,3.5) -- (3.5,3.5) --
          (3.5,5.5) -- (1.5,5.5) -- (1.5,6.5) --
          (4.5,6.5) -- (4.5,4.5) -- (5.5,4.5) --
          (5.5,6.5) -- (6.5,6.5) -- (6.5,0.5);
  \end{scope}
\end{tikzpicture}
</script>

We focus on the $7 \times 7$ case,
because its level of difficulty is appropriate to our needs.
We begin with a straightforward backtracking algorithm,
and then optimize it step by step using observations
of how the search can be pruned.
After each optimization, we measure the running time
of the algorithm and the number of recursive calls,
so that we clearly see the effect of each
optimization on the efficiency of the search.

## Basic algorithm

The first version of the algorithm does not contain
any optimizations. We simply use backtracking to generate
all possible paths from the upper-left corner to
the lower-right corner and count the number of such paths.

- running time: 483 seconds
- number of recursive calls: 76 billion

## Optimization 1

In any solution, we first move one step
down or right.
There are always two paths that 
are symmetric
about the diagonal of the grid
after the first step.
For example, the following paths are symmetric:

<script type="text/tikz">
\begin{tikzpicture}[scale=.55]
  \begin{scope}
    \draw (0, 0) grid (7, 7);
    \draw[thick,->] (0.5,6.5) -- (0.5,4.5) -- (2.5,4.5) --
          (2.5,3.5) -- (0.5,3.5) -- (0.5,0.5) --
          (3.5,0.5) -- (3.5,1.5) -- (1.5,1.5) --
          (1.5,2.5) -- (4.5,2.5) -- (4.5,0.5) --
          (5.5,0.5) -- (5.5,3.5) -- (3.5,3.5) --
          (3.5,5.5) -- (1.5,5.5) -- (1.5,6.5) --
          (4.5,6.5) -- (4.5,4.5) -- (5.5,4.5) --
          (5.5,6.5) -- (6.5,6.5) -- (6.5,0.5);
  \end{scope}

  \begin{scope}[xshift=-90, yshift=7cm, yscale=1,xscale=-1,rotate=-90]
    \draw (0, 0) grid (7, 7);
    \draw[thick,->] (0.5,6.5) -- (0.5,4.5) -- (2.5,4.5) --
          (2.5,3.5) -- (0.5,3.5) -- (0.5,0.5) --
          (3.5,0.5) -- (3.5,1.5) -- (1.5,1.5) --
          (1.5,2.5) -- (4.5,2.5) -- (4.5,0.5) --
          (5.5,0.5) -- (5.5,3.5) -- (3.5,3.5) --
          (3.5,5.5) -- (1.5,5.5) -- (1.5,6.5) --
          (4.5,6.5) -- (4.5,4.5) -- (5.5,4.5) --
          (5.5,6.5) -- (6.5,6.5) -- (6.5,0.5);
  \end{scope}
\end{tikzpicture}
</script>

Hence, we can decide that we always first
move one step down (or right),
and finally multiply the number of solutions by two
- running time: 244 seconds
- number of recursive calls: 38 billion

## Optimization 2

If the path reaches the lower-right square
before it has visited all other squares of the grid,
it is clear that
it will not be possible to complete the solution.
An example of this is the following path:

<script type="text/tikz">
\begin{tikzpicture}[scale=.55]
  \begin{scope}
    \draw (0, 0) grid (7, 7);
    \draw[thick,->] (0.5,6.5) -- (0.5,4.5) -- (2.5,4.5) --
          (2.5,3.5) -- (0.5,3.5) -- (0.5,0.5) --
          (3.5,0.5) -- (3.5,1.5) -- (1.5,1.5) --
          (1.5,2.5) -- (4.5,2.5) -- (4.5,0.5) --
          (6.5,0.5);
  \end{scope}
\end{tikzpicture}
</script>

Using this observation, we can terminate the search
immediately if we reach the lower-right square too early.
- running time: 119 seconds
- number of recursive calls: 20 billion

## Optimization 3
If the path touches a wall
and can turn either left or right,
the grid splits into two parts
that contain unvisited squares.
For example, in the following situation,
the path can turn either left or right:

<script type="text/tikz">
\begin{tikzpicture}[scale=.55]
  \begin{scope}
    \draw (0, 0) grid (7, 7);
    \draw[thick,->] (0.5,6.5) -- (0.5,4.5) -- (2.5,4.5) --
          (2.5,3.5) -- (0.5,3.5) -- (0.5,0.5) --
          (3.5,0.5) -- (3.5,1.5) -- (1.5,1.5) --
          (1.5,2.5) -- (4.5,2.5) -- (4.5,0.5) --
          (5.5,0.5) -- (5.5,6.5);
  \end{scope}
\end{tikzpicture}
</script>

In this case, we cannot visit all squares anymore, so we can terminate the search.
This optimization is very useful:
- running time: 1.8 seconds
- number of recursive calls: 221 million

## Optimization 4
The idea of Optimization 3 can be generalized: if the path cannot continue
forward but can turn either left or right, the grid splits into two parts that both
contain unvisited squares. For example, consider the following path:

<script type="text/tikz">
\begin{tikzpicture}[scale=.55]
  \begin{scope}
    \draw (0, 0) grid (7, 7);
    \draw[thick,->] (0.5,6.5) -- (0.5,4.5) -- (2.5,4.5) --
          (2.5,3.5) -- (0.5,3.5) -- (0.5,0.5) --
          (3.5,0.5) -- (3.5,1.5) -- (1.5,1.5) --
          (1.5,2.5) -- (4.5,2.5) -- (4.5,0.5) --
          (5.5,0.5) -- (5.5,4.5) -- (3.5,4.5);
  \end{scope}
\end{tikzpicture}
</script>

It is clear that we cannot visit all squares anymore,
so we can terminate the search.
After this optimization, the search is
very efficient:

- running time: 0.6 seconds
- number of recursive calls: 69 million

Now is a good moment to stop optimizing
the algorithm and see what we have achieved.
The running time of the original algorithm
was 483 seconds,
and now after the optimizations,
the running time is only 0.6 seconds.
Thus, the algorithm became nearly 1000 times
faster after the optimizations.

This is a usual phenomenon in backtracking,
because the search tree is usually large
and even simple observations can effectively
prune the search.
Especially useful are optimizations that
occur during the first steps of the algorithm,
i.e., at the top of the search tree.
