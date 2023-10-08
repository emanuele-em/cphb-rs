# Summary

[Preface](preface.md)

- [Basic Techniques](introduction.md)
    - [Introduction](introduction.md)
        - [Rust competitive helper](rust_competitive_helper.md)
        - [Input and output](input_and_output.md)
        - [Working with numbers](working_with_numbers.md)
        - [Shortening code](shortening_code.md)
        - [Mathematics](mathematics.md)
        - [Contests and resources](contests_and_resources.md)
    - [Time complexity](calculation_rules.md)
        - [Calculation rules](calculation_rules.md)
        - [Complexity classes](complexity_classes.md)
        - [Estimating efficiency](estimating_efficiency.md)
        - [Maximum subarray sum](maximum_subarray_sum.md)
    - [Sorting](sorting.md)
        - [Sorting theory](sorting_theory.md)
        - [Sorting in Rust](sorting_in_rust.md)
        - [Binary search](binary_search.md)
    - [Data structures](data_structures.md)
        - [Vectors](vectors.md)
        - [Slices](slices.md)
        - [Set structures](set_structures.md)
        - [Map structures](map_structures.md)
        - [Iterators and ranges](iterators_and_ranges.md)
        - [Other structures](other_structures.md)
        - [Comparison to sorting](comparison_to_sorting.md)
    - [Complete search](complete_search.md)
        - [Generating subsets](generating_subsets.md)
        - [Generating permutations](generating_permutation.md)
        - [Backtracking](backtracking.md)
        - [Pruning the search](pruning_the_search.md)
        - [Meet in the middle](meet_in_the_middle.md)
    - [Greedy algorithms](greedy_argorithm.md)
        - [Coin problem](coin_problem.md)
        - [Scheduling](scheduling.md)
        - [Tasks and deadlines](task_and_deadline.md)
        - [Minimizing sums](minimizing_sums.md)
        - [Data compression](data_compression.md)
    - [Dynamic programming](dynamic_programming.md)
        - [Coin problem](dynamic_coin_problem.md)
        - [Longest increasing subsequence](longest_increasing_subsequence.md)
        - [Paths in a grid](path_in_a_grid.md)
        - [Knapsack problems](knapsack_problems.md)
        - [Edit distance](edit_distance.md)
        - [Counting tilings](counting_titlings.md)
    - [Amortized analysis](amortized_analysis.md)
        - [Two pointers method](two_pointers_method.md)
        - [Nearest smaller elements](nearest_smaller_element.md)
        - [Sliding window minimum](sliding_window_minimum.md)
