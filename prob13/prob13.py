'''
1106. Parsing A Boolean Expression

Hard

A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

 

Example 1:

Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.
Example 2:

Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.
Example 3:

Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.
 

Constraints:

1 <= expression.length <= 2 * 104
expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.

'''






class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        stack = []

        for char in expression:
            if char == 't':
                stack.append(True)
            elif char == 'f':
                stack.append(False)
            elif char in ('!', '&', '|'):
                stack.append(char)
            elif char == ')':
            # We need to evaluate the current sub-expression
                sub_expr = []
                while stack[-1] != '(':
                    sub_expr.append(stack.pop())
                stack.pop()  # Remove the '('

                operator = stack.pop()

                if operator == '!':
                # Negation, there should be exactly one boolean value
                    stack.append(not sub_expr[0])
                elif operator == '&':
                # AND, we return True if all sub-expressions are True
                    stack.append(all(sub_expr))
                elif operator == '|':
                # OR, we return True if at least one sub-expression is True
                    stack.append(any(sub_expr))
            elif char == '(':
                stack.append('(')
    
        return stack[0]
        