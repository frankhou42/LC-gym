class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            length = 0
            if (num - 1 not in nums):
                length += 1
                while (num + length) in nums:
                    length += 1
            
            res = max(length, res)

        return res