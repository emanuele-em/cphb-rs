# Shortening code

Short code is ideal in competitive programming, because programs should be written as fast as possible. Because of this, competitive programmers often define shorter names for datatypes and other parts of code.

## Type names

Using the command `type` it is possible to give a shorter name to a datatype.
For example, the name `usize` should be considered long, so we can define a shorter name `u`:
```rust
type u = usize;
```
After this, the code
```rust
let a: usize = 123456789;
let b: usize = 987654321;
println!("{}", a*b);
```
can be shortened as follows:
```rust
# type u = usize;
let a: u = 123456789;
let b: u = 987654321;
println!("{}", a*b);
```
The command `type` can also be used with more complex types.
For example, the following code gives the name `vu` for a vector of `usize` and the name `hm` for a `Hashmap` with `String` as key and value.
```rust
type vu = Vec::<usize>;
type hm = std::collections::HashMap<String, String>;
```

## Macros

Another way to shorten code is to define macros.
A macro means that certain strings in the code will be changed before the compilation.
In Rust, macros are not popular during the constests but are useful if you want to create or improve your custom template (i.e. `out_line!()`).

You can define a macro using `macro_rules!` macro:

```rust
macro_rules! rep {
    ($a:expr, $b:expr) => {
        for i in $a..= $b {
            println!("{}", i);
        }
    };
}
```
After this, the code:
```rust
for i in 1..=5{
    println!("{}", i)
}
```
can be shortened as follows:
```rust
# macro_rules! rep {
#    ($a:expr, $b:expr) => {
#        for i in $a..= $b {
#            println!("{}", i);
#        }
#    };
#}
rep!(1, 5);
```
