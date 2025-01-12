'''
796. Rotate String
Solved
Easy
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.

'''

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if the lengths are different; if so, rotation is impossible
        if len(s) != len(goal):
            return False
        
        # Concatenate s with itself
        out = s + s

        # Check if goal is a substring of the concatenated string
        if goal in out:
            return True
        else:
            return False
