# Other structures

## VecDeque

A `VecDeque` is a double-ended queue implemented with a growable ring buffer.
It provides the functions `.push_back()` and `.pop_back()`, but it also includes the functions 
`.push_front()` and `.pop_front()`.
A `VecDeque` can be used as follow:
```rust
# use std::collections::VecDeque;
let mut d = VecDeque::new();
d.push_back(5); // [5]
d.push_back(2); // [5,2]
d.push_front(3); // [3,5,2]
d.pop_back(); // [3,5]
d.pop_front(); // [5]
# println!("d is {d:?}");
```
The internal implementation of a VecDeque
is more complex than that of a vector,
and for this reason, a deque is slower than a vector.

## LinkedList

A `LinkedList` in Rust is a doubly-linked list data structure provided by the standard library.
It is a linear data structure where each element (node) in the list contains two references, one pointing to the previous node and one pointing to the next node.
This structure allows for efficient insertions and removals at both the beginning and end of the list.

Unlike `Vec`, `LinkedList` does not require reallocation when elements are added or removed, which can lead to more predictable performance characteristics in certain situations.
However, it's important to note that random access to elements in a `LinkedList` is not as efficient as in `Vec` since it requires traversing the list from the beginning or end.

Here's an example of using `LinkedList`:
```rust
# use std::collections::LinkedList;
let mut list = LinkedList::new();
list.push_front(1);
list.push_front(2);
list.push_front(3);
println!("{:?}", list.front()); // Some(3)
println!("{:?}", list.back()); // Some(1)
```

## BinaryHeap

A **Binary Heap**
maintains a set of elements.
The supported operations are insertion,
retrieval and removal of
either the minimum or maximum element.
Insertion and removal take $O(\log n)$ time,
and retrieval takes $O(1)$ time.

While an ordered set efficiently supports
all the operations of a priority queue,
the benefit of using a priority queue is
that it has smaller constant factors.
A priority queue is usually implemented using
a heap structure that is much simpler than a
balanced binary tree used in an ordered set.

By default, the elements in a Rust priority queue are sorted in decreasing
order, and it is possible to find and remove the largest element in the queue. The
following code illustrates this:

```rust
# use std::collections::BinaryHeap;
let mut heap = BinaryHeap::new();
heap.push(1);
heap.push(5);
heap.push(2);
println!("{:?}",heap.peek()); //Some(5)
heap.pop();
println!("{:?}",heap.pop()); // Some(2)
```
