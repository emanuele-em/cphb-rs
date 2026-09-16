# Geometry

In geometric problems, it is often challenging
to find a way to approach the problem so that
the solution to the problem can be conveniently implemented
and the number of special cases is small.

As an example, consider a problem where
we are given the vertices of a quadrilateral
(a polygon that has four vertices),
and our task is to calculate its area.
For example, a possible input for the problem is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.45]

\draw[fill] (6,2) circle [radius=0.1];
\draw[fill] (5,6) circle [radius=0.1];
\draw[fill] (2,5) circle [radius=0.1];
\draw[fill] (1,1) circle [radius=0.1];
\draw[thick] (6,2) -- (5,6) -- (2,5) -- (1,1) -- (6,2);
\end{tikzpicture}
</script>

One way to approach the problem is to divide
the quadrilateral into two triangles by a straight
line between two opposite vertices:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.45]

\draw[fill] (6,2) circle [radius=0.1];
\draw[fill] (5,6) circle [radius=0.1];
\draw[fill] (2,5) circle [radius=0.1];
\draw[fill] (1,1) circle [radius=0.1];

\draw[thick] (6,2) -- (5,6) -- (2,5) -- (1,1) -- (6,2);
\draw[dashed,thick] (2,5) -- (6,2);
\end{tikzpicture}
</script>

After this, it suffices to sum the areas
of the triangles.
The area of a triangle can be calculated,
for example, using **Heron's formula**
\\[
\\sqrt{s (s-a) (s-b) (s-c)},
\\]
where $a$, $b$ and $c$ are the lengths
of the triangle's sides and
$s=(a+b+c)/2$.

This is a possible way to solve the problem,
but there is one pitfall:
how to divide the quadrilateral into triangles?
It turns out that sometimes we cannot just pick
two arbitrary opposite vertices.
For example, in the following situation,
the division line is _outside_ the quadrilateral:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.45]

\draw[fill] (6,2) circle [radius=0.1];
\draw[fill] (3,2) circle [radius=0.1];
\draw[fill] (2,5) circle [radius=0.1];
\draw[fill] (1,1) circle [radius=0.1];
\draw[thick] (6,2) -- (3,2) -- (2,5) -- (1,1) -- (6,2);

\draw[dashed,thick] (2,5) -- (6,2);
\end{tikzpicture}
</script>

However, another way to draw the line works:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.45]

\draw[fill] (6,2) circle [radius=0.1];
\draw[fill] (3,2) circle [radius=0.1];
\draw[fill] (2,5) circle [radius=0.1];
\draw[fill] (1,1) circle [radius=0.1];
\draw[thick] (6,2) -- (3,2) -- (2,5) -- (1,1) -- (6,2);

\draw[dashed,thick] (3,2) -- (1,1);
\end{tikzpicture}
</script>

It is clear for a human which of the lines is the correct
choice, but the situation is difficult for a computer.
                           
However, it turns out that we can solve the problem using
another method that is more convenient to a programmer.
Namely, there is a general formula
\\[
x_1y_2-x_2y_1+x_2y_3-x_3y_2+x_3y_4-x_4y_3+x_4y_1-x_1y_4,
\\]
that calculates the area of a quadrilateral
whose vertices are
$(x_1,y_1)$,
$(x_2,y_2)$,
$(x_3,y_3)$ and
$(x_4,y_4)$.
This formula is easy to implement, there are no special
cases, and we can even generalize the formula
to _all_ polygons.
