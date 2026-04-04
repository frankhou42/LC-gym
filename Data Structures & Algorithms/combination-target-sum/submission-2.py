"""
Sol:
decisions -> we can either choose the current number or move on
to next

Key Insight:
First realize its backtracking if we are asked to find all
possibilites.

base case give answers top smallest problem 

recursive case we are going through each of the decision at each step
in the decision tree

!!!
Only difference between tree problem and backtracking is that
we need to figure out what is the decision tree and we need to
do the undo step


"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        combination = []
        #what we need to know from the parent to do base case + recursive case
        def dfs(total, index):
            #Base case total reaches num
            if total == target:
                res.append(combination.copy())
                return #stop recursing

            #Base case total > target or index > len(nums)
            if total > target or index >= len(nums):
                return
            
            #Recursive Case
            #Choice 1: Choose curr num
            total += nums[index]
            combination.append(nums[index])
            dfs(total, index)

            #Choice 2: skip curr num
            total -= nums[index]
            combination.pop()
            dfs(total, index + 1)
        
        dfs(0, 0)
        return res