<!--     - [Range queries](README.md) -->
<!--         - [Static array queries](README.md) -->
<!--         - [Binary indexed tree](README.md) -->
<!--         - [Segment tree](README.md) -->
<!--         - [Additional techniques](README.md) -->
<!--     - [Bit manipulation](README.md) -->
<!--         - [ Bit representation](README.md) -->
<!--         - [ Bit operations](README.md) -->
<!--         - [ Representing sets](README.md) -->
<!--         - [ Bit optimizations](README.md) -->
<!--         - [ Dynamic programming](README.md) -->
<!-- - [Graph algorithms](README.md) -->
<!--     - [Basics of graphs](README.md) -->
<!--         - [ Graph terminology](README.md) -->
<!--         - [ Graph representation](README.md) -->
<!--     - [Graph traversal](README.md) -->
<!--         - [ Depth-first search](README.md) -->
<!--         - [ Breadth-first search](README.md) -->
<!--         - [ Applications](README.md) -->
<!--     - [Shortest paths](README.md) -->
<!--         - [Bellman–Ford algorithm](README.md) -->
<!--         - [Dijkstra’s algorithm](README.md) -->
<!--         - [Floyd–Warshall algorithm](README.md) -->
<!--     - [Tree algorithms](README.md) -->
<!--         - [Tree traversal](README.md) -->
<!--         - [Diameter](README.md) -->
<!--         - [All longest paths](README.md) -->
<!--         - [Binary trees](README.md) -->
<!--     - [Spanning trees](README.md) -->
<!--         - [Kruskal’s algorithm](README.md) -->
<!--         - [Union-find structure](README.md) -->
<!--         - [Prim’s algorithm](README.md) -->
<!--     - [Directed graphs](README.md) -->
<!--         - [Topological sorting](README.md) -->
<!--         - [Dynamic programming](README.md) -->
<!--         - [Successor paths](README.md) -->
<!--         - [Cycle detection](README.md) -->
<!--     - [Strong connectivity](README.md) -->
<!--         - [Kosaraju’s algorithm](README.md) -->
<!--         - [2SAT problem](README.md) -->
<!--     - [Tree queries](README.md) -->
<!--         - [Finding ancestors](README.md) -->
<!--         - [Subtrees and paths](README.md) -->
<!--         - [Lowest common ancestor](README.md) -->
<!--         - [Offline algorithms](README.md) -->
<!--     - [Paths and circuits](README.md) -->
<!--         - [Eulerian paths](README.md) -->
<!--         - [Hamiltonian paths](README.md) -->
<!--         - [De Bruijn sequences](README.md) -->
<!--         - [Knight’s tours](README.md) -->
<!--     - [Flows and cuts](README.md) -->
<!--         - [Ford–Fulkerson algorithm](README.md) -->
<!--         - [Disjoint paths](README.md) -->
<!--         - [Maximum matchings](README.md) -->
<!--         - [Path covers](README.md) -->
<!-- - [Advanced topics](README.md) -->
<!--     - [Number theory](README.md) -->
<!--         - [Primes and factors](README.md) -->
<!--         - [Modular arithmetic](README.md) -->
<!--         - [Solving equations](README.md) -->
<!--         - [Other results](README.md) -->
<!--     - [Combinatorics](README.md) -->
<!--         - [Binomial coefficients](README.md) -->
<!--         - [Catalan numbers](README.md) -->
<!--         - [Inclusion-exclusion](README.md) -->
<!--         - [Burnside’s lemma](README.md) -->
<!--         - [Cayley’s formula](README.md) -->
<!--     - [Matrices](README.md) -->
<!--         - [Operations](README.md) -->
<!--         - [Linear recurrences](README.md) -->
<!--         - [Graphs and matrices](README.md) -->
<!--     - [Probability](README.md) -->
<!--         - [Calculation](README.md) -->
<!--         - [Events](README.md) -->
<!--         - [Random variables](README.md) -->
<!--         - [Markov chains](README.md) -->
<!--         - [Randomized algorithms](README.md) -->
<!--     - [Game theory](README.md) -->
<!--         - [Game states](README.md) -->
<!--         - [Nim game](README.md) -->
<!--         - [Sprague–Grundy theorem](README.md) -->
<!--     - [String algorithms](README.md) -->
<!--         - [String terminology](README.md) -->
<!--         - [Trie structure](README.md) -->
<!--         - [String hashing](README.md) -->
<!--         - [Z-algorithm](README.md) -->
<!--     - [Square root algorithms](README.md) -->
<!--         - [Combining algorithms](README.md) -->
<!--         - [Integer partitions](README.md) -->
<!--         - [Mo’s algorithm](README.md) -->
<!--     - [Segment trees revisited](README.md) -->
<!--         - [Lazy propagation](README.md) -->
<!--         - [Dynamic trees](README.md) -->
<!--         - [Data structures](README.md) -->
<!--         - [Two-dimensionality](README.md) -->
<!--     - [Geometry](README.md) -->
<!--         - [Complex numbers](README.md) -->
<!--         - [Points and lines](README.md) -->
<!--         - [Polygon area](README.md) -->
<!--         - [Distance functions](README.md) -->
<!--     - [Sweep line algorithms](README.md) -->
<!--         - [Intersection points](README.md) -->
<!--         - [Closest pair problem](README.md) -->
<!--         - [Convex hull problem](README.md) -->
