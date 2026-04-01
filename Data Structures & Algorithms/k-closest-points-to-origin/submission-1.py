"""
since we are finding k closest
we just minHeap by distance and have coordinate added to it

Key Insight:
if values in heap is list, the heap's order is kept
by th value of the first element in list
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distances.append([(x ** 2) + (y ** 2), x, y])

        heapq.heapify(distances)

        res = []
        for _ in range(k):
            d = heapq.heappop(distances)
            res.append([d[1], d[2]])

        return res
