# Vectors

A **Vector** is an array whose
size can be changed during the execution
of the program.

The following code creates an empty vector and
adds three elements to it:

```rust
let v = vec![1,2,3];
# println!("{v:?}");
```
After this, the elements can be accessed like in an ordinary array:

```rust
# let v = vec![1,2,3];
println!("{}", v[0]);
println!("{}", v[1]);
println!("{}", v[2]);
```

> Access to an array element with direct access is not really idiomatic in Rust, it should be better to use std functions like `.get(&index)` that return a `Result` that could be managed. However, in competitive programming use direct access could be faster.

The function `.len()` returns the number of elements in the vector.
The following code iterates through
the vector and prints all elements in it:

```rust
# let v = vec![1,2,3];
for i in 0..v.len(){
    println!("{}", v[i])
}
```

A shorter way to iterate through a vector is as follows:

```rust
# let v = vec![1,2,3];
for x in v {
    println!("{x}");
}
```

The function `.push()` add an alement to the back of an existing Vec.
The function `.last()` returns the last element
in the Vec, and
the function `.pop()` removes the last element:

```rust
let v = vec![5,2];
v.push(6);
println!("{v:?}");
println!("{:?}", v.last());
v.pop();
println!("{v:?}");
```

Another way to create a Vec is to give the number
of elements and the initial value for each element:

```rust
// size 10, initial value 0
let v = vec![0;10]
#println!("{v:?}");
```
```rust
// size 10, initial value 5
let v = vec![5;10]
#println!("{v:?}");
```

The internal implementation of a vector
uses a struct with three elements:
- Pointer to the first data on the heap
- length
- capacity

The capacity indicates how much memory is reserved for the Vec.
Vectors have `O(1)` indexing, amortized `O(1)` push (to the end) and `O(1)` pop (from the end).
