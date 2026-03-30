class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, total, stack):
            #base cases:
            #if sum equal to target add
            #if index out of bounds return None
            

            if total == target:
                res.append(stack.copy()) 
                # add a deep-copy of stack, not a ptr which is mutable
                return 
            
            #if greater than target or out of range backtrack
            if index > len(nums) - 1 or total > target:
                return 

            #Choices:
            
            #choice 1: keep adding the curr num to total
            stack.append(nums[index])
            dfs(index, total + nums[index], stack)

            #choice 2: not add curr num to total and move on to the next num
            stack.pop()
            dfs(index + 1, total, stack)

        dfs(0, 0, [])
        return res