# Amortized analysis

The time complexity of an algorithm
is often easy to analyze
just by examining the structure
of the algorithm:
what loops does the algorithm contain
and how many times the loops are performed.
However, sometimes a straightforward analysis
does not give a true picture of the efficiency of the algorithm.

**Amortized analysis** can be used to analyze
algorithms that contain operations whose
time complexity varies.
The idea is to estimate the total time used to
all such operations during the
execution of the algorithm, instead of focusing
on individual operations.
