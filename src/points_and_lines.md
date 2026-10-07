# Points and lines

The **cross product** $a \times b$ of vectors
$a=(x_1,y_1)$ and $b=(x_2,y_2)$ is calculated
using the formula $x_1 y_2 - x_2 y_1$.
The cross product tells us whether $b$
turns left (positive value), does not turn (zero)
or turns right (negative value)
when it is placed directly after $a$.

The following picture illustrates the above cases:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.45]

\draw[->,thick] (0,0)--(4,2);
\draw[->,thick] (4,2)--(4+1,2+2);

\node at (2.5,0.5) {$a$};
\node at (5,2.5) {$b$};

\node at (3,-2) {$a \times b = 6$};

\draw[->,thick] (8+0,0)--(8+4,2);
\draw[->,thick] (8+4,2)--(8+4+2,2+1);

\node at (8+2.5,0.5) {$a$};
\node at (8+5,1.5) {$b$};

\node at (8+3,-2) {$a \times b = 0$};

\draw[->,thick] (16+0,0)--(16+4,2);
\draw[->,thick] (16+4,2)--(16+4+2,2-1);

\node at (16+2.5,0.5) {$a$};
\node at (16+5,2.5) {$b$};

\node at (16+3,-2) {$a \times b = -8$};
\end{tikzpicture}
</script>

For example, in the first case
$a=(4,2)$ and $b=(1,2)$.
The following code calculates the cross product
using the point type `P` from the previous section:

```rust
# #[derive(Clone, Copy)] struct P { x: i64, y: i64 }
fn cross(a: P, b: P) -> i64 {
    a.x * b.y - a.y * b.x
}

let a = P { x: 4, y: 2 };
let b = P { x: 1, y: 2 };
assert_eq!(cross(a, b), 6);
```

This uses the formula directly. Equivalently, conjugating $a$
negates its y coordinate, and the imaginary part of the complex
product of $(x_1,-y_1)$ and $(x_2,y_2)$ is $x_1 y_2 - x_2 y_1$.

## Point location

Cross products can be used to test
whether a point is located on the left or right
side of a line.
Assume that the line goes through points
$s_1$ and $s_2$, we are looking from $s_1$
to $s_2$ and the point is $p$.

For example, in the following picture,
$p$ is on the left side of the line:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.45]
\draw[dashed,thick,->] (0,-3)--(12,6);
\draw[fill] (4,0) circle [radius=0.1];
\draw[fill] (8,3) circle [radius=0.1];
\draw[fill] (5,3) circle [radius=0.1];
\node at (4,-1) {$s_1$};
\node at (8,2) {$s_2$};
\node at (5,4) {$p$};
\end{tikzpicture}
</script>

The cross product $(p-s_1) \times (p-s_2)$
tells us the location of the point $p$.
If the cross product is positive,
$p$ is located on the left side,
and if the cross product is negative,
$p$ is located on the right side.
Finally, if the cross product is zero,
points $s_1$, $s_2$ and $p$ are on the same line.

## Line segment intersection

Next we consider the problem of testing
whether two line segments
$ab$ and $cd$ intersect. The possible cases are:

_Case 1:_
The line segments are on the same line
and they overlap each other.
In this case, there is an infinite number of
intersection points.
For example, in the following picture,
all points between $c$ and $b$ are
intersection points:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\draw (1.5,1.5)--(6,3);
\draw (0,1)--(4.5,2.5);
\draw[fill] (0,1) circle [radius=0.05];
\node at (0,0.5) {$a$};
\draw[fill] (1.5,1.5) circle [radius=0.05];
\node at (6,2.5) {$d$};
\draw[fill] (4.5,2.5) circle [radius=0.05];
\node at (1.5,1) {$c$};
\draw[fill] (6,3) circle [radius=0.05];
\node at (4.5,2) {$b$};
\end{tikzpicture}
</script>

In this case, we can use cross products to
check if all points are on the same line.
After this, we can sort the points and check
whether the line segments overlap each other.

_Case 2:_
The line segments have a common vertex
that is the only intersection point.
For example, in the following picture the
intersection point is $b=c$:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\draw (0,0)--(4,2);
\draw (4,2)--(6,1);
\draw[fill] (0,0) circle [radius=0.05];
\draw[fill] (4,2) circle [radius=0.05];
\draw[fill] (6,1) circle [radius=0.05];

\node at (0,0.5) {$a$};
\node at (4,2.5) {$b=c$};
\node at (6,1.5) {$d$};
\end{tikzpicture}
</script>

