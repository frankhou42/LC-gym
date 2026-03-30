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
        
        prefix_total = 1
        for i in range(len(nums)):
            res[i] = prefix_total
            prefix_total *= nums[i]

        postfix_total = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix_total
            postfix_total *= nums[i]
        return res


#time: O(n), space O(1)!
#fixed size output
