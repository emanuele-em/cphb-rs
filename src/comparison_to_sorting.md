# Comparison to sorting

It is often possible to solve a problem
using either data structures or sorting.
Sometimes there are remarkable differences
in the actual efficiency of these approaches,
which may be hidden in their time complexities.

Let us consider a problem where
we are given two lists $A$ and $B$
that both contain $n$ elements.
Our task is to calculate the number of elements
that belong to both of the lists.
For example, for the lists

$$
A = (5,2,8,9) \hspace{10px} \textrm{and} \hspace{10px} B = (3,2,9,5)
$$

the answer is 3 because the numbers 2, 5
and 9 belong to both of the lists.

A straightforward solution to the problem is
to go through all pairs of elements in $O(n^2)$ time,
but next we will focus on
more efficient algorithms.

## Algorithm 1

We construct a set of the elements that appear in $A$,
and after this, we iterate through the elements
of $B$ and check for each elements if it
also belongs to $A$.
This is efficient because the elements of $A$
are in a set.
Using the `BTreeSet` structure,
the time complexity of the algorithm is $O(n \log n)$.

## Algorithm 2

It is not necessary to maintain an ordered set,
so instead of the `BTreeSet` structure
we can also use the `HashSet` structure.
This is an easy way to make the algorithm
more efficient, because we only have to change
the underlying data structure.
The time complexity of the new algorithm is $O(n)$.

## Algorithm 3

Instead of data structures, we can use sorting.
First, we sort both lists $A$ and $B$.
After this, we iterate through both the lists
at the same time and find the common elements.
The time complexity of sorting is $O(n \log n)$,
and the rest of the algorithm works in $O(n)$ time,
so the total time complexity is $O(n \log n)$.

## Efficiency Comparison

The following table shows how efficient
the above algorithms are when $n$ varies and
the elements of the lists are random
integers between $1 \ldots 10^9$:

| $n$ | Algorithm 1 | Algorithm 2 | Algorithm 3 |
|----:|------------:|------------:|------------:|
| $10^6$ | $1.5$ s | $0.3$ s | $0.2$ s |
| $2 \cdot 10^6$ | $3.7$ s | $0.8$ s | $0.3$ s |
| $3 \cdot 10^6$ | $5.7$ s | $1.3$ s | $0.5$ s |
| $4 \cdot 10^6$ | $7.7$ s | $1.7$ s | $0.7$ s |
| $5 \cdot 10^6$ | $10.0$ s | $2.3$ s | $0.9$ s |

Algorithms 1 and 2 are equal except that
they use different set structures.
In this problem, this choice has an important effect on
the running time, because Algorithm 2
is 4–5 times faster than Algorithm 1.

However, the most efficient algorithm is Algorithm 3
which uses sorting.
It only uses half the time compared to Algorithm 2.
Interestingly, the time complexity of both
Algorithm 1 and Algorithm 3 is $O(n \log n)$,
but despite this, Algorithm 3 is ten times faster.
This can be explained by the fact that
sorting is a simple procedure and it is done
only once at the beginning of Algorithm 3,
and the rest of the algorithm works in linear time.
On the other hand,
Algorithm 1 maintains a complex balanced binary tree
during the whole algorithm.
