"""
convert to hashset, use the in operator as its O(1)

find LCS if there is next number (aka num + 1) in nums, otherwise would be O(n^2)

iterate through each element and compare its LCS with max LCS

return max LCS
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        maxLCS = 0

        for num in set_nums:
            LCS = 1
            next_num = num + 1
            while next_num in set_nums:
                LCS += 1
                next_num += 1
            
            maxLCS = max(LCS, maxLCS)

        return maxLCS

#time: O(n) space: O(n)