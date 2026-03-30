"""
Key Trick
water at i = min(maxL, maxR) - height[i]
use lmax and rmax

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
                #update lmax for next iter
                lmax = max(lmax, height[l])
                total += lmax - height[l]
            else: 
                r -= 1
                rmax = max(rmax, height[r])
                total += rmax - height[r]
        
        return total
