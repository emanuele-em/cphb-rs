# Events

An event in probability theory can be represented as a set
\\[
A \\subset X,
\\]
where $X$ contains all possible outcomes
and $A$ is a subset of outcomes.
For example, when drawing a dice, the outcomes are
\\[
X = \\{1,2,3,4,5,6\\}.
\\]
Now, for example, the event ''the outcome is even''
corresponds to the set
\\[
A = \\{2,4,6\\}.
\\]

Each outcome $x$ is assigned a probability $p(x)$.
Then, the probability $P(A)$ of an event
$A$ can be calculated as a sum
of probabilities of outcomes using the formula
\\[
P(A) = \\sum_{x \\in A} p(x).
\\]
For example, when throwing a dice,
$p(x)=1/6$ for each outcome $x$,
so the probability of the event
''the outcome is even'' is
\\[
p(2)+p(4)+p(6)=1/2.
\\]

The total probability of the outcomes in $X$ must
be 1, i.e., $P(X)=1$.

Since the events in probability theory are sets,
we can manipulate them using standard set operations:
- The **complement** $\bar A$ means
''$A$ does not happen''.
For example, when throwing a dice, 
the complement of $A=\\{2,4,6\\}$ is
$\bar A = \\{1,3,5\\}$.
- The **union** $A \cup B$ means
''$A$ or $B$ happen''.
For example, the union of
$A=\\{2,5\\}$
and $B=\\{4,5,6\\}$ is
$A \cup B = \\{2,4,5,6\\}$.
- The **intersection** $A \cap B$ means
''$A$ and $B$ happen''.
For example, the intersection of
$A=\\{2,5\\}$ and $B=\\{4,5,6\\}$ is
$A \cap B = \\{5\\}$.

## Complement

The probability of the complement
$\bar A$ is calculated using the formula
\\[
P(\\bar A)=1-P(A).
\\]

Sometimes, we can solve a problem easily
using complements by solving the opposite problem.
For example, the probability of getting
at least one six when throwing a dice ten times is
\\[
1-(5/6)^{10}.
\\]

Here $5/6$ is the probability that the outcome
of a single throw is not six, and
$(5/6)^{10}$ is the probability that none of
the ten throws is a six.
The complement of this is the answer to the problem.

## Union

The probability of the union $A \cup B$
is calculated using the formula
\\[
P(A \\cup B)=P(A)+P(B)-P(A \\cap B).
\\]
For example, when throwing a dice,
the union of the events
\\[
A=\\textrm{''the outcome is even''}
\\]
and
\\[
B=\\textrm{''the outcome is less than 4''}
\\]
is
\\[
A \\cup B=\\textrm{''the outcome is even or less than 4''},
\\]
and its probability is
\\[
P(A \\cup B) = P(A)+P(B)-P(A \\cap B)=1/2+1/2-1/6=5/6.
\\]

If the events $A$ and $B$ are **disjoint**, i.e.,
$A \cap B$ is empty,
the probability of the event $A \cup B$ is simply

\\[
P(A \\cup B)=P(A)+P(B).
\\]

## Conditional probability

The **conditional probability**
\\[
P(A | B) = \\frac{P(A \\cap B)}{P(B)}
\\]
is the probability of $A$
assuming that $B$ happens.
Hence, when calculating the
probability of $A$, we only consider the outcomes
that also belong to $B$.

Using the previous sets,
\\[
P(A | B)= 1/3,
\\]
because the outcomes of $B$ are
$\\{1,2,3\\}$, and one of them is even.
This is the probability of an even outcome
if we know that the outcome is between $1 \ldots 3$.

## Intersection

Using conditional probability,
the probability of the intersection
$A \cap B$ can be calculated using the formula
\\[
P(A \\cap B)=P(A)P(B|A).
\\]
Events $A$ and $B$ are **independent** if
\\[
P(A|B)=P(A) \\hspace{10px}\\textrm{and}\\hspace{10px} P(B|A)=P(B),
\\]
which means that the fact that $B$ happens does not
change the probability of $A$, and vice versa.
In this case, the probability of the intersection is
\\[
P(A \\cap B)=P(A)P(B).
\\]
For example, when drawing a card from a deck, the events
\\[
A = \\textrm{''the suit is clubs''}
\\]
and
\\[
B = \\textrm{''the value is four''}
\\]
are independent. Hence the event
\\[
A \\cap B = \\textrm{''the card is the four of clubs''}
\\]
happens with probability
\\[
P(A \\cap B)=P(A)P(B)=1/4 \\cdot 1/13 = 1/52.
\\]
