class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x1 = 0
            y1 = 0
            x2 = point[0]
            y2 = point[1]
            distance = (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
            heapq.heappush(heap, [distance, point])
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
