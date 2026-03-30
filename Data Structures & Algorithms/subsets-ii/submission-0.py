class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort() #sort nums so in order
        def backtrack(index):
            #base case
            if index == len(nums):
                res.append(subset.copy())
                return
            
            #option1: pick the num
            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop() #after reaching base case pop back up the tree to explore other option

            #option2: don't pick the num nd all of its dups
            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1)

        backtrack(0)
        return res
            