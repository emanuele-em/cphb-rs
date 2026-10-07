# Random variables

A **random variable** is a value that is generated
by a random process.
For example, when throwing two dice,
a possible random variable is
\\[
X=\\textrm{''the sum of the outcomes''}.
\\]
For example, if the outcomes are $[4,6]$
(meaning that we first throw a four and then a six),
then the value of $X$ is 10.

We denote $P(X=x)$ the probability that
the value of a random variable $X$ is $x$.
For example, when throwing two dice,
$P(X=10)=3/36$,
because the total number of outcomes is 36
and there are three possible ways to obtain
the sum 10: $[4,6]$, $[5,5]$ and $[6,4]$.

## Expected value

The **expected value** $E[X]$ indicates the
average value of a random variable $X$.
The expected value can be calculated as the sum
\\[
\\sum_x P(X=x)x,
\\]
where $x$ goes through all possible values of $X$.

For example, when throwing a dice,
the expected outcome is
\\[
1/6 \\cdot 1 + 1/6 \\cdot 2 + 1/6 \\cdot 3 + 1/6 \\cdot 4 + 1/6 \\cdot 5 + 1/6 \\cdot 6 = 7/2.
\\]

A useful property of expected values is **linearity**.
It means that the sum
$E[X_1+X_2+\cdots+X_n]$
always equals the sum
$E[X_1]+E[X_2]+\cdots+E[X_n]$.
This formula holds even if random variables
depend on each other.

For example, when throwing two dice,
the expected sum is
\\[
E[X_1+X_2]=E[X_1]+E[X_2]=7/2+7/2=7.
\\]

Let us now consider a problem where
$n$ balls are randomly placed in $n$ boxes,
and our task is to calculate the expected
number of empty boxes.
Each ball has an equal probability to
be placed in any of the boxes.
For example, if $n=2$, the possibilities
are as follows:

<script type="text/tikz">
\begin{tikzpicture}
\draw (0,0) rectangle (1,1);
\draw (1.2,0) rectangle (2.2,1);
\draw (3,0) rectangle (4,1);
\draw (4.2,0) rectangle (5.2,1);
\draw (6,0) rectangle (7,1);
\draw (7.2,0) rectangle (8.2,1);
\draw (9,0) rectangle (10,1);
\draw (10.2,0) rectangle (11.2,1);

\draw[fill=blue] (0.5,0.2) circle (0.1);
\draw[fill=red] (1.7,0.2) circle (0.1);
\draw[fill=red] (3.5,0.2) circle (0.1);
\draw[fill=blue] (4.7,0.2) circle (0.1);
\draw[fill=blue] (6.25,0.2) circle (0.1);
\draw[fill=red] (6.75,0.2) circle (0.1);
\draw[fill=blue] (10.45,0.2) circle (0.1);
\draw[fill=red] (10.95,0.2) circle (0.1);
\end{tikzpicture}
</script>

In this case, the expected number of
empty boxes is
\\[
\\frac{0+0+1+1}{4} = \\frac{1}{2}.
\\]
In the general case, the probability that a
single box is empty is
\\[
\\Big(\\frac{n-1}{n}\\Big)^n,
\\]
because no ball should be placed in it.
Hence, using linearity, the expected number of
empty boxes is
\\[
n \\cdot \\Big(\\frac{n-1}{n}\\Big)^n.
\\]

## Distributions

The **distribution** of a random variable $X$
shows the probability of each value that
$X$ may have.
The distribution consists of values $P(X=x)$.
For example, when throwing two dice,
the distribution for their sum is:

\small {

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $x$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| $P(X=x)$ | $1/36$ | $2/36$ | $3/36$ | $4/36$ | $5/36$ | $6/36$ | $5/36$ | $4/36$ | $3/36$ | $2/36$ | $1/36$ |

}

In a **uniform distribution**,
the random variable $X$ has $n$ possible
values $a,a+1,\ldots,b$ and the probability of each value is $1/n$.
For example, when throwing a dice,
$a=1$, $b=6$ and $P(X=x)=1/6$ for each value $x$.

The expected value of $X$ in a uniform distribution is
\\[
E[X] = \\frac{a+b}{2}.
\\]

In a **binomial distribution**, $n$ attempts
are made
and the probability that a single attempt succeeds
is $p$.
The random variable $X$ counts the number of
successful attempts,
and the probability of a value $x$ is
\\[
P(X=x)=p^x (1-p)^{n-x} {n \\choose x},
\\]
where $p^x$ and $(1-p)^{n-x}$ correspond to
successful and unsuccessful attemps,
and ${n \choose x}$ is the number of ways
we can choose the order of the attempts.

For example, when throwing a dice ten times,
the probability of throwing a six exactly
three times is $(1/6)^3 (5/6)^7 {10 \choose 3}$.

The expected value of $X$ in a binomial distribution is
\\[
E[X] = pn.
\\]

In a **geometric distribution**,
the probability that an attempt succeeds is $p$,
and we continue until the first success happens.
The random variable $X$ counts the number
of attempts needed, and the probability of
a value $x$ is
\\[
P(X=x)=(1-p)^{x-1} p,
\\]
where $(1-p)^{x-1}$ corresponds to the unsuccessful attemps
and $p$ corresponds to the first successful attempt.

For example, if we throw a dice until we throw a six,
the probability that the number of throws
is exactly 4 is $(5/6)^3 1/6$.

The expected value of $X$ in a geometric distribution is
\\[
E[X]=\\frac{1}{p}.
\\]
