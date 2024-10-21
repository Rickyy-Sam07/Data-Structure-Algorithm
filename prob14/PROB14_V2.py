def maxUniqueSplit(s: str) -> int:
    def helper(s, used):
        # 1. Base case: If the string is empty, return 0
        if not s:
            return 0
        
        max_splits = 0
        # 2. Try every possible split of the string
        for i in range(1, len(s) + 1):
            # 3. Take the substring s[:i]
            substring = s[:i]
            # 4. If this substring hasn't been used yet
            if substring not in used:
                # 5. Add it to the used set
                used.add(substring)
                # 6. Recursively try to split the remaining part of the string
                max_splits = max(max_splits, 1 + helper(s[i:], used))
                # 7. Remove the substring from the set to backtrack
                used.remove(substring)
        
        return max_splits

    # 8. We start with an empty set of used substrings
    return helper(s, set())



'''
EXPLAINATION :


Step-by-Step Explanation with Example (s = "ababccc"):
maxUniqueSplit(s: str):

This function starts the process by calling the helper function, passing the string s = "ababccc" and an empty set used = set() to track the substrings that have already been used.
python
Copy code
return helper("ababccc", set())
helper(s, used):

Base case: If s is empty (if not s), it means we've split the string fully, so return 0 because there are no more substrings left.
Initially, the string is not empty (s = "ababccc"), so this condition is skipped for now.

max_splits = 0:

We initialize max_splits to 0. This will store the maximum number of unique splits found during recursion.
Loop over possible splits:

We try to split the string s at every possible position by iterating through the indices 1 to len(s) + 1. For each split, we create a substring and check if it has been used before.
First Iteration (s = "ababccc"):
Substring s[:1] = "a":
We take the substring "a" from the string. It hasn't been used yet, so we add it to the used set (used = {"a"}).
We then call helper recursively on the remaining string "babccc".
Second Iteration (s = "babccc"):
Substring s[:1] = "b":
The next substring is "b". It hasn't been used, so we add it to used (used = {"a", "b"}).
We now call helper recursively on the remaining string "abccc".
Third Iteration (s = "abccc"):
Substring s[:2] = "ab":
We take "ab" and add it to used (used = {"a", "b", "ab"}).
We call helper recursively on "ccc".
Fourth Iteration (s = "ccc"):
Substring s[:1] = "c":
We take "c" and add it to used (used = {"a", "b", "ab", "c"}).
We call helper recursively on "cc".
Fifth Iteration (s = "cc"):
Substring s[:2] = "cc":
The final substring "cc" is added to used (used = {"a", "b", "ab", "c", "cc"}).
Now, we call helper with the remaining string, which is empty (s = "").
At this point, since the string is empty, the base case is reached, and 0 is returned.

Now, we start backtracking:

Backtrack:
We begin removing substrings from the used set to try other possible splits.
Backtracking from "ababccc":
After finding one valid split ["a", "b", "ab", "c", "cc"], we remove "cc" from used and check other substrings for "ccc".

We repeat this backtracking process for all possible splits, always updating max_splits with the highest number of splits found.

Final Result:
After trying all possible ways to split the string into unique substrings, the helper function will return the maximum number of unique splits, which for "ababccc" is 5.

Key Points:
Base Case: If the string is empty, return 0 because no further splits are possible.
Recursive Exploration: The function recursively explores all possible ways to split the string.
Backtracking: Substrings are added to the used set when a new split is made, and removed when we backtrack to explore other possibilities.
Maximizing Unique Splits: The function updates max_splits by checking every possible valid split and counting the total number of unique substrings found.







'''