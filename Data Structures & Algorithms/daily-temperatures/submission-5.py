"""
We want to keep temperatures that is waiting on hoter days
in a stack. If a hotter temperature is found we pop from the stack
until the hotter temperature is not hotter or we reached empty stack.
Use a stack when previous items are waiting for a future item to resolve them
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i in range(n):
            #resolve if possible
            while stack and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        
        return res

