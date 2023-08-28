# Mathematics

Mathematics plays an important role in competitive programming, and it is not possible to become a successful competitive programmer without having good mathematical skills.
This section discusses some important mathematical concepts and formulas that are needed later in the book.

## Sum formula

Each sum of the form

$$
\sum_{x=1}^n x^k = 1^k + 2^k+3^k+...+m^k,
$$

where $k$ is a positive integer, has a closed-form formula that is a polynomial of degree $k + 1$. For example[^1],

$$
    \sum_{x=1}^n x = 1 + 2 + 3 + ... + n = \frac{n(n+1)}{2}
$$
and
$$
    \sum_{x=1}^n x^2 = 1^2 + 2^2 + 3^2 + ... + n^2 = \frac{n(n+1)(2n+1)}{6}
$$

### Arithmetic progression

An **arithmetic progression** An arithmetic progression is a sequence of numbers where the difference between any two consecutive numbers is constant.
For example:
$$
3, 7, 11, 15
$$
is an arithmetic progression with constant 4. The sum of an arithmetic progression can be calculated using the formula
$$
\underbrace{a + \cdots + b}_{n \,\, \textrm{numbers}} = \frac{n(a+b)}{2}
$$

where a is the first number, b is the last number and n is the amount of numbers.
For example,
$$
3+7+11+15=\frac{4 \cdot (3+15)}{2} = 36
$$

The formula is based on the fact that the sum consists of $n$ numbers and the value of each number is $(a+b)/2$ on average.

### Geometric progression

A **geometric progression** is a sequence of numbers where the ratio between any two consecutive numbers is constant.
For example,
$$
3,6,12,24
$$
is a geometric progression with constant 2.
The sum of a geometric progression can be calculated using the formula
$$
a + ak + ak^2 + \cdots + b = \frac{bk-a}{k-1}
$$
where $a$ is the first number, $b$ is the last number and the ratio between consecutive numbers is $k$.
For example,
$$
3+6+12+24=\frac{24 \cdot 2 - 3}{2-1} = 45
$$
This formula can be derived as follows. Let
$$
S = a + ak + ak^2 + \cdots + b
$$
By multiplying both sides by $k$, we get
$$
kS = ak + ak^2 + ak^3 + \cdots + bk
$$
and solving the equation
$$
kS-S = bk-a
$$
yields the formula.

A special case of a sum of a geometric progression is the formula
$$
1+2+4+8+\ldots+2^{n-1}=2^n-1
$$

### Harmonic sum

A \key{harmonic sum} is a sum of the form
$$
\sum_{x=1}^n \frac{1}{x} = 1+\frac{1}{2}+\frac{1}{3}+\ldots+\frac{1}{n}
$$
An upper bound for a harmonic sum is $\log_2(n)+1$.
Namely, we can modify each term $1/k$ so that $k$ becomes the nearest power of two that does not exceed $k$.
For example, when $n=6$, we can estimate the sum as follows:
$$
1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\frac{1}{5}+\frac{1}{6} \le 1+\frac{1}{2}+\frac{1}{2}+\frac{1}{4}+\frac{1}{4}+\frac{1}{4}
$$
This upper bound consists of $\log_2(n)+1$ parts ($1$, $2 \cdot 1/2$, $4 \cdot 1/4$, etc.), and the value of each part is at most 1.

## Set theory

 A **set** is a collection of elements.
For example, the set
$$
X=\{2,4,7\}
$$
contains elements 2, 4 and 7.
The symbol $\emptyset$ denotes an empty set, and $|S|$ denotes the size of a set $S$, i.e., the number of elements in the set.
For example, in the above set, $|X|=3$.
If a set $S$ contains an element $x$, we write $x \in S$, and otherwise we write $x \notin S$.
For example, in the above set
$$
4 \in X \hspace{10px}\textrm{and}\hspace{10px} 5 \notin X
$$
New sets can be constructed using set operations:
- The \key{intersection} $A \cap B$ consists of elements that are in both $A$ and $B$. For example, if $A=\{1,2,5\}$ and $B=\{2,4\}$, then $A \cap B = \{2\}$.
- The \key{union} $A \cup B$ consists of elements that are in $A$ or $B$ or both. For example, if $A=\{3,7\}$ and $B=\{2,3,8\}$, then $A \cup B = \{2,3,7,8\}$.
- The \key{complement} $\bar A$ consists of elements that are not in $A$. The interpretation of a complement depends on the \key{universal set}, which contains all possible elements. For example, if $A=\{1,2,5,7\}$ and the universal set is $\{1,2,\ldots,10\}$, then $\bar A = \{3,4,6,8,9,10\}$.
- The \key{difference} $A \setminus B = A \cap \bar B$ consists of elements that are in $A$ but not in $B$. Note that $B$ can contain elements that are not in $A$. For example, if $A=\{2,3,7,8\}$ and $B=\{3,5,8\}$, then $A \setminus B = \{2,7\}$.

If each element of $A$ also belongs to $S$, we say that $A$ is a \key{subset} of $S$, denoted by $A \subset S$.
A set $S$ always has $2^{|S|}$ subsets, including the empty set.
For example, the subsets of the set $\{2,4,7\}$ are
$$
\emptyset, \{2\}, \{4\}, \{7\}, \{2,4\}, \{2,7\}, \{4,7\}, \{2,4,7\}
$$

Some often used sets are $\mathbb{N}$ (natural numbers), $\mathbb{Z}$ (integers), $\mathbb{Q}$ (rational numbers) and $\mathbb{R}$ (real numbers).
The set $\mathbb{N}$ can be defined in two ways, depending on the situation:
either $\mathbb{N}=\{0,1,2,\ldots\}$ or $\mathbb{N}=\{1,2,3,.\ldots\}$ .

