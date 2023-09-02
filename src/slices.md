# Slices

In Rust, `slices` are a powerful concept that allows you to work with a portion of a sequence (such as an `Vec`, or `String`) without copying or transferring ownership of the data.
Slices provide a safe and efficient way to reference a contiguous subsequence of elements.

`Slice` are composed of two parts:
1. A pointer to a chunk of memory
2. Length: a count of how many items are stored

A `Slice` is essentially a reference, unlike a `Vec` which stores its own elements.
It points to elements in another collection and is commonly used when you need to work with a subset of elements from that collection.

Slices are typically created using the slicing syntax [start..end], where start is the index of the first element to include in the slice, and end is the index of the first element to exclude from the slice. Here's an example:

```rust
let data = [12, 21, 33, 41, 57];
let slice = &data[1..4];
println!("{:?}", slice); // [21, 33, 41]
```

You can also create slices from `Vec` as follow:
```rust
let v = vec![12, 21, 33, 41, 57];
let slice = &v[1..4];
println!("{:?}", slice); // [21, 33, 41]
```

## Slice types

There are two main types of slices:
1. **Immutable Slices** (`&[T]`): These slices allow read-only access to the underlying data. You can't modify the elements through an immutable slice.
2. **Mutable Slices** (`&mut [T]`): Mutable slices allow both reading and writing to the underlying data. You can modify the elements through a mutable slice.


