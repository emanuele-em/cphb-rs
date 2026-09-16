# Catalan numbers

The **Catalan number**
$C_n$ equals the
number of valid
parenthesis expressions that consist of
$n$ left parentheses and $n$ right parentheses.

For example, $C_3=5$, because
we can construct the following parenthesis
expressions using three
left and right parentheses:

- `()()()`
- `(())()`
- `()(())`
- `((()))`
- `(()())`

## Parenthesis expressions

What is exactly a _valid parenthesis expression_?
The following rules precisely define all
valid parenthesis expressions:
- An empty parenthesis expression is valid.
- If an expression $A$ is valid,
then also the expression
`(`$A$`)` is valid.
- If expressions $A$ and $B$ are valid,
then also the expression $AB$ is valid.

Another way to characterize valid 
parenthesis expressions is that if
we choose any prefix of such an expression,
it has to contain at least as many left
parentheses as right parentheses.
In addition, the complete expression has to
contain an equal number of left and right
parentheses.

## Formula 1

Catalan numbers can be calculated using the formula
\\[
C_n = \\sum_{i=0}^{n-1} C_{i} C_{n-i-1}.
\\]

The sum goes through the ways to divide the
expression into two parts
such that both parts are valid
expressions and the first part is as short as possible
but not empty.
For any $i$, the first part contains $i+1$ pairs
of parentheses and the number of expressions
is the product of the following values:
- $C_{i}$: the number of ways to construct an expression
using the parentheses of the first part,
not counting the outermost parentheses
- $C_{n-i-1}$: the number of ways to construct an
expression using the parentheses of the second part

The base case is $C_0=1$,
because we can construct an empty parenthesis
expression using zero pairs of parentheses.

## Formula 2

Catalan numbers can also be calculated
using binomial coefficients:
\\[
C_n = \\frac{1}{n+1} {2n \\choose n}
\\]
The formula can be explained as follows:

There are a total of ${2n \choose n}$ ways
to construct a (not necessarily valid)
parenthesis expression that contains $n$ left
parentheses and $n$ right parentheses.
Let us calculate the number of such
expressions that are _not_ valid.

If a parenthesis expression is not valid,
it has to contain a prefix where the
number of right parentheses exceeds the
number of left parentheses.
The idea is to reverse each parenthesis
that belongs to such a prefix.
For example, the expression
`())()(` contains a prefix `())`,
and after reversing the prefix,
the expression becomes `)((()(`.

The resulting expression consists of $n+1$
left parentheses and $n-1$ right parentheses.
The number of such expressions is ${2n \choose n+1}$,
which equals the number of non-valid
parenthesis expressions.
Thus, the number of valid parenthesis
expressions can be calculated using the formula
\\[
{2n \\choose n}-{2n \\choose n+1} = {2n \\choose n} - \\frac{n}{n+1} {2n \\choose n} = \\frac{1}{n+1} {2n \\choose n}.
\\]

## Counting trees

Catalan numbers are also related to trees:
- there are $C_n$ binary trees of $n$ nodes
- there are $C_{n-1}$ rooted trees of $n$ nodes

\noindent
For example, for $C_3=5$, the binary trees are

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\path[draw,thick,-] (0,0) -- (-1,-1);
\path[draw,thick,-] (0,0) -- (1,-1);
\draw[fill=white] (0,0) circle (0.3);
\draw[fill=white] (-1,-1) circle (0.3);
\draw[fill=white] (1,-1) circle (0.3);

\path[draw,thick,-] (4,0) -- (4-0.75,-1) -- (4-1.5,-2);
\draw[fill=white] (4,0) circle (0.3);
\draw[fill=white] (4-0.75,-1) circle (0.3);
\draw[fill=white] (4-1.5,-2) circle (0.3);

\path[draw,thick,-] (6.5,0) -- (6.5-0.75,-1) -- (6.5-0,-2);
\draw[fill=white] (6.5,0) circle (0.3);
\draw[fill=white] (6.5-0.75,-1) circle (0.3);
\draw[fill=white] (6.5-0,-2) circle (0.3);

\path[draw,thick,-] (9,0) -- (9+0.75,-1) -- (9-0,-2);
\draw[fill=white] (9,0) circle (0.3);
\draw[fill=white] (9+0.75,-1) circle (0.3);
\draw[fill=white] (9-0,-2) circle (0.3);

\path[draw,thick,-] (11.5,0) -- (11.5+0.75,-1) -- (11.5+1.5,-2);
\draw[fill=white] (11.5,0) circle (0.3);
\draw[fill=white] (11.5+0.75,-1) circle (0.3);
\draw[fill=white] (11.5+1.5,-2) circle (0.3);
\end{tikzpicture}
</script>

and the rooted trees are

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\path[draw,thick,-] (0,0) -- (-1,-1);
\path[draw,thick,-] (0,0) -- (0,-1);
\path[draw,thick,-] (0,0) -- (1,-1);
\draw[fill=white] (0,0) circle (0.3);
\draw[fill=white] (-1,-1) circle (0.3);
\draw[fill=white] (0,-1) circle (0.3);
\draw[fill=white] (1,-1) circle (0.3);

\path[draw,thick,-] (3,0) -- (3,-1) -- (3,-2) -- (3,-3);
\draw[fill=white] (3,0) circle (0.3);
\draw[fill=white] (3,-1) circle (0.3);
\draw[fill=white] (3,-2) circle (0.3);
\draw[fill=white] (3,-3) circle (0.3);

\path[draw,thick,-] (6+0,0) -- (6-1,-1);
\path[draw,thick,-] (6+0,0) -- (6+1,-1) -- (6+1,-2);
\draw[fill=white] (6+0,0) circle (0.3);
\draw[fill=white] (6-1,-1) circle (0.3);
\draw[fill=white] (6+1,-1) circle (0.3);
\draw[fill=white] (6+1,-2) circle (0.3);

\path[draw,thick,-] (9+0,0) -- (9+1,-1);
\path[draw,thick,-] (9+0,0) -- (9-1,-1) -- (9-1,-2);
\draw[fill=white] (9+0,0) circle (0.3);
\draw[fill=white] (9+1,-1) circle (0.3);
\draw[fill=white] (9-1,-1) circle (0.3);
\draw[fill=white] (9-1,-2) circle (0.3);

\path[draw,thick,-] (12+0,0) -- (12+0,-1) -- (12-1,-2);
\path[draw,thick,-] (12+0,0) -- (12+0,-1) -- (12+1,-2);
\draw[fill=white] (12+0,0) circle (0.3);
\draw[fill=white] (12+0,-1) circle (0.3);
\draw[fill=white] (12-1,-2) circle (0.3);
\draw[fill=white] (12+1,-2) circle (0.3);

\end{tikzpicture}
</script>
