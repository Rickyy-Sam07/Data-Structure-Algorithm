''' 

Code
Testcase
Testcase
Test Result
2185. Counting Words With a Given Prefix
Solved
Easy
Topics
Companies
Hint
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

 

Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length, pref.length <= 100
words[i] and pref consist of lowercase English letters.

'''
# solution 1:  :  (more efficient  ->0ms)
from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count


#solution 2 ::
from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            match = True  # Assume the word matches the prefix
            for i in range(len(pref)):
                if i >= len(word) or word[i] != pref[i]:
                    match = False  # Mismatch found
                    break  # No need to check further
            if match:
                count += 1
        return count
