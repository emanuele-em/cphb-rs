# Set structures

A *set* is a data structure that
maintains a collection of elements.
The basic operations of sets are element
insertion, search and removal.

The Rust standard library contains two set
implementations:
The structure `BTreeSet` is based on a balanced
binary tree and its operations work in $O(\log n)$ time.
The structure `HashSet` uses hashing,
and its operations work in $O(1)$ time on average.

The choice of which set implementation to use
is often a matter of taste.
The benefit of the `BTreeSet` structure
is that it maintains the order of the elements
and provides functions that are not available
in `HashSet`.
On the other hand, `HashSet`
can be more efficient.

The following code creates a set
that contains integers,
and shows some of the operations.
The function `.insert()` adds an element to the set,
the function `.contains()` returns the number of occurrences
of an element in the set,
and the function `.remove` removes an element from the set.

```rust
# use std::collections::BTreeSet;
let mut s = BTreeSet::new();
s.insert(3);
s.insert(2);
s.insert(5);
println!("{:?}", s.contains(&3)); // true
println!("{:?}", s.contains(&4)); // false
s.remove(&3);
s.insert(4);
println!("{:?}", s.contains(&3)); // false
println!("{:?}", s.contains(&4)); // true
```

A set can be used mostly like a vector,
but it is not possible to access
the elements using the `[]` notation.
The following code creates a set,
prints the number of elements in it, and then
iterates through all the elements:
```rust
# use std::collections::BTreeSet;
let mut s = BTreeSet::from([1,2,3,4]);
println!("{}", s.len());
for x in s {
    println!("{x}");
}
```

An important property of sets is
that all their elements are _distinct_.
