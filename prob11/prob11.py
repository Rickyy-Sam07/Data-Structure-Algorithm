'''
2044. Count Number of Maximum Bitwise-OR Subsets
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

 

Example 1:

Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]
Example 2:

Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.
Example 3:

Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
 

Constraints:

1 <= nums.length <= 16
1 <= nums[i] <= 105

'''




from itertools import combinations
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        # Step 1: Calculate the maximum OR by generating all subsets
        n = len(nums)
        max_or = 0
        subsets = []
    
    # Generate all non-empty subsets
        for i in range(1, n + 1):
            for subset in combinations(nums, i):
                subsets.append(subset)
    
    # Step 2: Find the maximum OR value
        for subset in subsets:
            current_or = 0
            for num in subset:
                current_or |= num  # Bitwise OR for the current subset
            max_or = max(max_or, current_or)
    
    # Step 3: Count how many subsets give the maximum OR
        count = 0
        for subset in subsets:
            current_or = 0
            for num in subset:
                current_or |= num
            if current_or == max_or:
                count += 1
    
        return count



        