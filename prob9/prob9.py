'''
1405. Longest Happy String
Solved
Medium
Topics
Companies
Hint
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0

'''

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        
        def next_letter():
            nonlocal a, b, c  # Ensure we're modifying outer variables
            
            # If the last two characters in the result are the same, avoid repeating
            if len(result) >= 2 and result[-1] == result[-2]:
                if result[-1] == 'a':
                    if b > 0:
                        b -= 1
                        return 'b'
                    elif c > 0:
                        c -= 1
                        return 'c'
                elif result[-1] == 'b':
                    if c > 0:
                        c -= 1
                        return 'c'
                    elif a > 0:
                        a -= 1
                        return 'a'
                elif result[-1] == 'c':
                    if a > 0:
                        a -= 1
                        return 'a'
                    elif b > 0:
                        b -= 1
                        return 'b'
                
                return ''  # No valid letter can be used
            
            # If the last two are not the same, pick the letter with the highest remaining count
            else:
                if a >= b and a >= c and a > 0:
                    a -= 1
                    return 'a'
                elif b >= a and b >= c and b > 0:
                    b -= 1
                    return 'b'
                elif c >= a and c >= b and c > 0:
                    c -= 1
                    return 'c'
            
            return ''  # No valid letter can be used
        
        # Keep adding letters until no valid letter can be added
        while True:
            l = next_letter()
            if l == '':
                break  # No more valid characters can be appended
            else:
                result.append(l)  # Append the valid character to the result

        return ''.join(result)  # Join the result list into a string

