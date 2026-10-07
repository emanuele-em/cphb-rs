# Game states

Let us consider a game where there is initially
a heap of $n$ sticks.
Players $A$ and $B$ move alternately,
and player $A$ begins.
On each move, the player has to remove
1, 2 or 3 sticks from the heap,
and the player who removes the last stick wins the game.

For example, if $n=10$, the game may proceed as follows:
- Player $A$ removes 2 sticks (8 sticks left).
- Player $B$ removes 3 sticks (5 sticks left).
- Player $A$ removes 1 stick (4 sticks left).
- Player $B$ removes 2 sticks (2 sticks left).
- Player $A$ removes 2 sticks and wins.

This game consists of states $0,1,2,\ldots,n$,
where the number of the state corresponds to
the number of sticks left.

## Winning and losing states

A **winning state** is a state where
the player will win the game if they
play optimally,
and a **losing state** is a state
where the player will lose the game if the
opponent plays optimally.
It turns out that we can classify all states
of a game so that each state is either
a winning state or a losing state.

In the above game, state 0 is clearly a
losing state, because the player cannot make
any moves.
States 1, 2 and 3 are winning states,
because we can remove 1, 2 or 3 sticks
and win the game.
State 4, in turn, is a losing state,
because any move leads to a state that
is a winning state for the opponent.

More generally, if there is a move that leads
from the current state to a losing state,
the current state is a winning state,
and otherwise the current state is a losing state.
Using this observation, we can classify all states
of a game starting with losing states where
there are no possible moves.

The states $0 \ldots 15$ of the above game
can be classified as follows
($W$ denotes a winning state and $L$ denotes a losing state):

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (16,1);

\node at (0.5,0.5) {$L$};
\node at (1.5,0.5) {$W$};
\node at (2.5,0.5) {$W$};
\node at (3.5,0.5) {$W$};
\node at (4.5,0.5) {$L$};
\node at (5.5,0.5) {$W$};
\node at (6.5,0.5) {$W$};
\node at (7.5,0.5) {$W$};
\node at (8.5,0.5) {$L$};
\node at (9.5,0.5) {$W$};
\node at (10.5,0.5) {$W$};
\node at (11.5,0.5) {$W$};
\node at (12.5,0.5) {$L$};
\node at (13.5,0.5) {$W$};
\node at (14.5,0.5) {$W$};
\node at (15.5,0.5) {$W$};

\footnotesize
\node at (0.5,1.4) {$0$};
\node at (1.5,1.4) {$1$};
\node at (2.5,1.4) {$2$};
\node at (3.5,1.4) {$3$};
\node at (4.5,1.4) {$4$};
\node at (5.5,1.4) {$5$};
\node at (6.5,1.4) {$6$};
\node at (7.5,1.4) {$7$};
\node at (8.5,1.4) {$8$};
\node at (9.5,1.4) {$9$};
\node at (10.5,1.4) {$10$};
\node at (11.5,1.4) {$11$};
\node at (12.5,1.4) {$12$};
\node at (13.5,1.4) {$13$};
\node at (14.5,1.4) {$14$};
\node at (15.5,1.4) {$15$};
\end{tikzpicture}
</script>

It is easy to analyze this game:
a state $k$ is a losing state if $k$ is
divisible by 4, and otherwise it
is a winning state.
An optimal way to play the game is
to always choose a move after which
the number of sticks in the heap
is divisible by 4.
Finally, there are no sticks left and
the opponent has lost.

Of course, this strategy requires that
the number of sticks is _not_ divisible by 4
when it is our move.
If it is, there is nothing we can do,
and the opponent will win the game if
they play optimally.

## State graph

Let us now consider another stick game,
where in each state $k$, it is allowed to remove
any number $x$ of sticks such that $x$
is smaller than $k$ and divides $k$.
For example, in state 8 we may remove
1, 2 or 4 sticks, but in state 7 the only
allowed move is to remove 1 stick.

The following picture shows the states
$1 \ldots 9$ of the game as a **state graph**,
whose nodes are the states and edges are the moves between them:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,0) {$1$};
\node[draw, circle] (2) at (2,0) {$2$};
\node[draw, circle] (3) at (3.5,-1) {$3$};
\node[draw, circle] (4) at (1.5,-2) {$4$};
\node[draw, circle] (5) at (3,-2.75) {$5$};
\node[draw, circle] (6) at (2.5,-4.5) {$6$};
\node[draw, circle] (7) at (0.5,-3.25) {$7$};
\node[draw, circle] (8) at (-1,-4) {$8$};
\node[draw, circle] (9) at (1,-5.5) {$9$};

\path[draw,thick,->,>=latex] (2) -- (1);
\path[draw,thick,->,>=latex] (3) edge [bend right=20] (2);
\path[draw,thick,->,>=latex] (4) edge [bend left=20] (2);
\path[draw,thick,->,>=latex] (4) edge [bend left=20] (3);
\path[draw,thick,->,>=latex] (5) edge [bend right=20] (4);
\path[draw,thick,->,>=latex] (6) edge [bend left=20] (5);
\path[draw,thick,->,>=latex] (6) edge [bend left=20] (4);
\path[draw,thick,->,>=latex] (6) edge [bend right=40] (3);
\path[draw,thick,->,>=latex] (7) edge [bend right=20] (6);
\path[draw,thick,->,>=latex] (8) edge [bend right=20] (7);
\path[draw,thick,->,>=latex] (8) edge [bend right=20] (6);
\path[draw,thick,->,>=latex] (8) edge [bend left=20] (4);
\path[draw,thick,->,>=latex] (9) edge [bend left=20] (8);
\path[draw,thick,->,>=latex] (9) edge [bend right=20] (6);
\end{tikzpicture}
</script>

The final state in this game is always state 1,
which is a losing state, because there are no
valid moves.
The classification of states $1 \ldots 9$
is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (1,0) grid (10,1);

\node at (1.5,0.5) {$L$};
\node at (2.5,0.5) {$W$};
\node at (3.5,0.5) {$L$};
\node at (4.5,0.5) {$W$};
\node at (5.5,0.5) {$L$};
\node at (6.5,0.5) {$W$};
\node at (7.5,0.5) {$L$};
\node at (8.5,0.5) {$W$};
\node at (9.5,0.5) {$L$};

\footnotesize
\node at (1.5,1.4) {$1$};
\node at (2.5,1.4) {$2$};
\node at (3.5,1.4) {$3$};
\node at (4.5,1.4) {$4$};
\node at (5.5,1.4) {$5$};
\node at (6.5,1.4) {$6$};
\node at (7.5,1.4) {$7$};
\node at (8.5,1.4) {$8$};
\node at (9.5,1.4) {$9$};
\end{tikzpicture}
</script>

Surprisingly, in this game,
all even-numbered states are winning states,
and all odd-numbered states are losing states.
