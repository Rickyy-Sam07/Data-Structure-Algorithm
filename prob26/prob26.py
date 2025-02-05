'''1790. Check if One String Swap Can Make Strings Equal
Solved
Easy
Topics
Companies
Hint
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
'''

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # If lengths are different, return False immediately
        if len(s1) != len(s2):
            return False

        # Initialize an empty list to store the indices and mismatched characters
        diff = []

        # Iterate over both strings and find mismatched positions
        for i in range(len(s1)):
            if s1[i] != s2[i]:  # If characters at the same position differ
                diff.append((i, s1[i], s2[i]))  # Store index, char from s1, char from s2

        # Case 1: If no differences found, strings are already equal
        if len(diff) == 0:
            return True

        # Case 2: If exactly two differences are found, check swap possibility
        if len(diff) == 2:
            # Extract the mismatched character pairs
            index1, char1_s1, char1_s2 = diff[0]
            index2, char2_s1, char2_s2 = diff[1]

            # Check if swapping the mismatched characters makes s1 equal to s2
            if char1_s1 == char2_s2 and char1_s2 == char2_s1:
                return True

        # If there are more than two mismatches or swap conditions don't match, return False
        return False
