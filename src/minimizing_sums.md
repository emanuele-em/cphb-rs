# Minimizing sums

We next consider a problem where
we are given $n$ numbers $a_1,a_2,\ldots,a_n$
and our task is to find a value $x$
that minimizes the sum

$$
    |a_1-x|^c+|a_2-x|^c+\cdots+|a_n-x|^c
$$

We focus on the cases $c=1$ and $c=2$.

## Case $c=1$

In this case, we should minimize the sum

$$
|a_1-x|+|a_2-x|+\cdots+|a_n-x|
$$

For example, if the numbers are $[1,2,9,2,6]$,
the best solution is to select $x=2$
which produces the sum

$$
|1-2|+|2-2|+|9-2|+|2-2|+|6-2|=12.
$$

In the general case, the best choice for $x$
is the _median_ of the numbers,
i.e., the middle number after sorting.
For example, the list $[1,2,9,2,6]$
becomes $[1,2,2,6,9]$ after sorting,
so the median is 2.

The median is an optimal choice,
because if $x$ is smaller than the median,
the sum becomes smaller by increasing $x$,
and if $x$ is larger then the median,
the sum becomes smaller by decreasing $x$.
Hence, the optimal solution is that $x$
is the median.
If $n$ is even and there are two medians,
both medians and all values between them
are optimal choices.

## Case $c=2$

In this case, we should minimize the sum
$$
(a_1-x)^2+(a_2-x)^2+\cdots+(a_n-x)^2
$$

For example, if the numbers are $[1,2,9,2,6]$,
the best solution is to select $x=4$
which produces the sum

$$
(1-4)^2+(2-4)^2+(9-4)^2+(2-4)^2+(6-4)^2=46.
$$

In the general case, the best choice for $x$
is the _average_ of the numbers.
In the example the average is $\frac{1+2+9+2+6}{5}=4$.
This result can be derived by presenting
the sum as follows:

$$
nx^2 - 2x(a_1+a_2+\cdots+a_n) + (a_1^2+a_2^2+\cdots+a_n^2)
$$

The last part does not depend on $x$,
so we can ignore it.
The remaining parts form a function
$nx^2-2xs$ where $s=a_1+a_2+\cdots+a_n$.
This is a parabola opening upwards
with roots $x=0$ and $x=2\frac{s}{n}$,
and the minimum value is the average
of the roots $x=\frac{s}{n}$, i.e.,
the average of the numbers $a_1,a_2,\ldots,a_n$.
