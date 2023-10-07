# Edit distance

The **edit distance** or **Levenshtein distance** [^1]
is the minimum number of editing operations
needed to transform a string
into another string.
The allowed editing operations are as follows:

- insert a character (e.g. ABC $\rightarrow$ ABCA)
- remove a character (e.g. ABC $\rightarrow$ AC)
- modify a character (e.g. ABC $\rightarrow$ ADC)

For example, the edit distance between
LOVE and MOVIE is 2,
because we can first perform the operation
 LOVE $\rightarrow$ MOVE
(modify) and then the operation
MOVE $\rightarrow$ MOVIE
(insert).
This is the smallest possible number of operations,
because it is clear that only one operation is not enough.

Suppose that we are given a string `x`
of length `n` and a string `y` of length `m`,
and we want to calculate the edit distance between
`x` and `y`.
To solve the problem, we define a function
`distance}(a,b)` that gives the
edit distance between prefixes
`x[0..a]` and `y[0..b]`.
Thus, using this function, the edit distance
between `x` and `y` equals `distance(n-1,m-1)`.

We can calculate values of \texttt{distance}
as follows:
\\begin{equation*}
\\begin{split}
\\texttt{distance}(a,b) = \\min(& \\texttt{distance}(a,b-1)+1, \\\\
                           & \\texttt{distance}(a-1,b)+1, \\\\
                           & \\texttt{distance}(a-1,b-1)+\\texttt{cost}(a,b)).
\\end{split}
\\end{equation*}

Here $\texttt{cost}(a,b)=0$ if $\texttt{x}[a]=\texttt{y}[b]$,
and otherwise $\texttt{cost}(a,b)=1$.
The formula considers the following ways to
edit the string $\texttt{x}$:

- $\texttt{distance}(a,b-1)$: insert a character at the end of $\texttt{x}$
- $\texttt{distance}(a-1,b)$: remove the last character from $\texttt{x}$
- $\texttt{distance}(a-1,b-1)$: match or modify the last character of $\texttt{x}$

In the two first cases, one editing operation is needed
(insert or remove).

In the last case, if $\texttt{x}[a]=\texttt{y}[b]$, we can match the last characters without editing,
and otherwise one editing operation is needed (modify).

The following table shows the values of \texttt{distance}
in the example case:

<script type="text/tikz">
\begin{tikzpicture}[scale=.65]
  \begin{scope}
    %\fill [color=lightgray] (5, -3) rectangle (6, -4);
    \draw (1, -1) grid (7, -6);
    
    \node at (0.5,-2.5) {\texttt{L}};
    \node at (0.5,-3.5) {\texttt{O}};
    \node at (0.5,-4.5) {\texttt{V}};
    \node at (0.5,-5.5) {\texttt{E}};

    \node at (2.5,-0.5) {\texttt{M}};
    \node at (3.5,-0.5) {\texttt{O}};
    \node at (4.5,-0.5) {\texttt{V}};
    \node at (5.5,-0.5) {\texttt{I}};
    \node at (6.5,-0.5) {\texttt{E}};

    \node at (1.5,-1.5) {0};
    \node at (1.5,-2.5) {1};
    \node at (1.5,-3.5) {2};
    \node at (1.5,-4.5) {3};
    \node at (1.5,-5.5) {4};
    \node at (2.5,-1.5) {1};
    \node at (2.5,-2.5) {1};
    \node at (2.5,-3.5) {2};
    \node at (2.5,-4.5) {3};
    \node at (2.5,-5.5) {4};
    \node at (3.5,-1.5) {2};
    \node at (3.5,-2.5) {2};
    \node at (3.5,-3.5) {1};
    \node at (3.5,-4.5) {2};
    \node at (3.5,-5.5) {3};
    \node at (4.5,-1.5) {3};
    \node at (4.5,-2.5) {3};
    \node at (4.5,-3.5) {2};
    \node at (4.5,-4.5) {1};
    \node at (4.5,-5.5) {2};
    \node at (5.5,-1.5) {4};
    \node at (5.5,-2.5) {4};
    \node at (5.5,-3.5) {3};
    \node at (5.5,-4.5) {2};
    \node at (5.5,-5.5) {2};
    \node at (6.5,-1.5) {5};
    \node at (6.5,-2.5) {5};
    \node at (6.5,-3.5) {4};
    \node at (6.5,-4.5) {3};
    \node at (6.5,-5.5) {2};
  \end{scope}
\end{tikzpicture}
</script>

The lower-right corner of the table
tells us that the edit distance between
**LOVE** and **MOVIE** is 2.
The table also shows how to construct
the shortest sequence of editing operations.
In this case the path is as follows:

<script type="text/tikz">
\begin{tikzpicture}[scale=.65]
  \begin{scope}
    \draw (1, -1) grid (7, -6);
    
    \node at (0.5,-2.5) {\texttt{L}};
    \node at (0.5,-3.5) {\texttt{O}};
    \node at (0.5,-4.5) {\texttt{V}};
    \node at (0.5,-5.5) {\texttt{E}};

    \node at (2.5,-0.5) {\texttt{M}};
    \node at (3.5,-0.5) {\texttt{O}};
    \node at (4.5,-0.5) {\texttt{V}};
    \node at (5.5,-0.5) {\texttt{I}};
    \node at (6.5,-0.5) {\texttt{E}};

    \node at (1.5,-1.5) {0};
    \node at (1.5,-2.5) {1};
    \node at (1.5,-3.5) {2};
    \node at (1.5,-4.5) {3};
    \node at (1.5,-5.5) {4};
    \node at (2.5,-1.5) {1};
    \node at (2.5,-2.5) {1};
    \node at (2.5,-3.5) {2};
    \node at (2.5,-4.5) {3};
    \node at (2.5,-5.5) {4};
    \node at (3.5,-1.5) {2};
    \node at (3.5,-2.5) {2};
    \node at (3.5,-3.5) {1};
    \node at (3.5,-4.5) {2};
    \node at (3.5,-5.5) {3};
    \node at (4.5,-1.5) {3};
    \node at (4.5,-2.5) {3};
    \node at (4.5,-3.5) {2};
    \node at (4.5,-4.5) {1};
    \node at (4.5,-5.5) {2};
    \node at (5.5,-1.5) {4};
    \node at (5.5,-2.5) {4};
    \node at (5.5,-3.5) {3};
    \node at (5.5,-4.5) {2};
    \node at (5.5,-5.5) {2};
    \node at (6.5,-1.5) {5};
    \node at (6.5,-2.5) {5};
    \node at (6.5,-3.5) {4};
    \node at (6.5,-4.5) {3};
    \node at (6.5,-5.5) {2};

    \path[draw=red,thick,-,line width=2pt] (6.5,-5.5) -- (5.5,-4.5);
    \path[draw=red,thick,-,line width=2pt] (5.5,-4.5) -- (4.5,-4.5);
    \path[draw=red,thick,->,line width=2pt] (4.5,-4.5) -- (1.5,-1.5);
  \end{scope}
\end{tikzpicture}
</script>

The last characters of **LOVE** and **MOVIE**
are equal, so the edit distance between them
equals the edit distance between **LOV** and **MOVI**.
We can use one editing operation to remove the
character I from **MOVI**.
Thus, the edit distance is one larger than
the edit distance between **LOV** and **MOV**, etc.

___

[^1] The distance is named after V. I. Levenshtein who studied it in connection with binary codes [49].
