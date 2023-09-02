# Binary search

A general method for searching for an element
in an array is to use a `for` loop
that iterates through the elements of the array.
For example, the following code searches for
an element $x$ in an array:

```rust, ignore
for i in 0..n {
    if (array[i] == x) {
        // x found at index i
    }
}
```
The time complexity of this approach is $O(n)$,
because in the worst case, it is necessary to check
all elements of the array.
If the order of the elements is arbitrary,
this is also the best possible approach, because
there is no additional information available where
in the array we should search for the element $x$.

However, if the array is _sorted_,
the situation is different.
In this case it is possible to perform the
search much faster, because the order of the
elements in the array guides the search.
The following **binary search** algorithm
efficiently searches for an element in a sorted array
in $O(\log n)$ time.

## Method 1

The usual way to implement binary search
resembles looking for a word in a dictionary.
The search maintains an active region in the array,
which initially contains all array elements.
Then, a number of steps is performed,
each of which halves the size of the region.

At each step, the search checks the middle element
of the active region.
If the middle element is the target element,
the search terminates.
Otherwise, the search recursively continues
to the left or right half of the region,
depending on the value of the middle element.

The above idea can be implemented as follows:
```rust
# let array = vec![1,3,4,6,7,8,9];
# let x = 4;
# let n = array.len();
# let mut i = 0;
let mut a = 0;
let mut b = n-1;
# println!("The full array is {array:?}");
# println!("I search for {x:?}");
while a <= b {
    let k = (a+b)/2;
# i += 1;
# println!("Step {i}: I'm searching in {:?}", &array[a ..= b]);
    if (array[k] == x) {
        // x found at index k
# println!("FOUND!");
    }
    if array[k] > x {b = k-1}
    else {a = k+1}
}
```
In this implementation, the active region is $a \ldots b$,
and initially the region is $0 \ldots n-1$.
The algorithm halves the size of the region at each step,
so the time complexity is $O(\log n)$.

## Method 2

An alternative method to implement binary search
is based on an efficient way to iterate through
the elements of the array.
The idea is to make jumps and slow the speed
when we get closer to the target element.

The search goes through the array from left to
right, and the initial jump length is $n/2$.
At each step, the jump length will be halved:
first $n/4$, then $n/8$, $n/16$, etc., until
finally the length is 1.
After the jumps, either the target element has
been found or we know that it does not appear in the array.

The following code implements the above idea:
```rust
# let array = vec![1,3,4,6,7,8,9];
# let x = 4;
# let n = array.len();
# println!("The full array is {array:?}");
# println!("I search for {x:?}");
let mut k = 0;
let mut b = n/2;
while b >= 1{
# println!("Current jump length is {b}");
    while k+b < n && array[k+b] <= x {k += b}
    b /= 2;
}
if (array[k] == x) {
    // x found at index k
# println!("FOUND!");
}
```

During the search, the variable $b$
contains the current jump length.
The time complexity of the algorithm is $O(\log n)$,
because the code in the second `while` loop
is performed at most twice for each jump length.

## Rust functions

The Rust standard library contains the following functions
that are based on binary search and work in logarithmic time:

- `binary_search` returns a `Result<usize, usize>`, if it found the value it returns `Ok(index)` with the index of the element, if it does not found the element it return an `Err(index)` with the index where the element should be
- `binary_search_by` it is similar to `binary_search` but it accept a comparator function as closure
- `binary_search_by_key` it is like `binary_search` but it consider only one element of the data structure (the key), for example if a vector of tuples is sorted by its `.0` element you can use this function to make a search on the same `.0` key element

The functions assume that the array is sorted.
For example, the following code finds out whether
an array contains an element with value $x$:

```rust
# let array = vec![1,3,4,6,7,8,9];
# let x = 4;
# let n = array.len();
# println!("The full array is {array:?}");
# println!("I search for {x:?}");
# println!("___");
match array.binary_search(&x){
    Ok(k) => println!("{x} found at index {k}"),
    Err(k) => println!("{x} should be inserted at index {k}"),
}
```

### Iterators

In rust, another very common solution to solve problems involving a search or if you want to perform operations on elements of a collection, or even filter it, is to use iterators. 

Iterators are implemented as traits, which means that they are defined in terms of a set of methods that must be implemented by anu type that wants to be an iterator.
The most common way to create an iterator is to use the `iter()` method on a collection type, such as a vector or a string. For example, the following code creates an iterator over the numbers 1, 2, 3, 4:

