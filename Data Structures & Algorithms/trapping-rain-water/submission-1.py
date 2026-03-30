class Solution:
    def trap(self, height: List[int]) -> int:
        # we swap index to loop (increase index at same time)
        # when the side of index we have isn't the minimum of the two heights

        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[len(height) - 1]
        total = 0

        while l < r:
            #consider each minimum case
            if maxL < maxR:
                area = maxL - height[l]
                total += area if area > 0 else 0
                #consider edge case when the area is negative 
                l += 1
                maxL = height[l] if maxL < height[l] else maxL
                #UDPATE maximum height for left side
            else:
                area = maxR - height[r]
                total += area if area > 0 else 0
                r -= 1
                maxR = height[r] if maxR < height[r] else maxR

        return total
                