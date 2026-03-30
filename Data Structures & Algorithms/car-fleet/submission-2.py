class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #create sorted position array
        sorted_pairs = [(p, s) for p, s in zip(position, speed)]
        #pairs comes first because
        sorted_pairs.sort(reverse=True)

        stack = []#contains the time for each car to reach dest

        for p, s in sorted_pairs:
            stack.append((target - p)/s)
            #speed = delta_pos/time, time = delta_pos/speed
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)