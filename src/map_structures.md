# Map structures

A **map** is a generalized array
that consists of key-value-pairs.
While the keys in an ordinary array are always
the consecutive integers $0,1,\ldots,n-1$,
where $n$ is the size of the array,
the keys in a map can be of any data type and
they do not have to be consecutive values.

The Rust standard library contains two map
implementations that correspond to the set
implementations: the structure
`BTreeMap` is based on a balanced
binary tree and accessing elements
takes $O(\log n)$ time,
while the structure
`HashMap` uses hashing
and accessing elements takes $O(1)$ time on average.

The following code creates a map
where the keys are strings and the values are integers:

```rust
# use std::collections::BTreeMap;
let mut m = BTreeMap::new();
m.insert("monkey", 4);
m.insert("banana", 3);
m.insert("haspsichord", 9);
println!("{}", m["banana"]);
```

If the value of a key is requested
but the map does not contain it,
it panics.
To prevent panic, `.entry()` function could be used, and associated with other cool methods it became very usefull.
For example, in the following code,
the key _aybabtu_ with value 0
is added to the map.

```rust
# use std::collections::BTreeMap;
let mut m = BTreeMap::new();
m.entry("aybabtu").or_insert(0);
# println!("{}", m["aybabtu"]);
```

The function `.contains_key()` checks if a key exists in a map, also `.get()` can be used to check if a key exists, the difference is that the first function retusn a `bool`, while the second returns a `Option`:
```rust
# use std::collections::BTreeMap;
let mut m = BTreeMap::new();
m.entry("aybabtu").or_insert(5);
println!("{:?}", m.contains_key("aybabtu")); //true
println!("{:?}", m.get("aybabtu")); //Some(5)
println!("{:?}", m.contains_key("piano")); //false
println!("{:?}", m.get("piano")); //None
```
The following code prints all the keys and values in a map, every element is a tuple so you can destructur it in for loop:
```rust
# use std::collections::BTreeMap;
# let mut m = BTreeMap::new();
# m.insert("monkey", 4);
# m.insert("banana", 3);
# m.insert("haspsichord", 9);
# m.insert("aybabtu", 9);
for (i, x) in m{
    println!("{i}: {x}");
}

```
