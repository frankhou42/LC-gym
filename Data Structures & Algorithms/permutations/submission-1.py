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

            #the choices at each step
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    #backtrack and go for another choice using for loop
                    sol.pop()
        backtrack()
        return res

        #Time compolexity in backtracking = number of leaves x cost per leaf
        #which is the number of calls we make x cost of each call

        #Space complexity is O(n) not considering output, this is called auxiliary space
        #the recursion stack has O(n) cuz there is "n" depth. Sol is O(n) cuz there is n elements in it

        #O(logn) for BST binary search, O(n) for DFS/BFS traversal


