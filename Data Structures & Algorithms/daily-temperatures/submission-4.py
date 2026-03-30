"""
temps = [30,38,30,36,35,40,28]
stack = [5, 6]
res = [1, 4, 1, 2, 1, 0, 0]
trace the example as I code plz

stack holds temperatures that are waiting on a hotter days


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
            
                