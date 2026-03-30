"""
sort the nums
for each num we do two ptr to search through rest
of the nums to find potential total of 0 if not found continnue
if found return the numbers
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # to sort the nums

        res = []

        for i in range(len(nums)):
            #avoid repeated num[i] -> duplicate answers in res
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            #2sum on rest to find all potential 3sums
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r] 
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    #move on to next
                    l += 1
                    r-= 1

                    #avoid repeated num[l] and num[r]
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total > 0:
                    r -= 1
                else:
                    l += 1
                
        
        return res


