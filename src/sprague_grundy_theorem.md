# Sprague–Grundy theorem

The **Sprague–Grundy theorem**[^1] generalizes the
strategy used in nim to all games that fulfil
the following requirements:
- There are two players who move alternately.
- The game consists of states, and the possible moves
in a state do not depend on whose turn it is.
- The game ends when a player cannot make a move.
- The game surely ends sooner or later.
- The players have complete information about
the states and allowed moves, and there is no randomness in the game.

The idea is to calculate for each game state
a Grundy number that corresponds to the number of
sticks in a nim heap.
When we know the Grundy numbers of all states,
we can play the game like the nim game.

## Grundy numbers

The **Grundy number** of a game state is
\\[
\\textrm{mex}(\\{g_1,g_2,\\ldots,g_n\\}),
\\]
where $g_1,g_2,\ldots,g_n$ are the Grundy numbers of the
states to which we can move,
and the mex function gives the smallest
nonnegative number that is not in the set.
For example, $\textrm{mex}(\\{0,1,3\\})=2$.
If there are no possible moves in a state,
its Grundy number is 0, because
$\textrm{mex}(\emptyset)=0$.

The mex function itself is a short scan: mark which values are present,
then return the first index that was never marked.

```rust
fn mex(values: &[usize]) -> usize {
    let mut seen = vec![false; values.len() + 1];
    for &v in values {
        if v < seen.len() { seen[v] = true; }
    }
    seen.iter().position(|&s| !s).unwrap()
}
# println!("mex({:?}) = {}", [0,1,3], mex(&[0,1,3]));
# println!("mex(empty) = {}", mex(&[]));
```

A set of $n$ values can never miss a number larger than $n$, so a table
of $n+1$ flags always contains the answer and `position` always finds one.


For example, in the state graph

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,0) {\phantom{0}};
\node[draw, circle] (2) at (2,0) {\phantom{0}};
\node[draw, circle] (3) at (4,0) {\phantom{0}};
\node[draw, circle] (4) at (1,-2) {\phantom{0}};
\node[draw, circle] (5) at (3,-2) {\phantom{0}};
\node[draw, circle] (6) at (5,-2) {\phantom{0}};

\path[draw,thick,->,>=latex] (2) -- (1);
\path[draw,thick,->,>=latex] (3) -- (2);
\path[draw,thick,->,>=latex] (5) -- (4);
\path[draw,thick,->,>=latex] (6) -- (5);
\path[draw,thick,->,>=latex] (4) -- (1);
\path[draw,thick,->,>=latex] (4) -- (2);
\path[draw,thick,->,>=latex] (5) -- (2);
\path[draw,thick,->,>=latex] (6) -- (2);
\end{tikzpicture}
</script>

the Grundy numbers are as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\node[draw, circle] (1) at (0,0) {0};
\node[draw, circle] (2) at (2,0) {1};
\node[draw, circle] (3) at (4,0) {0};
\node[draw, circle] (4) at (1,-2) {2};
\node[draw, circle] (5) at (3,-2) {0};
\node[draw, circle] (6) at (5,-2) {2};

\path[draw,thick,->,>=latex] (2) -- (1);
\path[draw,thick,->,>=latex] (3) -- (2);
\path[draw,thick,->,>=latex] (5) -- (4);
\path[draw,thick,->,>=latex] (6) -- (5);
\path[draw,thick,->,>=latex] (4) -- (1);
\path[draw,thick,->,>=latex] (4) -- (2);
\path[draw,thick,->,>=latex] (5) -- (2);
\path[draw,thick,->,>=latex] (6) -- (2);
\end{tikzpicture}
</script>

The Grundy number of a losing state is 0,
and the Grundy number of a winning state is
a positive number.

The Grundy number of a state corresponds to
the number of sticks in a nim heap.
If the Grundy number is 0, we can only move to
states whose Grundy numbers are positive,
and if the Grundy number is $x>0$, we can move
to states whose Grundy numbers include all numbers
$0,1,\ldots,x-1$.

