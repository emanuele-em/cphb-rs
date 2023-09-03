# Tasks and deadlines

Let us now consider a problem where
we are given $n$ tasks with durations and deadlines
and our task is to choose an order to perform the tasks.
For each task, we earn $d-x$ points
where $d$ is the task's deadline
and $x$ is the moment when we finish the task.
What is the largest possible total score
we can obtain?

For example, suppose that the tasks are as follows:

| task | duration | deadline |
|:-----|:---------|:---------|
|A|4|2|
|B|3|5|
|C|2|7|
|D|4|5|

In this case, an optimal schedule for the tasks is as follows:


<script type="text/tikz">
\begin{tikzpicture}[scale=.4]
  \begin{scope}
    \draw (0, 0) rectangle (4, -1);
    \draw (4, 0) rectangle (10, -1);
    \draw (10, 0) rectangle (18, -1);
    \draw (18, 0) rectangle (26, -1);
    \node at (0.5,-0.5) {C};
    \node at (4.5,-0.5) {B};
    \node at (10.5,-0.5) {A};
    \node at (18.5,-0.5) {D};
    \draw (0,1.5) -- (26,1.5);
    \foreach \i in {0,2,...,26}
    {
        \draw (\i,1.25) -- (\i,1.75);
    }
    \footnotesize
    \node at (0,2.5) {0};
    \node at (10,2.5) {5};
    \node at (20,2.5) {10};
  \end{scope}
\end{tikzpicture}
</script>

In this solution, $C$ yields 5 points,
$B$ yields 0 points, $A$ yields $-7$ points
and $D$ yields $-8$ points,
so the total score is $-10$.

Surprisingly, the optimal solution to the problem
does not depend on the deadlines at all,
but a correct greedy strategy is to simply
perform the tasks _sorted by their durations_
in increasing order.
The reason for this is that if we ever perform
two tasks one after another such that the first task
takes longer than the second task,
we can obtain a better solution if we swap the tasks.
For example, consider the following schedule:

<script type="text/tikz">
\begin{tikzpicture}[scale=.4]
  \begin{scope}
    \draw (0, 0) rectangle (8, -1);
    \draw (8, 0) rectangle (12, -1);
    \node at (0.5,-0.5) {X};
    \node at (8.5,-0.5) {Y};
\draw (7.75,-1.5) -- (0.25,-1.5);
\draw (11.75,-1.5) -- (8.25,-1.5);
\footnotesize
\node at (4,-2.5) {a};
\node at (10,-2.5) {b};
  \end{scope}
\end{tikzpicture}
</script>

Here $a>b$, so we should swap the tasks:

<script type="text/tikz">
\begin{tikzpicture}[scale=.4]
  \begin{scope}
    \draw (0, 0) rectangle (4, -1);
    \draw (4, 0) rectangle (12, -1);
    \node at (0.5,-0.5) {$Y$};
    \node at (4.5,-0.5) {$X$};

\draw [decoration={brace}, decorate, line width=0.3mm] (3.75,-1.5) -- (0.25,-1.5);
\draw [decoration={brace}, decorate, line width=0.3mm] (11.75,-1.5) -- (4.25,-1.5);

\footnotesize
\node at (2,-2.5) {$b$};
\node at (8,-2.5) {$a$};

  \end{scope}
\end{tikzpicture}
</script>

Now $X$ gives $b$ points less and $Y$ gives $a$ points more,
so the total score increases by $a-b > 0$.
In an optimal solution,
for any two consecutive tasks,
it must hold that the shorter task comes
before the longer task.
Thus, the tasks must be performed
sorted by their durations.
