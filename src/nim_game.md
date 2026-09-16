# Nim game

The **nim game** is a simple game that
has an important role in game theory,
because many other games can be played using
the same strategy.
First, we focus on nim,
and then we generalize the strategy
to other games.

There are $n$ heaps in nim,
and each heap contains some number of sticks.
The players move alternately,
and on each turn, the player chooses
a heap that still contains sticks
and removes any number of sticks from it.
The winner is the player who removes the last stick.

The states in nim are of the form
$[x_1,x_2,\ldots,x_n]$,
where $x_k$ denotes the number of sticks in heap $k$.
For example, $[10,12,5]$ is a game where
there are three heaps with 10, 12 and 5 sticks.
The state $[0,0,\ldots,0]$ is a losing state,
because it is not possible to remove any sticks,
and this is always the final state.

## Analysis

It turns out that we can easily classify
any nim state by calculating
the **nim sum** $s = x_1 \oplus x_2 \oplus \cdots \oplus x_n$,
where $\oplus$ is the xor operation[^1].
The states whose nim sum is 0 are losing states,
and all other states are winning states.
For example, the nim sum of
$[10,12,5]$ is $10 \oplus 12 \oplus 5 = 3$,
so the state is a winning state.

But how is the nim sum related to the nim game?
We can explain this by looking at how the nim
sum changes when the nim state changes.

_Losing states:_
The final state $[0,0,\ldots,0]$ is a losing state,
and its nim sum is 0, as expected.
In other losing states, any move leads to
a winning state, because when a single value $x_k$ changes,
the nim sum also changes, so the nim sum
is different from 0 after the move.

_Winning states:_
We can move to a losing state if
there is any heap $k$ for which $x_k \oplus s < x_k$.
In this case, we can remove sticks from
heap $k$ so that it will contain $x_k \oplus s$ sticks,
which will lead to a losing state.
There is always such a heap, where $x_k$
has a one bit at the position of the leftmost
one bit of $s$.

As an example, consider the state $[10,12,5]$.
This state is a winning state,
because its nim sum is 3.
Thus, there has to be a move which
leads to a losing state.
Next we will find out such a move.

The nim sum of the state is as follows:


|  |  |
| ---: | ---: |
| 10 | `1010` |
| 12 | `1100` |
| 5 | `0101` |
| 3 | `0011` |


In this case, the heap with 10 sticks
is the only heap that has a one bit
at the position of the leftmost
one bit of the nim sum:


|  |  |
| ---: | ---: |
| 10 | `10\underline{1}0` |
| 12 | `1100` |
| 5 | `0101` |
| 3 | `00\underline{1}1` |


The new size of the heap has to be
$10 \oplus 3 = 9$,
so we will remove just one stick.
After this, the state will be $[9,12,5]$,
which is a losing state:


|  |  |
| ---: | ---: |
| 9 | `1001` |
| 12 | `1100` |
| 5 | `0101` |
| 0 | `0000` |


## Misère game

In a **misère game**, the goal of the game
is opposite,
so the player who removes the last stick
loses the game.
It turns out that the misère nim game can be
optimally played almost like the standard nim game.

The idea is to first play the misère game
like the standard game, but change the strategy
at the end of the game.
The new strategy will be introduced in a situation
where each heap would contain at most one stick
after the next move.

In the standard game, we should choose a move
after which there is an even number of heaps with one stick.
However, in the misère game, we choose a move so that
there is an odd number of heaps with one stick.

This strategy works because a state where the
strategy changes always appears in the game,
and this state is a winning state, because
it contains exactly one heap that has more than one stick
so the nim sum is not 0.

___

[^1]: The optimal strategy
for nim was published in 1901 by C. L. Bouton [10].
