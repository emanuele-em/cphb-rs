# String algorithms

This chapter deals with efficient algorithms
for string processing.
Many string problems can be easily solved
in $O(n^2)$ time, but the challenge is to
find algorithms that work in $O(n)$ or $O(n \log n)$
time.

For example, a fundamental string processing
problem is the **pattern matching** problem:
given a string of length $n$ and a pattern of length $m$,
our task is to find the occurrences of the pattern
in the string.
For example, the pattern `ABC` occurs two
times in the string `ABABCBABC`.

The pattern matching problem can be easily solved
in $O(nm)$ time by a brute force algorithm that
tests all positions where the pattern may
occur in the string.
However, in this chapter, we will see that there
are more efficient algorithms that require only
$O(n+m)$ time.