```rust
let numbers = vec![1,2,3,4];
let numbers_iterator = numbers.iter();
```

Iterator in Rust are very good in terms of performance:
- They are lazy, so they don't actually iterate over the sequence of values until they are required to do so
- They are composable, so they can be combined to create more complex iterators
- They are generic, which means that they can be used with any type that implements the `Iterator` trait

The following code counts the number of elements whose value is $x$:

```rust
# let array = vec![1,2,3,4,5,4,3,2,4,4,4,7];
# let x = 4;
let count = array.iter().filter(|&el| el==&x).count();
# println!("Array is {array:?}");
# println!("x is {x}");
# println!("___");
println!("{count}");
```

## Finding the smallest solution

An important use for binary search is
to find the position where the value of a **function** changes.
Suppose that we wish to find the smallest value $k$
that is a valid solution for a problem.
We are given a function `ok(x)`
that returns `true` if `x` is a valid solution
and `false` otherwise.
In addition, we know that `ok(x)` is `false`
when `x<k` and `true` when `x >= k`.
The situation looks as follows:

| $x$ | 0 | 1 | $\cdots$ | $k-1$ | $k$ | $k+1$ | $\cdots$ |
| ---:|---|---|----------|-------|-----|-------|----------|
| $\texttt{ok}(x)$ | `false` | `false` | $\cdots$ | `false` | `true` | `true` | $\cdots$ |

Now, the value of $k$ can be found using binary search by:

```rust
# use std::cmp::Ordering;
# let array = vec![1,2,3,4,5,7,8, 9, 12, 13, 14, 15];
# let mut okx = vec![false; array.len()];
# okx.iter_mut().enumerate().for_each(|(i, e)| *e = ok(&array[i]));
# let k = 7;
# fn ok(x: &usize) -> bool{ *x >= 7 };
let ok = | x | {if ok(x) {return Ordering::Greater} Ordering::Less};
let k = array.binary_search_by(ok);
# println!("Array is {array:?}");
# println!("ok(x) is {okx:?}");
# println!("___");
# println!("k is {k:?}");
```

The search finds the largest value of $x$ for which
`ok(x)` is `false`. To do so we can exploit a binary_search_by property: indeed the function returns a value also if the returned `Result` is `Err`, we create a simple closure that return an `Ordering`, from the moment that we want the very first `true` element, we can return `Ordering::Less` if `ok(x)` is `true` and `Ordering::Greater` if it is `false`.
Thus, the next value $k=x+1$
is the smallest possible value for which
$ok(k)$ is `true`.

The algorithm calls the function `ok`
$O(\log z)$ times, so the total time complexity
depends on the function `ok`.
For example, if the function works in $O(n)$ time,
the total time complexity is $O(n \log z)$.

## Find the maximum value

Binary search can also be used to find
the maximum value for a function that is
first increasing and then decreasing.
Our task is to find a position $k$ such that

- $f(x) \le (x+1)$ when $x \le k$, and
- $f(x) \ge (x+1)$ when $x \ge k$.

The idea is to use binary search
for finding the largest value of $x$
for which $f(x)<f(x+1)$.
This implies that $k=x+1$
because $f(x+1)>f(x+2)$.
The following code implements the search: 

```rust
# use std::cmp::Ordering;
# let array = vec![11,12,13,14,65,9,8, 7, 6, 5, 4, 3, 2, 1];
let f = | &x | { 
    let i = array.iter().position(|el| el == &x).unwrap();
    array[i].cmp(&array[i+1])
};
let k = array.binary_search_by(f);
# println!("Array is {array:?}");
# println!("___");
# println!("k is {k:?}");
```
To better understand `binary_search_by`, you should just keep in mind that:
- `Ordering::Less` in custom comparator function means that the final result is **in the right half** of the collection
- `Ordering::Greater` in custom comparator function means that the final result is **in the left half**

>    The verbose version of the above function would be:
>    ```rust
>        # use std::cmp::Ordering;
>        # let array = vec![11,12,13,14,65,9,8, 7, 6, 5, 4, 3, 2, 1];
>        let f = | &x | { 
>            let i = array.iter().position(|el| el == &x).unwrap();
>            if array[i] < array[i+1]{
>                return Ordering::Less //go in the right half
>            } else {
>                return Ordering::Greater //go in left half
>            }
>        };
>        let k = array.binary_search_by(f);
>        # println!("Array is {array:?}");
>        # println!("___");
>        # println!("k is {k:?}");
>    ```