As an example, consider a game where
the players move a figure in a maze.
Each square in the maze is either floor or wall.
On each turn, the player has to move
the figure some number
of steps left or up.
The winner of the game is the player who
makes the last move.

The following picture shows a possible initial state
of the game, where @ denotes the figure and *
denotes a square where it can move.

<script type="text/tikz">
\begin{tikzpicture}[scale=.65]
  \begin{scope}
    \fill [color=black] (0, 1) rectangle (1, 2);
    \fill [color=black] (0, 3) rectangle (1, 4);
    \fill [color=black] (2, 2) rectangle (3, 3);
    \fill [color=black] (2, 4) rectangle (3, 5);
    \fill [color=black] (4, 3) rectangle (5, 4);

    \draw (0, 0) grid (5, 5);
    
    \node at (4.5,0.5) {@};
    \node at (3.5,0.5) {*};
    \node at (2.5,0.5) {*};
    \node at (1.5,0.5) {*};
    \node at (0.5,0.5) {*};
    \node at (4.5,1.5) {*};
    \node at (4.5,2.5) {*};
    
  \end{scope}
\end{tikzpicture}
</script>

The states of the game are all floor squares
of the maze.
In the above maze, the Grundy numbers
are as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=.65]
  \begin{scope}
    \fill [color=black] (0, 1) rectangle (1, 2);
    \fill [color=black] (0, 3) rectangle (1, 4);
    \fill [color=black] (2, 2) rectangle (3, 3);
    \fill [color=black] (2, 4) rectangle (3, 5);
    \fill [color=black] (4, 3) rectangle (5, 4);

    \draw (0, 0) grid (5, 5);
    
    \node at (0.5,4.5) {0};
    \node at (1.5,4.5) {1};
    \node at (2.5,4.5) {};
    \node at (3.5,4.5) {0};
    \node at (4.5,4.5) {1};

    \node at (0.5,3.5) {};
    \node at (1.5,3.5) {0};
    \node at (2.5,3.5) {1};
    \node at (3.5,3.5) {2};
    \node at (4.5,3.5) {};

    \node at (0.5,2.5) {0};
    \node at (1.5,2.5) {2};
    \node at (2.5,2.5) {};
    \node at (3.5,2.5) {1};
    \node at (4.5,2.5) {0};

    \node at (0.5,1.5) {};
    \node at (1.5,1.5) {3};
    \node at (2.5,1.5) {0};
    \node at (3.5,1.5) {4};
    \node at (4.5,1.5) {1};

    \node at (0.5,0.5) {0};
    \node at (1.5,0.5) {4};
    \node at (2.5,0.5) {1};
    \node at (3.5,0.5) {3};
    \node at (4.5,0.5) {2};
  \end{scope}
\end{tikzpicture}
</script>

Thus, each state of the maze game
corresponds to a heap in the nim game.
For example, the Grundy number for
the lower-right square is 2,
so it is a winning state.
We can reach a losing state and
win the game by moving
either four steps left or
two steps up.

Note that unlike in the original nim game,
it may be possible to move to a state whose
Grundy number is larger than the Grundy number
of the current state.
However, the opponent can always choose a move
that cancels such a move, so it is not possible
to escape from a losing state.

## Subgames

Next we will assume that our game consists
of subgames, and on each turn, the player
first chooses a subgame and then a move in the subgame.
The game ends when it is not possible to make any move
in any subgame.

In this case, the Grundy number of a game
is the nim sum of the Grundy numbers of the subgames.
The game can be played like a nim game by calculating
all Grundy numbers for subgames and then their nim sum.

As an example, consider a game that consists
of three mazes.
In this game, on each turn, the player chooses one
of the mazes and then moves the figure in the maze.
Assume that the initial state of the game is as follows:



<script type="text/tikz">
\begin{tikzpicture}[scale=.55]
  \begin{scope}
    \fill [color=black] (0, 1) rectangle (1, 2);
    \fill [color=black] (0, 3) rectangle (1, 4);
    \fill [color=black] (2, 2) rectangle (3, 3);
    \fill [color=black] (2, 4) rectangle (3, 5);
    \fill [color=black] (4, 3) rectangle (5, 4);

    \draw (0, 0) grid (5, 5);

    \node at (4.5,0.5) {@};

    \end{scope}
\end{tikzpicture}
</script>

<script type="text/tikz">
\begin{tikzpicture}[scale=.55]
  \begin{scope}
    \fill [color=black] (1, 1) rectangle (2, 3);
    \fill [color=black] (2, 3) rectangle (3, 4);
    \fill [color=black] (4, 4) rectangle (5, 5);

    \draw (0, 0) grid (5, 5);
    
    \node at (4.5,0.5) {@};

  \end{scope}
\end{tikzpicture}
</script>

<script type="text/tikz">
\begin{tikzpicture}[scale=.55]
  \begin{scope}
    \fill [color=black] (1, 1) rectangle (4, 4);

    \draw (0, 0) grid (5, 5);
    
    \node at (4.5,0.5) {@};
  \end{scope}
\end{tikzpicture}
</script>



The Grundy numbers for the mazes are as follows:



<script type="text/tikz">
\begin{tikzpicture}[scale=.55]
  \begin{scope}
    \fill [color=black] (0, 1) rectangle (1, 2);
    \fill [color=black] (0, 3) rectangle (1, 4);
    \fill [color=black] (2, 2) rectangle (3, 3);
    \fill [color=black] (2, 4) rectangle (3, 5);
    \fill [color=black] (4, 3) rectangle (5, 4);

    \draw (0, 0) grid (5, 5);

    \node at (0.5,4.5) {0};
    \node at (1.5,4.5) {1};
    \node at (2.5,4.5) {};
    \node at (3.5,4.5) {0};
    \node at (4.5,4.5) {1};

    \node at (0.5,3.5) {};
    \node at (1.5,3.5) {0};
    \node at (2.5,3.5) {1};
    \node at (3.5,3.5) {2};
    \node at (4.5,3.5) {};

    \node at (0.5,2.5) {0};
    \node at (1.5,2.5) {2};
    \node at (2.5,2.5) {};
    \node at (3.5,2.5) {1};
    \node at (4.5,2.5) {0};

    \node at (0.5,1.5) {};
    \node at (1.5,1.5) {3};
    \node at (2.5,1.5) {0};
    \node at (3.5,1.5) {4};
    \node at (4.5,1.5) {1};

    \node at (0.5,0.5) {0};
    \node at (1.5,0.5) {4};
    \node at (2.5,0.5) {1};
    \node at (3.5,0.5) {3};
    \node at (4.5,0.5) {2};
    \end{scope}
\end{tikzpicture}
</script>

<script type="text/tikz">
\begin{tikzpicture}[scale=.55]
  \begin{scope}
    \fill [color=black] (1, 1) rectangle (2, 3);
    \fill [color=black] (2, 3) rectangle (3, 4);
    \fill [color=black] (4, 4) rectangle (5, 5);

    \draw (0, 0) grid (5, 5);

    \node at (0.5,4.5) {0};
    \node at (1.5,4.5) {1};
    \node at (2.5,4.5) {2};
    \node at (3.5,4.5) {3};
    \node at (4.5,4.5) {};

    \node at (0.5,3.5) {1};
    \node at (1.5,3.5) {0};
    \node at (2.5,3.5) {};
    \node at (3.5,3.5) {0};
    \node at (4.5,3.5) {1};

    \node at (0.5,2.5) {2};
    \node at (1.5,2.5) {};
    \node at (2.5,2.5) {0};
    \node at (3.5,2.5) {1};
    \node at (4.5,2.5) {2};

    \node at (0.5,1.5) {3};
    \node at (1.5,1.5) {};
    \node at (2.5,1.5) {1};
    \node at (3.5,1.5) {2};
    \node at (4.5,1.5) {0};

    \node at (0.5,0.5) {4};
    \node at (1.5,0.5) {0};
    \node at (2.5,0.5) {2};
    \node at (3.5,0.5) {5};
    \node at (4.5,0.5) {3};
  \end{scope}
