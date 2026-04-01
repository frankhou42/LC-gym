"""
heapify nums -> pop len(nums) - k elements from minHeap
return heap[0] is not good as its nlogn as we are doing
logn operation popping from nums

Key Insight:
Similar to kth element in data stream, we remove smallest
as heap size is greater than k

no need to heapify 
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]
            