# Complex numbers

A **complex number** is a number of the form $x+y i$,
where $i = \sqrt{-1}$ is the **imaginary unit**.
A geometric interpretation of a complex number is
that it represents a two-dimensional point $(x,y)$
or a vector from the origin to a point $(x,y)$.

For example, $4+2i$ corresponds to the
following point and vector:

<script type="text/tikz">
\begin{tikzpicture}[scale=0.45]

\draw[->,thick] (-5,0)--(5,0);
\draw[->,thick] (0,-5)--(0,5);

\draw[fill] (4,2) circle [radius=0.1];
\draw[->,thick] (0,0)--(4-0.1,2-0.1);

\node at (4,2.8) {$(4,2)$};
\end{tikzpicture}
</script>

C++ solves geometric problems with its `complex` class, which gives
points and vectors arithmetic for free. Rust has no complex type in its
standard library and no external crates are available here, so we define
a small point type instead and implement the operators we need. Keeping
the coordinates integral avoids rounding entirely, which is worth doing
whenever the problem allows it.

In the following code, `i64` is the type of
a coordinate and `P` is the type of a point or a vector.
The fields `x` and `y` hold its coordinates.

```rust
use std::ops::{Add, Sub, Mul};

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
struct P { x: i64, y: i64 }

impl Add for P { type Output = P;
    fn add(self, o: P) -> P { P { x: self.x + o.x, y: self.y + o.y } } }
impl Sub for P { type Output = P;
    fn sub(self, o: P) -> P { P { x: self.x - o.x, y: self.y - o.y } } }
// multiplication follows the complex rule, which is what makes
// rotations and the cross product fall out naturally
impl Mul for P { type Output = P;
    fn mul(self, o: P) -> P {
        P { x: self.x * o.x - self.y * o.y,
            y: self.x * o.y + self.y * o.x }
    } }
# let p = P { x: 4, y: 2 };
# println!("{:?}", p);
```

For example, the following code defines a point $p=(4,2)$
and prints its x and y coordinates:

```rust
# #[derive(Clone, Copy, Debug)] struct P { x: i64, y: i64 }
let p = P { x: 4, y: 2 };
println!("{} {}", p.x, p.y); // 4 2
```

The following code defines vectors $v=(3,1)$ and $u=(2,2)$,
and after that calculates the sum $s=v+u$.

```rust
# use std::ops::Add;
# #[derive(Clone, Copy, Debug)] struct P { x: i64, y: i64 }
# impl Add for P { type Output = P;
#     fn add(self, o: P) -> P { P { x: self.x+o.x, y: self.y+o.y } } }
let v = P { x: 3, y: 1 };
let u = P { x: 2, y: 2 };
let s = v + u;
println!("{} {}", s.x, s.y); // 5 3
```

In practice,
an appropriate coordinate type is usually
`i64` (integer) or `f64`
(real number).
It is a good idea to use integer whenever possible,
because calculations with integers are exact.
If real numbers are needed,
precision errors should be taken into account
when comparing numbers.
A safe way to check if real numbers $a$ and $b$ are equal
is to compare them using $|a-b|<\epsilon$,
where $\epsilon$ is a small number (for example, $\epsilon=10^{-9}$).

## Functions

In the following examples, the coordinate type is
`f64`.

The function $\texttt{abs}(v)$ calculates the length
$|v|$ of a vector $v=(x,y)$
using the formula $\sqrt{x^2+y^2}$.
The function can also be used for
calculating the distance between points
$(x_1,y_1)$ and $(x_2,y_2)$,
because that distance equals the length
of the vector $(x_2-x_1,y_2-y_1)$.

Lengths and angles are not integers, so these need a floating-point
point type alongside the integer one. Two small concrete types read more
clearly in a book than one generic type behind a pile of trait bounds:

```rust
#[derive(Clone, Copy, Debug)]
struct Pf { x: f64, y: f64 }

impl Pf {
    fn sub(self, o: Pf) -> Pf { Pf { x: self.x - o.x, y: self.y - o.y } }
    fn len(self) -> f64 { (self.x * self.x + self.y * self.y).sqrt() }
    fn arg(self) -> f64 { self.y.atan2(self.x) }
    fn polar(s: f64, a: f64) -> Pf { Pf { x: s * a.cos(), y: s * a.sin() } }
    fn mul(self, o: Pf) -> Pf {
        Pf { x: self.x * o.x - self.y * o.y,
             y: self.x * o.y + self.y * o.x }
    }
}
```

The following code calculates the distance
between points $(4,2)$ and $(3,-1)$:

```rust
# #[derive(Clone, Copy, Debug)] struct Pf { x: f64, y: f64 }
# impl Pf {
#     fn sub(self, o: Pf) -> Pf { Pf { x: self.x-o.x, y: self.y-o.y } }
#     fn len(self) -> f64 { (self.x*self.x + self.y*self.y).sqrt() }
# }
let a = Pf { x: 4.0, y: 2.0 };
let b = Pf { x: 3.0, y: -1.0 };
println!("{:.5}", b.sub(a).len()); // 3.16228
```

The function $\texttt{arg}(v)$ calculates the
angle of a vector $v=(x,y)$ with respect to the x axis.
The function gives the angle in radians,
where $r$ radians equals $180 r/\pi$ degrees.
The angle of a vector that points to the right is 0,
and angles decrease clockwise and increase
counterclockwise.

The function $\texttt{polar}(s,a)$ constructs a vector
whose length is $s$ and that points to an angle $a$.
A vector can be rotated by an angle $a$
by multiplying it by a vector with length 1 and angle $a$.

The following code calculates the angle of
the vector $(4,2)$, rotates it $1/2$ radians
counterclockwise, and then calculates the angle again:

```rust
# #[derive(Clone, Copy, Debug)] struct Pf { x: f64, y: f64 }
# impl Pf {
#     fn arg(self) -> f64 { self.y.atan2(self.x) }
#     fn polar(s: f64, a: f64) -> Pf { Pf { x: s*a.cos(), y: s*a.sin() } }
#     fn mul(self, o: Pf) -> Pf {
#         Pf { x: self.x*o.x - self.y*o.y, y: self.x*o.y + self.y*o.x } }
# }
let mut v = Pf { x: 4.0, y: 2.0 };
println!("{:.6}", v.arg());          // 0.463648
v = v.mul(Pf::polar(1.0, 0.5));
println!("{:.6}", v.arg());          // 0.963648
```

Comparing floating-point values for equality is unreliable, so geometric
code compares against a tolerance instead. Note that `f64::EPSILON` is
far too small for this purpose -- it is the spacing of representable
values near 1.0, not a geometric tolerance:

```rust
const EPS: f64 = 1e-9;
# let (a, b): (f64, f64) = (0.1 + 0.2, 0.3);
# println!("0.1+0.2 == 0.3 ? {}", a == b);
# println!("within EPS ?    {}", (a - b).abs() < EPS);
```
