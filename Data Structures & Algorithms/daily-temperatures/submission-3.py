"""
temps = [30, 29, 38]
stack = [0, 1]
res = []
trace the example as I code plz

if the element is greater than the previous element
we keep popping elements from the stack is empty or there
is an element greater than curr element
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res
            
                