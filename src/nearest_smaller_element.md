# Nearest smaller elements

Amortized analysis is often used to
estimate the number of operations
performed on a data structure.
The operations may be distributed unevenly so
that most operations occur during a
certain phase of the algorithm, but the total
number of the operations is limited.

As an example, consider the problem
of finding for each array element
the nearest smaller element, i.e.,
the first smaller element that precedes the element
in the array.
It is possible that no such element exists,
in which case the algorithm should report this.
Next we will see how the problem can be
efficiently solved using a stack structure.

We go through the array from left to right
and maintain a stack of array elements.
At each array position, we remove elements from the stack
until the top element is smaller than the
current element, or the stack is empty.
Then, we report that the top element is
the nearest smaller element of the current element,
or if the stack is empty, there is no such element.
Finally, we add the current element to the stack.

As an example, consider the following array:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {2};
\node at (4.5,0.5) {5};
\node at (5.5,0.5) {3};
\node at (6.5,0.5) {4};
\node at (7.5,0.5) {2};
\end{tikzpicture}
</script>

First, the elements 1, 3 and 4 are added to the stack,
because each element is larger than the previous element.
Thus, the nearest smaller element of 4 is 3,
and the nearest smaller element of 3 is 1.

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (2,0) rectangle (3,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {2};
\node at (4.5,0.5) {5};
\node at (5.5,0.5) {3};
\node at (6.5,0.5) {4};
\node at (7.5,0.5) {2};

\draw (0.2,0.2-1.2) rectangle (0.8,0.8-1.2);
\draw (1.2,0.2-1.2) rectangle (1.8,0.8-1.2);
\draw (2.2,0.2-1.2) rectangle (2.8,0.8-1.2);

\node at (0.5,0.5-1.2) {1};
\node at (1.5,0.5-1.2) {3};
\node at (2.5,0.5-1.2) {4};

\draw[->,thick] (0.8,0.5-1.2) -- (1.2,0.5-1.2);
\draw[->,thick] (1.8,0.5-1.2) -- (2.2,0.5-1.2);
\end{tikzpicture}
</script>

The next element 2 is smaller than the two top
elements in the stack.
Thus, the elements 3 and 4 are removed from the stack,
and then the element 2 is added to the stack.
Its nearest smaller element is 1:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (3,0) rectangle (4,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {2};
\node at (4.5,0.5) {5};
\node at (5.5,0.5) {3};
\node at (6.5,0.5) {4};
\node at (7.5,0.5) {2};

\draw (0.2,0.2-1.2) rectangle (0.8,0.8-1.2);
\draw (3.2,0.2-1.2) rectangle (3.8,0.8-1.2);

\node at (0.5,0.5-1.2) {1};
\node at (3.5,0.5-1.2) {2};

\draw[->,thick] (0.8,0.5-1.2) -- (3.2,0.5-1.2);
\end{tikzpicture}
</script>

Then, the element 5 is larger than the element 2,
so it will be added to the stack, and
its nearest smaller element is 2:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (4,0) rectangle (5,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {2};
\node at (4.5,0.5) {5};
\node at (5.5,0.5) {3};
\node at (6.5,0.5) {4};
\node at (7.5,0.5) {2};

\draw (0.2,0.2-1.2) rectangle (0.8,0.8-1.2);
\draw (3.2,0.2-1.2) rectangle (3.8,0.8-1.2);
\draw (4.2,0.2-1.2) rectangle (4.8,0.8-1.2);

\node at (0.5,0.5-1.2) {1};
\node at (3.5,0.5-1.2) {2};
\node at (4.5,0.5-1.2) {5};

\draw[->,thick] (0.8,0.5-1.2) -- (3.2,0.5-1.2);
\draw[->,thick] (3.8,0.5-1.2) -- (4.2,0.5-1.2);
\end{tikzpicture}
</script>

After this, the element 5 is removed from the stack
and the elements 3 and 4 are added to the stack:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (6,0) rectangle (7,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {2};
\node at (4.5,0.5) {5};
\node at (5.5,0.5) {3};
\node at (6.5,0.5) {4};
\node at (7.5,0.5) {2};

\draw (0.2,0.2-1.2) rectangle (0.8,0.8-1.2);
\draw (3.2,0.2-1.2) rectangle (3.8,0.8-1.2);
\draw (5.2,0.2-1.2) rectangle (5.8,0.8-1.2);
\draw (6.2,0.2-1.2) rectangle (6.8,0.8-1.2);

\node at (0.5,0.5-1.2) {1};
\node at (3.5,0.5-1.2) {2};
\node at (5.5,0.5-1.2) {3};
\node at (6.5,0.5-1.2) {4};

\draw[->,thick] (0.8,0.5-1.2) -- (3.2,0.5-1.2);
\draw[->,thick] (3.8,0.5-1.2) -- (5.2,0.5-1.2);
\draw[->,thick] (5.8,0.5-1.2) -- (6.2,0.5-1.2);
\end{tikzpicture}
</script>

Finally, all elements except 1 are removed
from the stack and the last element 2
is added to the stack:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.7]
\fill[color=lightgray] (7,0) rectangle (8,1);
\draw (0,0) grid (8,1);

\node at (0.5,0.5) {1};
\node at (1.5,0.5) {3};
\node at (2.5,0.5) {4};
\node at (3.5,0.5) {2};
\node at (4.5,0.5) {5};
\node at (5.5,0.5) {3};
\node at (6.5,0.5) {4};
\node at (7.5,0.5) {2};

\draw (0.2,0.2-1.2) rectangle (0.8,0.8-1.2);
\draw (7.2,0.2-1.2) rectangle (7.8,0.8-1.2);

\node at (0.5,0.5-1.2) {1};
\node at (7.5,0.5-1.2) {2};

\draw[->,thick] (0.8,0.5-1.2) -- (7.2,0.5-1.2);
\end{tikzpicture}
</script>

The efficiency of the algorithm depends on
the total number of stack operations.
If the current element is larger than
the top element in the stack, it is directly
added to the stack, which is efficient.
However, sometimes the stack can contain several
larger elements and it takes time to remove them.
Still, each element is added _exactly once_ to the stack
and removed _at most once_ from the stack.
Thus, each element causes $O(1)$ stack operations,
and the algorithm works in $O(n)$ time.
