'''
1331. Rank Transform of an Array
Solved
Easy
Topics
Companies
Hint
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]

'''
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Sort the array to determine the ranks of each unique element
        s_arr = sorted(arr)
        
        # Step 2: Create a dictionary to store the rank of each unique element
        dic = {}
        count = 1
        
        # Step 3: Assign ranks to the unique elements in the sorted array
        for i in s_arr:
            if i not in dic:
                dic[i] = count
                count = count + 1

        # Step 4: Build the result array based on the original array 'arr'
        final = []
        for i in arr:
            final.append(dic[i])  # Append the rank of the current element in 'arr'

        # Step 5: Return the rank-transformed array
        return final
