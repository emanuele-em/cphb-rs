# Burnside's lemma

**Burnside's lemma**
can be used to count
the number of combinations so that
only one representative is counted
for each group of symmetric combinations.
Burnside's lemma states that the number of
combinations is
\\[
\\sum_{k=1}^n \\frac{c(k)}{n},
\\]
where there are $n$ ways to change the
position of a combination,
and there are $c(k)$ combinations that
remain unchanged when the $k$th way is applied.

As an example, let us calculate the number of
necklaces of $n$ pearls,
where each pearl has $m$ possible colors.
Two necklaces are symmetric if they are
similar after rotating them.
For example, the necklace

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw[fill=white] (0,0) circle (1);
\draw[fill=red] (0,1) circle (0.3);
\draw[fill=blue] (1,0) circle (0.3);
\draw[fill=red] (0,-1) circle (0.3);
\draw[fill=green] (-1,0) circle (0.3);
\end{tikzpicture}
</script>

has the following symmetric necklaces:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw[fill=white] (0,0) circle (1);
\draw[fill=red] (0,1) circle (0.3);
\draw[fill=blue] (1,0) circle (0.3);
\draw[fill=red] (0,-1) circle (0.3);
\draw[fill=green] (-1,0) circle (0.3);

\draw[fill=white] (4,0) circle (1);
\draw[fill=green] (4+0,1) circle (0.3);
\draw[fill=red] (4+1,0) circle (0.3);
\draw[fill=blue] (4+0,-1) circle (0.3);
\draw[fill=red] (4+-1,0) circle (0.3);

\draw[fill=white] (8,0) circle (1);
\draw[fill=red] (8+0,1) circle (0.3);
\draw[fill=green] (8+1,0) circle (0.3);
\draw[fill=red] (8+0,-1) circle (0.3);
\draw[fill=blue] (8+-1,0) circle (0.3);

\draw[fill=white] (12,0) circle (1);
\draw[fill=blue] (12+0,1) circle (0.3);
\draw[fill=red] (12+1,0) circle (0.3);
\draw[fill=green] (12+0,-1) circle (0.3);
\draw[fill=red] (12+-1,0) circle (0.3);
\end{tikzpicture}
</script>

There are $n$ ways to change the position
of a necklace,
because we can rotate it
$0,1,\ldots,n-1$ steps clockwise.
If the number of steps is 0,
all $m^n$ necklaces remain the same,
and if the number of steps is 1,
only the $m$ necklaces where each
pearl has the same color remain the same.

More generally, when the number of steps is $k$,
a total of
\\[
m^{\\textrm{gcd}(k,n)}
\\]
necklaces remain the same,
where $\textrm{gcd}(k,n)$ is the greatest common
divisor of $k$ and $n$.
The reason for this is that blocks
of pearls of size $\textrm{gcd}(k,n)$
will replace each other.
Thus, according to Burnside's lemma,
the number of necklaces is
\\[
\\sum_{i=0}^{n-1} \\frac{m^{\\textrm{gcd}(i,n)}}{n}.
\\]
For example, the number of necklaces of length 4
with 3 colors is
\\[
\\frac{3^4+3+3^2+3}{4} = 24.
\\]
