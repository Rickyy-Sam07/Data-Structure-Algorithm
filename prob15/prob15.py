'''
1957. Delete Characters to Make Fancy String
Solved
Easy

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.

'''


class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []  # Result list to build the final string
        count = 0  # Counter for consecutive characters

        for i in range(len(s)):
            # Check if the current character is the same as the last one added to result
            if i > 0 and s[i] == s[i - 1]:
                count += 1  # Increment count for consecutive characters
            else:
                count = 1  # Reset count if it's a different character
            
            # Append the character only if the count is less than or equal to 2
            if count <= 2:
                result.append(s[i])
        
        return "".join(result)  # Join the result list into a final string