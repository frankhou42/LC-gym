class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1

        total = 0

        maxL = height[l]
        maxR = height[r]

        while l < r: # complete all index height water counts
            if (maxL < maxR):
                res = maxL - height[l] # height added is the smaller of maxL/R 's ptr (l or r)
                #use maxL since its the min(maxL, maxR)

                total += 0 if res < 0 else res
                #consider edge case where res is negative

                #now we adjust the ptr
                l += 1
                
                #udpate maximum height of the left side of next index
                maxL = height[l] if maxL < height[l] else maxL
            else:   
                #case where maxR > maxL or tie
                res = maxR - height[r]
                total += 0 if res < 0 else res
                r -= 1
                maxR = height[r] if maxR < height[r] else maxR

        return total
