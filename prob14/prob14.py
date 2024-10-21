'''
1593. Split a String Into the Max Number of Unique Substrings
Solved
Medium
Topics
Companies
Hint
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.


'''


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(s, used):
        # If the string is empty, return 0 since there are no substrings left
            if not s:
                return 0
        
            max_splits = 0
        # Try every possible split of the string
            for i in range(1, len(s) + 1):
            # Take the substring s[:i]
                substring = s[:i]
            # If this substring hasn't been used yet
                if substring not in used:
                # Add it to the used set
                    used.add(substring)
                # Recursively try to split the remaining part of the string
                    max_splits = max(max_splits, 1 + helper(s[i:], used))
                # Remove the substring from the set to backtrack
                    used.remove(substring)
        
            return max_splits

    # We start with an empty set of used substrings
        return helper(s, set())