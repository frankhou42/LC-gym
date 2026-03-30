class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre = 1
        post = 1

        #prefix first pass
        for i in range(len(nums)):
            #put the prefix into res
            res[i] *= pre
            pre *= nums[i]

        #suffix second pass

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]


        return res



             
