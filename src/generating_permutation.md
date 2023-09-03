# Generating permutations

Next we consider the problem of generating
all permutations of a set of $n$ elements.
For example, the permutations of $\{0,1,2\}$ are
$(0,1,2)$, $(0,2,1)$, $(1,0,2)$, $(1,2,0)$,
$(2,0,1)$ and $(2,1,0)$.

Like subsets, permutations can be generated
using recursion.
The following function `.search()` goes
through the permutations of the set $\{0,1,\ldots,n-1\}$.
The function builds a vector `permutation`
that contains the permutation,
and the search begins when the function is called with parameters:

```rust
fn search(permutation: &mut Vec<usize>, n: usize, chosen: &mut Vec<bool>){
    if permutation.len() == n{
        // process permutation
        # println!("{permutation:?}");
    } else {
        for i in 0..n{
            if chosen[i] {continue}
            chosen[i] = true;
            permutation.push(i);
            search(permutation, n, chosen);
            chosen[i] = false;
            permutation.pop();
        }
    }
}
# let mut permutation = Vec::new();
# let n = 4;
# let mut chosen = vec![false;n];
# println!("Permutation of {n}:");
# search(&mut permutation, n, &mut chosen);
```
