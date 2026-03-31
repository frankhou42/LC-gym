"""
we need to keep finding 2-heaviest stones, use heap
we create max heap for stones andheappop 2 heaviest stones
loop until one stone left we keep smashing the stones and
appending the remains of smashing if there is any

Key Insight:
max heap is created by negating all the values in arr
as the min will now be the max as its negative.
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            h1 = heapq.heappop(stones)
            h2 = heapq.heappop(stones)
            if h1 != h2:
                heapq.heappush(stones, -abs(h2 - h1))

        return -stones[0] if stones else 0