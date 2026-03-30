class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        stack = []

        #Recursively find all possible subsets
        def dfs(index):
            #base case 
            #Iterated beyond the list, max depth and got an answer
            #append to res
            if index > len(nums) - 1:
                #stack.copy() freezes the current stack and append it
                #to res
                res.append(stack.copy())
                return None
            
            #At each index there are 2 choices

            #Choice 1: add the number
            stack.append(nums[index])
            dfs(index + 1)

            #Choice 2: Not add the number
            stack.pop()
            dfs(index + 1)

        dfs(0)

        return res
            
            
