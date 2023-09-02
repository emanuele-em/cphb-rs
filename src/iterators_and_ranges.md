# Iterators and ranges

As anticipated in previous chapters, many functions in the Rust standard library
operate with iterators.
In Rust an `Iterator` is a trait that implement a method, `.next()`, which when called, returns an `Option<Item>`.

When you call `next` it returns `Some(Item)` as long as there are alement, and `None` otherwise.
`Iterator` trait has more that 70 others methods but they are built on top of `next`, so you can get them for free.

## Working with ranges

Iterators are used in Rust standard library functions
that are given a range of elements in a data structure.
For example, the following code use `.fold()` that accept as parameters the starting point of the accumulator (`0`), accumulator (`accumualator`) and sum every single element (`x`) of the given range.
```rust
(0..10).fold(0, |accumulator, x| sum+x); //45
# println!("{}", (0..10).fold(0, |accumulator, x| sum+x)); //45
```
This code iter on a every single element of the range and edit them accordingly to the closure, then it iter on the first $5$ element:
```rust
for x in (1..100).map(|x| x+2).take(5){
// 3 4 5 6 7
# println!("{}", x);
}
```

## Working with Iterators

Iterators are often used to access elements of a collection. The following code creates an
iterator `it` from a `BTreeSet`:

```rust
# use std::collections::BTreeSet;
let mut s = BTreeSet::new();
let it = s.iter();
```
There are a lot of method that allow you to iterate through the iterator and every type adapt each method to its structure.
The following code return the max value of the previous `BTreeSet`:
```rust
# use std::collections::BTreeSet;
# let mut s = BTreeSet::from([1,2,3,4,5,56,7]);
# let it = s.iter();
# println!("{:?}", it.clone().max().unwrap());
it.max().unwrap();
```

function `.find()` accept a closure that return true or false, it applies the closure to each element of the iterator and if of them return true it return `Some(element)`. It stops at the first `true`
```rust
let v = vec![1, 2, 2, 2, 5, 56, 7, 2];
# println!("{:?}", v.iter().find(|&x| x==&2));
v.iter().find(|&x| x==&2); //Some(2)
```

The function `.filter()` filter all element of the iterator with the expression inside the closure that it accepts as argument.
The following code returns the smallest element in the collection whose value is _at least $x$_:
```rust
# let v = vec![1, 2, 2, 2, 5, 56, 7, 2];
# println!("{:?}", v.iter().filter(|&el| el>&5).min().unwrap());
v.iter().filter(|&el| el>&5).min().unwrap(); // 7
```

You can play combinig methods to obtain particular results as for example the nearest element of a given value $x$:
```rust
# let v = vec![1, 2, 2, 2, 5, 56, 7, 2];
# let x = 5;
let near_up = v.iter().filter(|&el| el>&x).min().unwrap();
let near_down = v.iter().filter(|&el| el<&x).max().unwrap();
println!("{near_down} < x < {near_up}"); // 2 < x < 7
```

