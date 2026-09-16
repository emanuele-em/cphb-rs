# Calculation

To calculate the probability of an event,
we can either use combinatorics
or simulate the process that generates the event.
As an example, let us calculate the probability
of drawing three cards with the same value
from a shuffled deck of cards
(for example, $\spadesuit 8$, $\clubsuit 8$ and $\diamondsuit 8$).

## Method 1

We can calculate the probability using the formula

\\[
\\frac{\\textrm{number of desired outcomes}}{\\textrm{total number of outcomes}}.
\\]

In this problem, the desired outcomes are those
in which the value of each card is the same.
There are $13 {4 \choose 3}$ such outcomes,
because there are $13$ possibilities for the
value of the cards and ${4 \choose 3}$ ways to
choose $3$ suits from $4$ possible suits.

There are a total of ${52 \choose 3}$ outcomes,
because we choose 3 cards from 52 cards.
Thus, the probability of the event is

\\[
\\frac{13 {4 \\choose 3}}{{52 \\choose 3}} = \\frac{1}{425}.
\\]

## Method 2

Another way to calculate the probability is
to simulate the process that generates the event.
In this example, we draw three cards, so the process
consists of three steps.
We require that each step of the process is successful.

Drawing the first card certainly succeeds,
because there are no restrictions.
The second step succeeds with probability $3/51$,
because there are 51 cards left and 3 of them
have the same value as the first card.
In a similar way, the third step succeeds with probability $2/50$.

The probability that the entire process succeeds is

\\[
1 \\cdot \\frac{3}{51} \\cdot \\frac{2}{50} = \\frac{1}{425}.
\\]
