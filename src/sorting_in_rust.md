# Sorting in Rust

It is almost never a good idea to use
a home-made sorting algorithm
in a contest, because there are good
implementations available in programming languages.
For example, the Rust standard library contains
the function `sort()` that can be easily used for
sorting arrays and other data structures.

There are many benefits in using a library function.
First, it saves time because there is no need to
implement the function.
Second, the library implementation is
certainly correct and efficient: it is not probable
that a home-made sorting function would be better.

In this section we will see how to use the
Rust `sort()` function.
The following code sorts
a vector in increasing order:
```rust
let mut v = vec![4,2,5,3,5,8,3];
v.sort();
# println!("{v:?}");
```
After the sorting, the contents of the
vector will be
`[2,3,3,4,5,5,8]`.
The default sorting order is increasing,
but a reverse order is possible as follows:
```rust
let mut v = vec![4,2,5,3,5,8,3];
v.sort();
v.reverse();
# println!("{v:?}");
```
The following code sorts the string `s`:
```rust
let mut s = "monkey";
let mut s: Vec<_> = s.chars().collect();
s.sort();
# println!("{}", s.iter().collect::<String>());
```
Sorting a string means that the characters
of the string are sorted.
For example, the string _monkey_ becomes _ekmnoy_.

## `Sort_unstable()`

The particularity of `sort()` function is that when two elements of the slice are equals then it doesn't reorder them.
For this reason `sort()` function is considered **stable**.
Current implementation of `sort()` is adaptive and try to use best algorithm for each case, it is currently based on iterative merge sort inspired by timsort[^1]. In most of case (except for the case when the slice is very short) it allocate half the size of the slice.

If the stability of the sorting algorithm is not a requirement you can use `sort_unstable()` that is tipically faster than the stable version. This function is _in-place_ (it does not allocate) the algorithm is based on **pattern-defeating-quicksort**[^2]

## Comparison trait

The function `sort` requires that `Ord`, `PartialOrd`, `PartialEq` traits are defined for the data type
of the elements to be sorted.
When sorting, these traits will be used
whenever it is necessary to find out the order of two elements.

Most Rust data types have a built-in implementation of these traits,
and elements of those types can be sorted automatically.
For example, numbers are sorted according to their values
and strings are sorted in alphabetical order.

### Tuples

_Tuples_ (`(T1, T2, ...)`) are sorted primarily according to their
first elements (`.0`).
If the first elements of two tuples are equal,
they are sorted according to their second elements (`.1`) and so on:
```rust
let mut v: Vec<(_,_,_)> = Vec::new();
v.push((1,5,3));
v.push((1,6,1));
v.push((1,5,4));
v.sort();
# println!("{v:?}");
```
After this, the order of the pairs is
$(1,5,3)$, $(1,5,4)$ and $(1,6,1)$.

### User defined struct and enum

User-defined structs do not have traits `Ord`, `PartialOrd`, `PartialEq` implemented automatically.
The traits should be implemented manually:
- `Ord` implements the function `cmp()` that return `Ordering` enums to determine if an element is _Less_, _Greater_, or _Equal_ to another.
- `PartialOrd` implements the function `partial_cmp()` that returns `Option<Ordering>`.
- `PartialEq` implements `eq()` that returns `bool`: `true` if compared elements are equal, `false` otherwise.

In most cases we don't want to implements these functions one by one because the structs the we create are composed by fields that follow standard `Ordering`, for this reason in Rust most traits are _Derivable_.
Preappending `#[derive(PartialEq, Eq, PartialOrd, Ord)]` it will be produced a lexicographic ordering based on the top-to-bottom declaration order of the struct's memebers. On enums variants are ordered by their discriminant, by default discriminant is smallest for variants at the top and largest for variants at the bottom.

For example, the following struct `P`
contains the x and y coordinates of a point.
The traits are defined so that
the points are sorted primarily by the x coordinate
and secondarily by the y coordinate.
```rust
# use std::cmp::Ordering;
# #[derive(Debug)]
struct P {
    x: i32,
    y: i32,
};

impl Ord for P {
    fn cmp(&self, other: &Self) -> Ordering {
        self.x.cmp(&other.x).then(self.y.cmp(&other.y))
    }
}

impl PartialOrd for P {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for P {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}

impl Eq for P {}

#    let p1 = P { x: 3, y: 5 };
#    let p2 = P { x: 1, y: 8 };
#    let p3 = P { x: 3, y: 5 };
#    println!("{:?} == {:?}: {}",p1, p2, p1 == p2);
#    println!("{:?} == {:?}: {}",p1, p3, p1 == p3);
#    println!("{:?} < {:?}: {}",p1, p2, p1 < p2);
#    println!("{:?} > {:?}: {}",p1, p2, p1 > p2);
#    println!("{:?} <= {:?}: {}",p1, p3, p1 <= p3);
#    println!("{:?} >= {:?}: {}",p1, p3, p1 >= p3);
```
this should be easily replaced by:
```rust
# use std::cmp::Ordering;
# #[derive(Debug)]
#[derive(PartialEq, Eq, PartialOrd, Ord)]
struct P {
    x: i32,
    y: i32,
};
#    let p1 = P { x: 3, y: 5 };
#    let p2 = P { x: 1, y: 8 };
#    let p3 = P { x: 3, y: 5 };
#    println!("{:?} == {:?}: {}",p1, p2, p1 == p2);
#    println!("{:?} == {:?}: {}",p1, p3, p1 == p3);
#    println!("{:?} < {:?}: {}",p1, p2, p1 < p2);
#    println!("{:?} > {:?}: {}",p1, p2, p1 > p2);
#    println!("{:?} <= {:?}: {}",p1, p3, p1 <= p3);
#    println!("{:?} >= {:?}: {}",p1, p3, p1 >= p3);
```

___

[^1] Timsort is a hybrid, stable sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data [https://en.wikipedia.org/wiki/Timsort](https://en.wikipedia.org/wiki/Timsort)

[^2] the algorithm was developed by Orson Peters [https://github.com/orlp/pdqsort](https://github.com/orlp/pdqsort)
