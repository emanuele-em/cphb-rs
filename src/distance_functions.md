# Distance functions

A **distance function** defines the distance between
two points.
The usual distance function is the
**Euclidean distance** where the distance between
points $(x_1,y_1)$ and $(x_2,y_2)$ is
\\[
\\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}.
\\]
An alternative distance function is the
**Manhattan distance**
where the distance between points
$(x_1,y_1)$ and $(x_2,y_2)$ is
\\[
|x_1-x_2|+|y_1-y_2|.
\\]

For example, consider the following picture:

<script type="text/tikz">
\begin{tikzpicture}

\draw[fill] (2,1) circle [radius=0.05];
\draw[fill] (5,2) circle [radius=0.05];

\node at (2,0.5) {$(2,1)$};
\node at (5,1.5) {$(5,2)$};

\draw[dashed] (2,1) -- (5,2);

\draw[fill] (5+2,1) circle [radius=0.05];
\draw[fill] (5+5,2) circle [radius=0.05];

\node at (5+2,0.5) {$(2,1)$};
\node at (5+5,1.5) {$(5,2)$};

\draw[dashed] (5+2,1) -- (5+2,2);
\draw[dashed] (5+2,2) -- (5+5,2);

\node at (3.5,-0.5) {Euclidean distance};
\node at (5+3.5,-0.5) {Manhattan distance};
\end{tikzpicture}
</script>

The Euclidean distance between the points is
\\[
\\sqrt{(5-2)^2+(2-1)^2}=\\sqrt{10}
\\]
and the Manhattan distance is
\\[
|5-2|+|2-1|=4.
\\]
The following picture shows regions that are within a distance of 1
from the center point, using the Euclidean and Manhattan distances:

<script type="text/tikz">
\begin{tikzpicture}

\draw[fill=gray!20] (0,0) circle [radius=1];
\draw[fill] (0,0) circle [radius=0.05];

\node at (0,-1.5) {Euclidean distance};

\draw[fill=gray!20] (5+0,1) -- (5-1,0) -- (5+0,-1) -- (5+1,0) -- (5+0,1);
\draw[fill] (5,0) circle [radius=0.05];
\node at (5,-1.5) {Manhattan distance};
\end{tikzpicture}
</script>

## Rotating coordinates

Some problems are easier to solve if
Manhattan distances are used instead of Euclidean distances.
As an example, consider a problem where we are given
$n$ points in the two-dimensional plane
and our task is to calculate the maximum Manhattan
distance between any two points.

For example, consider the following set of points:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.65]
\draw[color=gray] (-1,-1) grid (4,4);

\filldraw (0,2) circle (2.5pt);
\filldraw (3,3) circle (2.5pt);
\filldraw (1,0) circle (2.5pt);
\filldraw (3,1) circle (2.5pt);

\node at (0,1.5) {$A$};
\node at (3,2.5) {$C$};
\node at (1,-0.5) {$B$};
\node at (3,0.5) {$D$};
\end{tikzpicture}
</script>

The maximum Manhattan distance is 5
between points $B$ and $C$:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.65]
\draw[color=gray] (-1,-1) grid (4,4);

\filldraw (0,2) circle (2.5pt);
\filldraw (3,3) circle (2.5pt);
\filldraw (1,0) circle (2.5pt);
\filldraw (3,1) circle (2.5pt);

\node at (0,1.5) {$A$};
\node at (3,2.5) {$C$};
\node at (1,-0.5) {$B$};
\node at (3,0.5) {$D$};

\path[draw=red,thick,line width=2pt] (1,0) -- (1,3) -- (3,3);
\end{tikzpicture}
</script>

A useful technique related to Manhattan distances
is to rotate all coordinates 45 degrees so that
a point $(x,y)$ becomes $(x+y,y-x)$.
For example, after rotating the above points,
the result is:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.6]
\draw[color=gray] (0,-3) grid (7,3);

\filldraw (2,2) circle (2.5pt);
\filldraw (6,0) circle (2.5pt);
\filldraw (1,-1) circle (2.5pt);
\filldraw (4,-2) circle (2.5pt);

\node at (2,1.5) {$A$};
\node at (6,-0.5) {$C$};
\node at (1,-1.5) {$B$};
\node at (4,-2.5) {$D$};
\end{tikzpicture}
</script>

And the maximum distance is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.6]
\draw[color=gray] (0,-3) grid (7,3);

\filldraw (2,2) circle (2.5pt);
\filldraw (6,0) circle (2.5pt);
\filldraw (1,-1) circle (2.5pt);
\filldraw (4,-2) circle (2.5pt);

\node at (2,1.5) {$A$};
\node at (6,-0.5) {$C$};
\node at (1,-1.5) {$B$};
\node at (4,-2.5) {$D$};

\path[draw=red,thick,line width=2pt] (1,-1) -- (4,2) -- (6,0);
\end{tikzpicture}
</script>

Consider two points $p_1=(x_1,y_1)$ and $p_2=(x_2,y_2)$ whose rotated
coordinates are $p'_1=(x'_1,y'_1)$ and $p'_2=(x'_2,y'_2)$.
Now there are two ways to express the Manhattan distance
between $p_1$ and $p_2$:
\\[
|x_1-x_2|+|y_1-y_2| = \\max(|x'_1-x'_2|,|y'_1-y'_2|)
\\]

For example, if $p_1=(1,0)$ and $p_2=(3,3)$,
the rotated coordinates are $p'_1=(1,-1)$ and $p'_2=(6,0)$
and the Manhattan distance is
\\[
|1-3|+|0-3| = \\max(|1-6|,|-1-0|) = 5.
\\]

The rotated coordinates provide a simple way
to operate with Manhattan distances, because we can
consider x and y coordinates separately.
To maximize the Manhattan distance between two points,
we should find two points whose
rotated coordinates maximize the value of
\\[
\\max(|x'_1-x'_2|,|y'_1-y'_2|).
\\]
This is easy, because either the horizontal or vertical
difference of the rotated coordinates has to be maximum.
