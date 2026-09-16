# Integer partitions

Some square root algorithms are based on
the following observation:
if a positive integer $n$ is represented as
a sum of positive integers,
such a sum always contains at most
$O(\sqrt n)$ _distinct_ numbers.
The reason for this is that to construct
a sum that contains a maximum number of distinct
numbers, we should choose _small_ numbers.
If we choose the numbers $1,2,\ldots,k$,
the resulting sum is
\\[
\\frac{k(k+1)}{2}.
\\]
Thus, the maximum amount of distinct numbers is $k = O(\sqrt n)$.
Next we will discuss two problems that can be solved
efficiently using this observation.

## Knapsack

Suppose that we are given a list of integer weights
whose sum is $n$.
Our task is to find out all sums that can be formed using
a subset of the weights. For example, if the weights are
$\\{1,3,3\\}$, the possible sums are as follows:
- $0$ (empty set)
- $1$
- $3$
- $1+3=4$
- $3+3=6$
- $1+3+3=7$

Using the standard knapsack approach (see Chapter 7.4),
the problem can be solved as follows:
we define a function $\texttt{possible}(x,k)$ whose value is 1
if the sum $x$ can be formed using the first $k$ weights,
and 0 otherwise.
Since the sum of the weights is $n$,
there are at most $n$ weights and
all values of the function can be calculated
in $O(n^2)$ time using dynamic programming.

However, we can make the algorithm more efficient
by using the fact that there are at most $O(\sqrt n)$
_distinct_ weights.
Thus, we can process the weights in groups
that consists of similar weights.
We can process each group
in $O(n)$ time, which yields an $O(n \sqrt n)$ time algorithm.

The idea is to use an array that records the sums of weights
that can be formed using the groups processed so far.
The array contains $n$ elements: element $k$ is 1 if the sum
$k$ can be formed and 0 otherwise.
To process a group of weights, we scan the array
from left to right and record the new sums of weights that
can be formed using this group and the previous groups.

## String construction

Given a string `s` of length $n$
and a set of strings $D$ whose total length is $m$,
consider the problem of counting the number of ways
`s` can be formed as a concatenation of strings in $D$.
For example,
if $\texttt{s}=\texttt{ABAB}$ and
$D=\\{\texttt{A},\texttt{B},\texttt{AB}\\}$,
there are 4 ways:
- $\texttt{A}+\texttt{B}+\texttt{A}+\texttt{B}$
- $\texttt{AB}+\texttt{A}+\texttt{B}$
- $\texttt{A}+\texttt{B}+\texttt{AB}$
- $\texttt{AB}+\texttt{AB}$

We can solve the problem using dynamic programming:
Let $\texttt{count}(k)$ denote the number of ways to construct the prefix
$\texttt{s}[0 \ldots k]$ using the strings in $D$.
Now $\texttt{count}(n-1)$ gives the answer to the problem,
and we can solve the problem in $O(n^2)$ time
using a trie structure.

However, we can solve the problem more efficiently
by using string hashing and the fact that there
are at most $O(\sqrt m)$ distinct string lengths in $D$.
First, we construct a set $H$ that contains all
hash values of the strings in $D$.
Then, when calculating a value of $\texttt{count}(k)$,
we go through all values of $p$
such that there is a string of length $p$ in $D$,
calculate the hash value of $\texttt{s}[k-p+1 \ldots k]$
and check if it belongs to $H$.
Since there are at most $O(\sqrt m)$ distinct string lengths,
this results in an algorithm whose running time is $O(n \sqrt m)$.
