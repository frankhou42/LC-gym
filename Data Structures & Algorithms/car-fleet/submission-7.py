"""
!!!Key Intuition to Stack Problems:
Stack problem is about storing unresolved elements
and processing them when a future element comes

sort the position and speed arr by position
iterate through each car and calculate its time
to reach the target from closest to target to furthest
this is because the front car decides the fleet speed

pos = speed x time

zip combines 2 arrs and to reverse sort we must reverse=True

"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, speed) for pos, speed in zip(position, speed)]
        cars = sorted(cars, reverse=True)
        stack = []

        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if stack and time > stack[-1] or not stack:
                stack.append(time)
        
        return len(stack)
