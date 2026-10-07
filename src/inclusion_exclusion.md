# Inclusion-exclusion

**Inclusion-exclusion** is a technique
that can be used for counting the size
of a union of sets when the sizes of
the intersections are known, and vice versa.
A simple example of the technique is the formula
\\[
|A \\cup B| = |A| + |B| - |A \\cap B|,
\\]
where $A$ and $B$ are sets and $|X|$
denotes the size of $X$.
The formula can be illustrated as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.8]

\draw (0,0) circle (1.5);
\draw (1.5,0) circle (1.5);

\node at (-0.75,0) {\small $A$};
\node at (2.25,0) {\small $B$};
\node at (0.75,0) {\small $A \cap B$};

\end{tikzpicture}
</script>

Our goal is to calculate
the size of the union $A \cup B$
that corresponds to the area of the region
that belongs to at least one circle.
The picture shows that we can calculate
the area of $A \cup B$ by first summing the
areas of $A$ and $B$ and then subtracting
the area of $A \cap B$.

The same idea can be applied when the number
of sets is larger.
When there are three sets, the inclusion-exclusion formula is
\\[
|A \\cup B \\cup C| = |A| + |B| + |C| - |A \\cap B|  - |A \\cap C|  - |B \\cap C| + |A \\cap B \\cap C|
\\]
and the corresponding picture is

<script type="text/tikz">
\begin{tikzpicture}[scale=0.8]

\draw (0,0) circle (1.75);
\draw (2,0) circle (1.75);
\draw (1,1.5) circle (1.75);

\node at (-0.75,-0.25) {\small $A$};
\node at (2.75,-0.25) {\small $B$};
\node at (1,2.5) {\small $C$};
\node at (1,-0.5) {\small $A \cap B$};
\node at (0,1.25) {\small $A \cap C$};
\node at (2,1.25) {\small $B \cap C$};
\node at (1,0.5) {\scriptsize $A \cap B \cap C$};

\end{tikzpicture}
</script>

In the general case, the size of the 
union $X_1 \cup X_2 \cup \cdots \cup X_n$
can be calculated by going through all possible
intersections that contain some of the sets $X_1,X_2,\ldots,X_n$.
If the intersection contains an odd number of sets,
its size is added to the answer,
and otherwise its size is subtracted from the answer.

Note that there are similar formulas
for calculating
the size of an intersection from the sizes of
unions. For example,
\\[
|A \\cap B| = |A| + |B| - |A \\cup B|
\\]
and
\\[
|A \\cap B \\cap C| = |A| + |B| + |C| - |A \\cup B|  - |A \\cup C|  - |B \\cup C| + |A \\cup B \\cup C| .
\\]

## Derangements

As an example, let us count the number of **derangements**
of elements $\\{1,2,\ldots,n\\}$, i.e., permutations
where no element remains in its original place.
For example, when $n=3$, there are
two derangements: $(2,3,1)$ and $(3,1,2)$.

One approach for solving the problem is to use
inclusion-exclusion.
Let $X_k$ be the set of permutations
that contain the element $k$ at position $k$.
For example, when $n=3$, the sets are as follows:
\\[
\\begin{array}{lcl}
X_1 & = & \\{(1,2,3),(1,3,2)\\} \\\\
X_2 & = & \\{(1,2,3),(3,2,1)\\} \\\\
X_3 & = & \\{(1,2,3),(2,1,3)\\} \\\\
\\end{array}
\\]
Using these sets, the number of derangements equals
\\[
n! - |X_1 \\cup X_2 \\cup \\cdots \\cup X_n|,
\\]
so it suffices to calculate the size of the union.
Using inclusion-exclusion, this reduces to
calculating sizes of intersections which can be
done efficiently.
For example, when $n=3$, the size of
$|X_1 \cup X_2 \cup X_3|$ is
\\[
\\begin{array}{lcl}
 & & |X_1| + |X_2| + |X_3| - |X_1 \\cap X_2|  - |X_1 \\cap X_3|  - |X_2 \\cap X_3| + |X_1 \\cap X_2 \\cap X_3| \\\\
 & = & 2+2+2-1-1-1+1 \\\\
 & = & 4, \\\\
\\end{array}
\\]
so the number of solutions is $3!-4=2$.

It turns out that the problem can also be solved
without using inclusion-exclusion.
Let $f(n)$ denote the number of derangements
for $\\{1,2,\ldots,n\\}$. We can use the following
recursive formula:

\\begin{equation*}
    f(n) = \\begin{cases}
               0               & n = 1\\\\
               1               & n = 2\\\\
               (n-1)(f(n-2) + f(n-1)) & n>2 \\\\
           \\end{cases}
\\end{equation*}

The formula can be derived by considering
the possibilities how the element 1 changes
in the derangement.
There are $n-1$ ways to choose an element $x$
that replaces the element 1.
In each such choice, there are two options:

_Option 1:_ We also replace the element $x$
with the element 1.
After this, the remaining task is to construct
a derangement of $n-2$ elements.

_Option 2:_ We replace the element $x$
with some other element than 1.
Now we have to construct a derangement
of $n-1$ element, because we cannot replace
the element $x$ with the element $1$, and all other
elements must be changed.
