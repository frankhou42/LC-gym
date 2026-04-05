"""
Sol:
we can choose the number or skip the number, skipping all other same numbers
Key Insight:
If we want to avoid dups, we sort and skip
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        def dfs(index):
            #base case
            if index == len(nums):
                res.append(subset.copy())
                return

            #Recusive Choices
            #Choice 1: choose
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()

            #Choice 2: Skip dups
            while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                index += 1
            dfs(index + 1)

        dfs(0)

        return res
            