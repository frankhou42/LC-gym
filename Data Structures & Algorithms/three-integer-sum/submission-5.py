"""
sort the nums
for each num we do two ptr to search through rest
of the nums to find potential total of 0 if not found continnue
if found return the numbers

!!! avoid repeated answer with 
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #to sort the nums small to big

        res = []

        for i in range(len(nums)):
            #avoid repeated number for answer
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            #2sum 
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r] 
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    #move on to next !!!
                    l += 1
                    r-= 1

                    #avoid repeat using same number as answer
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total > 0:
                    r -= 1
                else:
                    l += 1
                
        
        return res

#time O(n^2) space O(1), res is output, doesn't count


