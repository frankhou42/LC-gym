"""
Key Trick
water at i = min(maxL, maxR) - height[i]
use lmax and rmax to find min of maxes in O(1)
and determine which side to find water

[0,2,0,3,1,0,1,3,2,1]
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        total = 0
        while l < r:
            #we can find water for left side
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                #update lmax first so that we consider
                #water including the current pos.
                #If curr is lmax then no water
                total += lmax - height[l]
            else: 
                r -= 1
                rmax = max(rmax, height[r])
                total += rmax - height[r]
        
        return total