This case is easy to check, because
there are only four possibilities
for the intersection point:
$a=c$, $a=d$, $b=c$ and $b=d$.

_Case 3:_
There is exactly one intersection point
that is not a vertex of any line segment.
In the following picture, the point $p$
is the intersection point:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.9]
\draw (0,1)--(6,3);
\draw (2,4)--(4,0);
\draw[fill] (0,1) circle [radius=0.05];
\node at (0,0.5) {$c$};
\draw[fill] (6,3) circle [radius=0.05];
\node at (6,2.5) {$d$};
\draw[fill] (2,4) circle [radius=0.05];
\node at (1.5,3.5) {$a$};
\draw[fill] (4,0) circle [radius=0.05];
\node at (4,-0.4) {$b$};
\draw[fill] (3,2) circle [radius=0.05];
\node at (3,1.5) {$p$};
\end{tikzpicture}
</script>

In this case, the line segments intersect
exactly when both points $c$ and $d$ are
on different sides of a line through $a$ and $b$,
and points $a$ and $b$ are on different
sides of a line through $c$ and $d$.
We can use cross products to check this.

## Point distance from a line

Another feature of cross products is that
the area of a triangle can be calculated
using the formula
\\[
\\frac{| (a-c) \\times (b-c) |}{2},
\\]
where $a$, $b$ and $c$ are the vertices of the triangle.
Using this fact, we can derive a formula
for calculating the shortest distance between a point and a line.
For example, in the following picture $d$ is the
shortest distance between the point $p$ and the line
that is defined by the points $s_1$ and $s_2$:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.75]
\draw (-2,-1)--(6,3);
\draw[dashed] (1,4)--(2.40,1.2);
\node at (0,-0.5) {$s_1$};
\node at (4,1.5) {$s_2$};
\node at (0.5,4) {$p$};
\node at (2,2.7) {$d$};
\draw[fill] (0,0) circle [radius=0.05];
\draw[fill] (4,2) circle [radius=0.05];
\draw[fill] (1,4) circle [radius=0.05];
\end{tikzpicture}
</script>

The area of the triangle whose vertices are
$s_1$, $s_2$ and $p$ can be calculated in two ways:
it is both
$\frac{1}{2} |s_2-s_1| d$ and
$\frac{1}{2} |(s_1-p) \times (s_2-p)|$.
Thus, the shortest distance is
\\[
d = \\frac{|(s_1-p) \\times (s_2-p)|}{|s_2-s_1|} .
\\]

## Point inside a polygon

Let us now consider the problem of
testing whether a point is located inside or outside
a polygon.
For example, in the following picture point $a$
is inside the polygon and point $b$ is outside
the polygon.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.75]
%\draw (0,0)--(2,-2)--(3,1)--(5,1)--(2,3)--(1,2)--(-1,2)--(1,4)--(-2,4)--(-2,1)--(-3,3)--(-4,0)--(0,0);
\draw (0,0)--(2,2)--(5,1)--(2,3)--(1,2)--(-1,2)--(1,4)--(-2,4)--(-2,1)--(-3,3)--(-4,0)--(0,0);

\draw[fill] (-3,1) circle [radius=0.05];
\node at (-3,0.5) {$a$};
\draw[fill] (1,3) circle [radius=0.05];
\node at (1,2.5) {$b$};
\end{tikzpicture}
</script>

A convenient way to solve the problem is to
send a _ray_ from the point to an arbitrary direction
and calculate the number of times it touches
the boundary of the polygon.
If the number is odd,
the point is inside the polygon,
and if the number is even,
the point is outside the polygon.

For example, we could send the following rays:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.75]
\draw (0,0)--(2,2)--(5,1)--(2,3)--(1,2)--(-1,2)--(1,4)--(-2,4)--(-2,1)--(-3,3)--(-4,0)--(0,0);

\draw[fill] (-3,1) circle [radius=0.05];
\node at (-3,0.5) {$a$};
\draw[fill] (1,3) circle [radius=0.05];
\node at (1,2.5) {$b$};

\draw[dashed,->] (-3,1)--(-6,0);
\draw[dashed,->] (-3,1)--(0,5);

\draw[dashed,->] (1,3)--(3.5,0);
\draw[dashed,->] (1,3)--(3,4);
\end{tikzpicture}
</script>

The rays from $a$ touch 1 and 3 times
the boundary of the polygon,
so $a$ is inside the polygon.
Correspondingly, the rays from $b$
touch 0 and 2 times the boundary of the polygon,
so $b$ is outside the polygon.