We can also construct a set using a rule of the form
$$
\{f(n) : n \in S\}
$$
where $f(n)$ is some function.
This set contains all elements of the form $f(n)$, where $n$ is an element in $S$.

For example, the set
$$
X=\{2n : n \in \mathbb{Z}\}
$$
contains all even integers.

## Logic
The value of a logical expression is either **true** (1) or **false** (0).
The most important logical operators are $\lnot$ (\key{negation}), $\land$ (\key{conjunction}), $\lor$ (\key{disjunction}), $\Rightarrow$ (\key{implication}) and $\Leftrightarrow$ (\key{equivalence}).
The following table shows the meanings of these operators:

| $A$ | $B$ | $\lnot A$ | $\lnot B$ | $A \land B$ | $A \lor B$ | $A \Rightarrow B$ | $A \Leftrightarrow B$ |
| - | - | - | - | - | - | - | - |
| 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |

The expression $\lnot A$ has the opposite value of $A$.
The expression $A \land B$ is true if both $A$ and $B$ are true, and the expression $A \lor B$ is true if $A$ or $B$ or both are true.
The expression $A \Rightarrow B$ is true if whenever $A$ is true, also $B$ is true.
The expression $A \Leftrightarrow B$ is true if $A$ and $B$ are both true or both false.

### Predicate

A **predicate** is an expression that is true or false depending on its parameters.
Predicates are usually denoted by capital letters.
For example, we can define a predicate $P(x)$ that is true exactly when $x$ is a prime number.
Using this definition, $P(7)$ is true but $P(8)$ is false.

### Quantifier

A **quantifier** connects a logical expression to the elements of a set.
The most important quantifiers are $\forall$ (\key{for all}) and $\exists$ (\key{there is}).
For example,
$$
\forall x (\exists y (y < x))
$$
means that for each element $x$ in the set, there is an element $y$ in the set such that $y$ is smaller than $x$.
This is true in the set of integers, but false in the set of natural numbers.

Using the notation described above, we can express many kinds of logical propositions.
For example,
$$
\forall x ((x>1 \land \lnot P(x)) \Rightarrow (\exists a (\exists b (a > 1 \land b > 1 \land x = ab))))
$$
means that if a number $x$ is larger than 1 and not a prime number, then there are numbers $a$ and $b$ that are larger than $1$ and whose product is $x$.
This proposition is true in the set of integers.

## Functions

The function $\lfloor x \rfloor$ rounds the number $x$
down to an integer, and the function
$\lceil x \rceil$ rounds the number $x$
up to an integer. For example,
$$
\lfloor 3/2 \rfloor = 1 \hspace{10px} \textrm{and} \hspace{10px} \lceil 3/2 \rceil = 2
$$

The functions $\min(x_1,x_2,\ldots,x_n)$ and $\max(x_1,x_2,\ldots,x_n)$ give the smallest and largest of values $x_1,x_2,\ldots,x_n$.
For example,
$$
\min(1,2,3)=1 \hspace{10px} \textrm{and} \hspace{10px} \max(1,2,3)=3
$$

### Factorial

The \key{factorial} $n!$ can be defined
$$
\prod_{x=1}^n x = 1 \cdot 2 \cdot 3 \cdot \ldots \cdot n
$$
or recursively
$$
\begin{array}{lcl}
0! & = & 1 \\
n! & = & n \cdot (n-1)! \\
\end{array}
$$

### Fibonacci

The **Fibonacci numbers**[^2] 
arise in many situations.
They can be defined recursively as follows:
$$
\begin{array}{lcl}
f(0) & = & 0 \\
f(1) & = & 1 \\
f(n) & = & f(n-1)+f(n-2) \\
\end{array}
$$
The first Fibonacci numbers are
$$
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \ldots
$$
There is also a closed-form formula for calculating Fibonacci numbers, which is sometimes called **Binet's formula**:
$$
f(n)=\frac{(1 + \sqrt{5})^n - (1-\sqrt{5})^n}{2^n \sqrt{5}}
$$

## Logarithms

The \key{logarithm} of a number $x$ is denoted $\log_k(x)$, where $k$ is the base of the logarithm.
According to the definition, $\log_k(x)=a$ exactly when $k^a=x$.

A useful property of logarithms is that $\log_k(x)$ equals the number of times we have to divide $x$ by $k$ before we reach the number 1.
For example, $\log_2(32)=5$ because 5 divisions by 2 are needed:

$$
32 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1
$$

Logarithms are often used in the analysis of algorithms, because many efficient algorithms halve something at each step.
Hence, we can estimate the efficiency of such algorithms using logarithms.

The logarithm of a product is
$$
\log_k(ab) = \log_k(a)+\log_k(b
$$
and consequently,
$$
\log_k(x^n) = n \cdot \log_k(x)
$$
In addition, the logarithm of a quotient is
$$
\log_k\Big(\frac{a}{b}\Big) = \log_k(a)-\log_k(b)
$$
Another useful formula is
$$
\log_u(x) = \frac{\log_k(x)}{\log_k(u)}
$$
and using this, it is possible to calculate logarithms to any base if there is a way to calculate logarithms to some fixed base.

### Natural logarithm

The **natural logarithm** $\ln(x)$ of a number $x$ is a logarithm whose base is $e \approx 2.71828$.
Another property of logarithms is that the number of digits of an integer $x$ in base $b$ is $\lfloor \log_b(x)+1 \rfloor$.
For example, the representation of $123$ in base $2$ is $1111011$ and $\lfloor \log_2(123)+1 \rfloor = 7$.

___

[^1] There is even a general formula for such sums, called Faulhaber’s formula, but it is too
complex to be presented here.

[^2] Fibonacci (c. 1175--1250) was an Italian mathematician.
