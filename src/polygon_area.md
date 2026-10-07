# Polygon area

A general formula for calculating the area
of a polygon, sometimes called the **shoelace formula**,
is as follows: 
\\[
\\frac{1}{2} |\\sum_{i=1}^{n-1} (p_i \\times p_{i+1})| =
\\frac{1}{2} |\\sum_{i=1}^{n-1} (x_i y_{i+1} - x_{i+1} y_i)|,
\\]
Here the vertices are
$p_1=(x_1,y_1)$, $p_2=(x_2,y_2)$, $\ldots$, $p_n=(x_n,y_n)$
in such an order that
$p_i$ and $p_{i+1}$ are adjacent vertices on the boundary
of the polygon,
and the first and last vertex is the same, i.e., $p_1=p_n$.

For example, the area of the polygon

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\filldraw (4,1.4) circle (2pt);
\filldraw (7,3.4) circle (2pt);
\filldraw (5,5.4) circle (2pt);
\filldraw (2,4.4) circle (2pt);
\filldraw (4,3.4) circle (2pt);
\node (1) at (4,1) {(4,1)};
\node (2) at (7.2,3) {(7,3)};
\node (3) at (5,5.8) {(5,5)};
\node (4) at (2,4) {(2,4)};
\node (5) at (3.5,3) {(4,3)};
\path[draw] (4,1.4) -- (7,3.4) -- (5,5.4) -- (2,4.4) -- (4,3.4) -- (4,1.4);
\end{tikzpicture}
</script>

is
\\[
\\frac{|(2\\cdot5-5\\cdot4)+(5\\cdot3-7\\cdot5)+(7\\cdot1-4\\cdot3)+(4\\cdot3-4\\cdot1)+(4\\cdot4-2\\cdot3)|}{2} = 17/2.
\\]

The idea of the formula is to go through trapezoids
whose one side is a side of the polygon,
and another side lies on the horizontal line $y=0$.
For example:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\path[draw,fill=lightgray] (5,5.4) -- (7,3.4) -- (7,0) -- (5,0) -- (5,5.4);
\filldraw (4,1.4) circle (2pt);
\filldraw (7,3.4) circle (2pt);
\filldraw (5,5.4) circle (2pt);
\filldraw (2,4.4) circle (2pt);
\filldraw (4,3.4) circle (2pt);
\node (1) at (4,1) {(4,1)};
\node (2) at (7.2,3) {(7,3)};
\node (3) at (5,5.8) {(5,5)};
\node (4) at (2,4) {(2,4)};
\node (5) at (3.5,3) {(4,3)};
\path[draw] (4,1.4) -- (7,3.4) -- (5,5.4) -- (2,4.4) -- (4,3.4) -- (4,1.4);
\draw (0,0) -- (10,0);
\end{tikzpicture}
</script>

The area of such a trapezoid is
\\[
(x_{i+1}-x_{i}) \\frac{y_i+y_{i+1}}{2},
\\]
where the vertices of the polygon are $p_i$ and $p_{i+1}$.
If $x_{i+1}>x_{i}$, the area is positive,
and if $x_{i+1}<x_{i}$, the area is negative.

The area of the polygon is the sum of areas of
all such trapezoids, which yields the formula
\\[
|\\sum_{i=1}^{n-1} (x_{i+1}-x_{i}) \\frac{y_i+y_{i+1}}{2}| =
\\frac{1}{2} |\\sum_{i=1}^{n-1} (x_i y_{i+1} - x_{i+1} y_i)|.
\\]

Note that the absolute value of the sum is taken,
because the value of the sum may be positive or negative,
depending on whether we walk clockwise or counterclockwise
along the boundary of the polygon.

## Pick's theorem

**Pick's theorem** provides another way to calculate
the area of a polygon provided that all vertices 
of the polygon have integer coordinates.
According to Pick's theorem, the area of the polygon is
\\[
a + b/2 -1,
\\]
where $a$ is the number of integer points inside the polygon
and $b$ is the number of integer points on the boundary of the polygon.

For example, the area of the polygon

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\filldraw (4,1.4) circle (2pt);
\filldraw (7,3.4) circle (2pt);
\filldraw (5,5.4) circle (2pt);
\filldraw (2,4.4) circle (2pt);
\filldraw (4,3.4) circle (2pt);
\node (1) at (4,1) {(4,1)};
\node (2) at (7.2,3) {(7,3)};
\node (3) at (5,5.8) {(5,5)};
\node (4) at (2,4) {(2,4)};
\node (5) at (3.5,3) {(4,3)};
\path[draw] (4,1.4) -- (7,3.4) -- (5,5.4) -- (2,4.4) -- (4,3.4) -- (4,1.4);

\filldraw (2,4.4) circle (2pt);
\filldraw (3,4.4) circle (2pt);
\filldraw (4,4.4) circle (2pt);
\filldraw (5,4.4) circle (2pt);
\filldraw (6,4.4) circle (2pt);

\filldraw (4,3.4) circle (2pt);
\filldraw (5,3.4) circle (2pt);
\filldraw (6,3.4) circle (2pt);
\filldraw (7,3.4) circle (2pt);

\filldraw (4,2.4) circle (2pt);
\filldraw (5,2.4) circle (2pt);
\end{tikzpicture}
</script>

is $6+7/2-1=17/2$.
