class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # count1 tracks open parentheses '(' that need matching
        # count2 tracks unmatched close parentheses ')'
        count1 = 0
        count2 = 0
        
        # Iterate over the string
        for char in s:
            if char == "(":
                count1 += 1  # Expecting a closing parenthesis
                
            elif char == ")":
                if count1 > 0:
                    count1 -= 1  # Matched one open parenthesis
                else:
                    count2 += 1  # Unmatched closing parenthesis, need to add an opening one
        
        # The total steps will be unmatched opening (count1) + unmatched closing (count2)
        return count1 + count2