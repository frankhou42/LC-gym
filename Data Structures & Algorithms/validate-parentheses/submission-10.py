"""
If its the start of a parenthsis put in stack, if its not
and don't match top of stack, return false
"""
class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {
            '(' :')',
            '[' :']',
            '{' :'}'
        }

        stack = []

        for c in s:
            if c in dictionary:
                stack.append(c)
            elif stack and dictionary[stack[-1]] == c:
                stack.pop()
            else:
                return False

        return not stack