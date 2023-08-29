# Rust Competitive Helper

[Rust Competitive Helper](https://github.com/rust-competitive-helper/rust-competitive-helper) is a template for competitive programming in Rust, written by [Egor](https://codeforces.com/profile/Egor) and adapted as a separate project by [qwerty787788](https://codeforces.com/profile/qwerty787788).

The use of a template in competitive programming is very useful because it saves time for repetitive tasks such as reading input and writing output.

Rust competitive helper works well with [Competitive Companion](https://github.com/jmerle/competitive-companion), guides and tutorial are avalaible in Readme.md of the relevant Github repositories.
From now on it will be assumed that rust competitive helper is set up correctly.

The main function where we are going to solve the problem looks like this:

```rust, ignore
use algo_lib::io::input::Input;
use algo_lib::io::output::output;
use algo_lib::{out, out_line};

fn solve(input: &mut Input, _test_case: usize) {
    // solution comes here
}

pub(crate) fn run(mut input: Input) -> bool {
    // this part automatically changes based on problem typology:
    // (1) number of tests given
    // (2) one test only
    // (3) EOF
}

//START MAIN
mod tester;

fn main() {
    tester::run_tests();
}
//END MAIN
```
The code can be compiled using the following command
```ignore
cargo build --bin name_of_the_problem_bin
```
The solution will be compiled in the `main.rs` file of the main package (not in the `main.rs` file of the compiled bin where `solve()` function is located)
