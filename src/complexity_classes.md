# Complexity classes

The following list contains common time complexities of algorithms:

| Complexity | Description |
| :---: | :--- |
| $O(1)$ | **Constant-time algorithm**: The running time of a constant-time algorithm does not depend on the input size.  A typical constant-time algorithm is a direct formula that calculates the answer. |
| $O(\log n)$ | **Logarithmic algorithm**: often halves the input size at each step.  The running time of such an algorithm is logarithmic, because $\log_2 n$ equals the number of times $n$ must be divided by 2 to get 1. |
| $O(\sqrt n)$ |**Square root algorithm**: is slower than $O(\log n)$ but faster than $O(n)$.  A special property of square roots is that $\sqrt n = n/\sqrt n$, so the square root $\sqrt n$ lies, in some sense, in the middle of the input. |
| $O(n)$ | **Linear algorithm**: it goes through the input a constant number of times.  This is often the best possible time complexity, because it is usually necessary to access each input element at least once before reporting the answer. |
| $O(n \log n)$ | **Linearithmic algorithm**: This time complexity often indicates that the algorithm sorts the input, because the time complexity of efficient sorting algorithms is $O(n \log n)$.  Another possibility is that the algorithm uses a data structure where each operation takes $O(\log n)$ time. |
| $O(n^2)$ | **Quadratic algorithm**: a quadratic algorithm often contains two nested loops.  It is possible to go through all pairs of the input elements in $O(n^2)$ time. |
| $O(n^3)$ | **Cubic algorithm**: it often contains three nested loops.  It is possible to go through all triplets of the input elements in $O(n^3)$ time. |
| $O(2^n)$ |  **Exponential algorithm**: This time complexity often indicates that the algorithm iterates through all subsets of the input elements.  For example, the subsets of $\{1,2,3\}$ are $\emptyset$, $\{1\}$, $\{2\}$, $\{3\}$, $\{1,2\}$, $\{1,3\}$, $\{2,3\}$ and $\{1,2,3\}$. |
| $O(n!)$ | **Factorial algorithm**: This time complexity often indicates that the algorithm iterates through all permutations of the input elements.  For example, the permutations of $\{1,2,3\}$ are $(1,2,3)$, $(1,3,2)$, $(2,1,3)$, $(2,3,1)$, $(3,1,2)$ and $(3,2,1)$. |

An algorithm is **polynomial** if its time complexity is at most $O(n^k)$ where $k$ is a constant.  All the above time complexities except $O(2^n)$ and $O(n!)$ are polynomial.  In practice, the constant $k$ is usually small, and therefore a polynomial time complexity roughly means that the algorithm is _efficient_.

Most algorithms in this book are polynomial.  Still, there are many important problems for which
no polynomial algorithm is known, i.e., nobody knows how to solve them efficiently.  \key{NP-hard} problems are an important set of problems, for which no polynomial algorithm is known[^1].

___

[^1] A classic book on the topic is M. R. Garey's and D. S. Johnson's _Computers and Intractability: A Guide to the Theory of NP-Completeness_ [28].
