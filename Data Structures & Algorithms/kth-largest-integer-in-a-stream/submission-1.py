"""
We are only keeping track of the k largest elements with minHeap
so we can get the minimum in O(1) with heap[0] peek

e.g.
[1,2,3,3]

Key Insight:
Binary search works on sorted array as it allows elimination
of half of the search space

minheap .heappush & .heappop are O(logn)

.heapify just turn input to heap, no return

we use heap when we need *the best element repeatedly*
as heap always gives the max/min

"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        # now peek gives us min of k largest (aka kth)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        #only pop if there are more than k elements so
        #we can find kth
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

