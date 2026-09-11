Got it — here's the complete, consolidated list of array & string patterns only, merging your original 20 with the additions relevant specifically to arrays/strings (dropping graph/tree-specific stuff like Union-Find or Trie unless they're array/string flavored).

| #   | Pattern                            | When to use                                                                             | Difficulty  |
| --- | ---------------------------------- | --------------------------------------------------------------------------------------- | ----------- |
| 1   | Simulation                         | Follow problem instructions directly, step by step                                      | Easy        |
| 2   | Counting / Frequency               | Count occurrences, character/element frequency                                          | Easy        |
| 3   | Prefix Sum                         | Range sum queries, cumulative totals                                                    | Easy        |
| 4   | Difference Array                   | Range update queries                                                                    | Medium      |
| 5   | Two Pointers                       | Sorted arrays, pair sums, partitioning                                                  | Easy-Medium |
| 6   | Sliding Window                     | Contiguous subarrays/substrings with a condition                                        | Medium      |
| 7   | Fast & Slow Pointers               | Cycle detection, finding duplicates                                                     | Medium      |
| 8   | Binary Search on Array             | Search/insert in sorted array                                                           | Medium      |
| 9   | Binary Search on Answer            | Optimize/minimize-maximize an answer value                                              | Medium-Hard |
| 10  | Monotonic Stack                    | Next greater/smaller element, histogram problems                                        | Hard        |
| 11  | Monotonic Queue (Deque)            | Sliding window maximum/minimum                                                          | Hard        |
| 12  | Hashing (HashMap/HashSet)          | O(1) lookup, complement search, grouping                                                | Easy        |
| 13  | Sorting-based                      | Sorting simplifies comparisons/structure                                                | Medium      |
| 14  | Greedy                             | Local optimal choice → global optimal, no sorting needed                                | Medium      |
| 15  | Interval Problems                  | Merge/insert/overlap intervals                                                          | Medium      |
| 16  | Matrix Traversal                   | 2D array patterns (rotate, spiral, search)                                              | Medium      |
| 17  | Cyclic Sort                        | Numbers confined to range [1,n]                                                         | Medium      |
| 18  | In-place Array Manipulation        | Constant space rearrangement                                                            | Medium      |
| 19  | Kadane's Algorithm                 | Maximum/minimum subarray sum                                                            | Medium      |
| 20  | Divide & Conquer                   | Split into independent subproblems, combine results                                     | Medium      |
| 21  | Dynamic Programming (1D/2D)        | Optimal substructure, overlapping subproblems (subsequences, partitions, edit distance) | Medium-Hard |
| 22  | Backtracking                       | Generate subsets, permutations, combinations                                            | Medium-Hard |
| 23  | Bit Manipulation                   | XOR tricks, subsets via bitmask, single number                                          | Easy-Medium |
| 24  | String Matching (KMP / Z-function) | Pattern search in strings                                                               | Hard        |
| 25  | Rolling Hash (Rabin-Karp)          | Efficient substring comparison                                                          | Hard        |
| 26  | Manacher's Algorithm               | Linear-time longest palindromic substring                                               | Hard        |

**A few grouping notes so you study efficiently:**

- **13 (Sorting) + 14 (Greedy)** often overlap in practice — many problems use sorting _as_ the greedy strategy (e.g., interval scheduling), but plenty of greedy problems (Jump Game, Gas Station) don't sort at all. Learn them as separate mental tools even though they co-occur often.
- **21 (DP) is the biggest, deepest category** — for arrays/strings specifically, focus on: Kadane's-style (already separate at #19), subsequence DP (LIS, LCS), partition DP (palindrome partitioning), knapsack-style (subset sum, coin change), and string DP (edit distance, wildcard matching).
- **24, 25, 26** are all "string searching" cousins — you can learn Rolling Hash first since it's the easiest to implement, then KMP, then Manacher's last since it's the most niche.
- **9 (Binary Search on Answer)** is one of the highest-leverage patterns once you're past easy problems — it disguises itself in problems that don't look like search at all (e.g., "minimize the maximum," "find smallest divisor").


Arrays basics (traversal, simulation)
Hashing
Two Pointers
Sliding Window
Prefix Sum
Sorting + Greedy
Binary Search
Binary Search on Answer
Intervals
Matrix problems
Cyclic Sort
In-place manipulation
Kadane's Algorithm
Monotonic Stack
Monotonic Queue
String algorithms (KMP, Z, Rabin–Karp)
Difference Array
Rolling Hash