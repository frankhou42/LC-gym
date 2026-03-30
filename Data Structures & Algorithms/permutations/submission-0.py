class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        #solution is the one being constantly mutated due to 
        #backtracking,

        def backtrack():
            #base case
            #if we found a solution
            if len(sol) == len(nums):
                res.append(sol.copy())
                #append not the sol addr, it will be empty
                #in the end as we pop everything out and we will
                #just print the pointer to that empty list. we want the list copy
                #at each instance
                return 

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
        backtrack()
        return res





