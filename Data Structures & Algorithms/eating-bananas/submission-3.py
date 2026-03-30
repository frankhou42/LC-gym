"""
binary search through the eating rate as we are just trying all
eating rates and finding minimum eating rate for allowed hours


max eating rate is max number in piles, min eating rate is 1

pick middle eating rate, if mid eating rate hours < h, keep searching
left half as we are tryuing to minimize eating rate. Otherwise
search right half
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minimum = float('inf')

        while l <= r:
            mid = (l + r) // 2
            total_h = 0
            for p in piles:
                total_h += math.ceil(p / mid)
            
            if total_h <= h: #find smaller eating rate
                minimum = min(minimum, mid)
                r = mid - 1
            else:#eating rate too slow, eat more
                l = mid + 1

        return minimum