\end{tikzpicture}
</script>

<script type="text/tikz">
\begin{tikzpicture}[scale=.55]
  \begin{scope}
    \fill [color=black] (1, 1) rectangle (4, 4);

    \draw (0, 0) grid (5, 5);

    \node at (0.5,4.5) {0};
    \node at (1.5,4.5) {1};
    \node at (2.5,4.5) {2};
    \node at (3.5,4.5) {3};
    \node at (4.5,4.5) {4};

    \node at (0.5,3.5) {1};
    \node at (1.5,3.5) {};
    \node at (2.5,3.5) {};
    \node at (3.5,3.5) {};
    \node at (4.5,3.5) {0};

    \node at (0.5,2.5) {2};
    \node at (1.5,2.5) {};
    \node at (2.5,2.5) {};
    \node at (3.5,2.5) {};
    \node at (4.5,2.5) {1};

    \node at (0.5,1.5) {3};
    \node at (1.5,1.5) {};
    \node at (2.5,1.5) {};
    \node at (3.5,1.5) {};
    \node at (4.5,1.5) {2};

    \node at (0.5,0.5) {4};
    \node at (1.5,0.5) {0};
    \node at (2.5,0.5) {1};
    \node at (3.5,0.5) {2};
    \node at (4.5,0.5) {3};
  \end{scope}
\end{tikzpicture}
</script>



In the initial state, the nim sum of the Grundy numbers
is $2 \oplus 3 \oplus 3 = 2$, so
the first player can win the game.
One optimal move is to move two steps up
in the first maze, which produces the nim sum
$0 \oplus 3 \oplus 3 = 0$.

## Grundy's game

Sometimes a move in a game divides the game
into subgames that are independent of each other.
In this case, the Grundy number of the game is

\\[
\\textrm{mex}(\\{g_1, g_2, \\ldots, g_n \\}),
\\]
where $n$ is the number of possible moves and
\\[
g_k = a_{k,1} \\oplus a_{k,2} \\oplus \\ldots \\oplus a_{k,m},
\\]
where move $k$ generates subgames with
Grundy numbers $a_{k,1},a_{k,2},\ldots,a_{k,m}$.

An example of such a game is **Grundy's game**.
Initially, there is a single heap that contains $n$ sticks.
On each turn, the player chooses a heap and divides
it into two nonempty heaps such that the heaps
are of different size.
The player who makes the last move wins the game.

Let $f(n)$ be the Grundy number of a heap
that contains $n$ sticks.
The Grundy number can be calculated by going
through all ways to divide the heap into
two heaps.
For example, when $n=8$, the possibilities
are $1+7$, $2+6$ and $3+5$, so
\\[
f(8)=\\textrm{mex}(\\{f(1) \\oplus f(7), f(2) \\oplus f(6), f(3) \\oplus f(5)\\}).
\\]

In this game, the value of $f(n)$ is based on the values
of $f(1),\ldots,f(n-1)$.
The base cases are $f(1)=f(2)=0$,
because it is not possible to divide the heaps
of 1 and 2 sticks.
The first Grundy numbers are:
\\[
\\begin{array}{lcl}
f(1) & = & 0 \\\\
f(2) & = & 0 \\\\
f(3) & = & 1 \\\\
f(4) & = & 0 \\\\
f(5) & = & 2 \\\\
f(6) & = & 1 \\\\
f(7) & = & 0 \\\\
f(8) & = & 2 \\\\
\\end{array}
\\]
The Grundy number for $n=8$ is 2,
so it is possible to win the game.
The winning move is to create heaps
$1+7$, because $f(1) \oplus f(7) = 0$.

___

[^1]: The theorem was
independently discovered by R. Sprague [69] and P. M. Grundy [34].
