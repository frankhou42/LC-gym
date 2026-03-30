"""
loop from closest to furthest, if current car time to reach target
is smaller than the previous closer car, merge to same fleet since
its faster. Otherwise, new fleet is formed

we are using the cars ahead to resolve the cars behind it
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
        stack = []
        for p, s in cars:
            time_to_target = (target - p) /s
            
            if not stack or stack[-1] < time_to_target:
                stack.append(time_to_target)
        return len(stack)
            
            