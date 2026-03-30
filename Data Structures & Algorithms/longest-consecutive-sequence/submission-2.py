class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set (nums)
        res = 0

        #find the longest sequence for each num
        for num in nums:
            length = 0
            #find the first of the sequence
            if (num - 1 not in nums):
                length += 1
                #while nums has the next consective number (num + incrementing var length)
                while(num + length in nums):
                    length += 1
            res = max(length, res)

        return res

