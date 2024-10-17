'''
670. Maximum Swap
Solved
Medium
Topics
Companies
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
'''


class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        max_num = num  # Initialize max_num to the original number
    
    # Try swapping every pair of digits
        for i in range(len(num_str)):
            for j in range(i + 1, len(num_str)):
            # Swap the digits at index i and j
                num_str[i], num_str[j] = num_str[j], num_str[i]
            
            # Convert the list back to a number and compare
                swapped_num = int(''.join(num_str))
                max_num = max(max_num, swapped_num)
            
            # Swap the digits back to restore the original order
                num_str[i], num_str[j] = num_str[j], num_str[i]
    
        return max_num
