# Estimating efficiency

By calculating the time complexity of an algorithm, it is possible to check, before implementing the algorithm, that it is efficient enough for the problem.
The starting point for estimations is the fact that a modern computer can perform some hundreds of millions of operations in a second.

For example, assume that the time limit for a problem is one second and the input size is $n=10^5$.
If the time complexity is $O(n^2)$, the algorithm will perform about $(10^5)^2=10^{10}$ operations.
This should take at least some tens of seconds, so the algorithm seems to be too slow for solving the problem.

On the other hand, given the input size, we can try to _guess_ the required time complexity of the algorithm that solves the problem.
The following table contains some useful estimates assuming a time limit of one second.

| input size | reuired time complexity |
| --- | --- |
| $n \le 10$ | $O(n!)$ |
| $n \le 20$ | $O(2^n)$ |
| $n \le 500$ | $O(n^3)$ |
| $n \le 5000$ | $O(n^2)$ |
| $n \le 10^6$ | $O(n \log n)$ or $O(n)$ |
| $n$ is large | $O(1)$ or $O(\log n)$ |

For example, if the input size is $n=10^5$, it is probably expected that the time
complexity of the algorithm is $O(n)$ or $O(n \log n)$.
This information makes it easier to design the algorithm, because it rules out approaches that would yield an algorithm with a worse time complexity.

Still, it is important to remember that a time complexity is only an estimate of efficiency, because it hides the _constant factors_.
For example, an algorithm that runs in $O(n)$ time may perform $n/2$ or $5n$ operations.
This has an important effect on the actual running time of the algorithm.
