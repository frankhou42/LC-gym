"""
at each step we choose a number that we haven't used yet
and add it to the local result. We recursively find all permutations
if we reach full length append to global result. 

Key Insight:
The core idea of dfs is to explore on path fully before trying another path
The base case tells us when does a path end.
 
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        
        def dfs():
            #base case
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            
            #recursive case
            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    dfs()
                    permutation.pop()
            
        
        dfs()
        return res

            