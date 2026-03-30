class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prefix: 1, 1, 2, 8 store product before each index
        postfix: 48, 24, 6, 1 store product after each index
        res is essentialy prefix * post fix as that is the total product of arr
        expect the arr itself

        """

        #create res arr
        res = [0] * len(nums)

        #we default product before start and after end to be 1
        #so that we don't
        prefix = postfix = 1

        #pass 1: create prefix arr
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        #pass 2: create postfix arr
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

