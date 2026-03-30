"""
Iterate through nums to see if complement has already been seen.
If so, return curr num and complement index (stored in hashmap)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[nums[i]] = i

#time:  O(n) space: O(n)