"""
Iterate through each string if its an operator pop out
the last 2 and do opeartion and append it back to the stack
If not an operator just append to stack
return stack[-1] at the end
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif c == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                #use int so it truncates towards 0
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        
        return int(stack[-1])