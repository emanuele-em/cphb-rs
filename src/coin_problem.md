# Coin problem

As a first example, we consider a problem
where we are given a set of coins
and our task is to form a sum of money $n$
using the coins.
The values of the coins are
$\texttt{coins}=\{c_1,c_2,\ldots,c_k\}$,
and each coin can be used as many times we want.
What is the minimum number of coins needed?

For example, if the coins are the euro coins (in cents)
$$
\{1,2,5,10,20,50,100,200\}
$$
and $n=520$,
we need at least four coins.
The optimal solution is to select coins
$200+200+100+20$ whose sum is 520.

## Greedy alghoritm

A simple greedy algorithm to the problem
always selects the largest possible coin,
until the required sum of money has been constructed.
This algorithm works in the example case,
because we first select two 200 cent coins,
then one 100 cent coin and finally one 20 cent coin.
But does this algorithm always work?

It turns out that if the coins are the euro coins,
the greedy algorithm _always_ works, i.e.,
it always produces a solution with the fewest
possible number of coins.
The correctness of the algorithm can be
shown as follows:

First, each coin 1, 5, 10, 50 and 100 appears
at most once in an optimal solution,
because if the
solution would contain two such coins,
we could replace them by one coin and
obtain a better solution.
For example, if the solution would contain
coins $5+5$, we could replace them by coin $10$.

In the same way, coins 2 and 20 appear
at most twice in an optimal solution,
because we could replace
coins $2+2+2$ by coins $5+1$ and
coins $20+20+20$ by coins $50+10$.
Moreover, an optimal solution cannot contain
coins $2+2+1$ or $20+20+10$,
because we could replace them by coins $5$ and $50$.

Using these observations,
we can show for each coin $x$ that
it is not possible to optimally construct
a sum $x$ or any larger sum by only using coins
that are smaller than $x$.
For example, if $x=100$, the largest optimal
sum using the smaller coins is  $50+20+20+5+2+2=99$.
Thus, the greedy algorithm that always selects
the largest coin produces the optimal solution.

This example shows that it can be difficult
to argue that a greedy algorithm works,
even if the algorithm itself is simple.

## General case

In the general case, the coin set can contain any coins
and the greedy algorithm _does not_ necessarily produce
an optimal solution.

We can prove that a greedy algorithm does not work
by showing a counterexample
where the algorithm gives a wrong answer.
In this problem we can easily find a counterexample:
if the coins are $\{1,3,4\}$ and the target sum
is 6, the greedy algorithm produces the solution
$4+1+1$ while the optimal solution is $3+3$.

It is not known if the general coin problem
can be solved using any greedy algorithm[^1]
However, as we will see in Chapter 7,
in some cases,
the general problem can be efficiently
solved using a dynamic
programming algorithm that always gives the
correct answer.
___

[^1] However, it is possible to \emph{check} in polynomial time if the greedy algorithm presented in this chapter works for a given set of coins [53]
