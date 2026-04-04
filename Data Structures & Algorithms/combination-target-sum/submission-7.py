"""
Key Insight:
When a problem has choices at each step and asks for all 
possibilities, we can model it as a decision tree.

We use recursion to explore this tree by defining a small example 
and a base case for when a solution is complete.

At each step, we iterate over all possible choices, 
recursively explore each one, and then undo the choice 
to return to the previous state before trying the next option.

At each state we need to know the current index we are on
and the subset that we have built

Input param is what do we need to know from parent at each point
which is the same as everything we need to know to describe
where I am at in decision tree

Sol:
1 []
12 1
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def validSubsets(index):
            #base case
            if index == len(nums):
                res.append(subset.copy())
                return
            
            #recursive choices
            #choose
            subset.append(nums[index])
            validSubsets(index + 1)

            #not choose
            subset.pop()
            validSubsets(index + 1)

        validSubsets(0)
        return res


            
            
            
