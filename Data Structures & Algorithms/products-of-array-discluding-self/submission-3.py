"""
forward pass through nums to populate prefix sum 
and then backward pass through nums to populate

prefix sum and postfix sum are just running totals

total = 1 * 6
[1,1,2,8]
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        total = 1
        for i in range(len(nums) - 1):
            total *= nums[i]
            res[i + 1] = total

        total = 1
        for i in range(len(nums) - 1, 0, -1):
            total *= nums[i]
            res[i - 1] *= total
        return res


