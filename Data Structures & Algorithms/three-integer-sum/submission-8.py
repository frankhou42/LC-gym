"""
Fix one number, find pairs with two pointers, and skip 
duplicates at every step.

we sort and use 2 ptrs here instead of hashmap 2sum because
this gives us control over l and r ptrs to avoid duplicates

Avoiding duplicates is key to solve this problem!!!
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []

        for i in range(len(nums)):
            #skips i of same res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    #skips l and r of same res
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    
                    #keep seraching inside
                    l += 1
                    r -= 1
                    
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
