class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            #update max area
            area = min(heights[l], heights[r]) * (r - l)
            if area > res:
                res = area

            #compare the l and r heights and move corresponding ptr
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                #tiebreak by moving to the next tallest height
                if heights[l + 1] > heights[r - 1]:
                    l += 1
                else:
                    r -= 1
        return res