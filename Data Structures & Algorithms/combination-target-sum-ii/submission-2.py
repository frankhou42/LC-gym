"""
Sol:
skip the number to not use it and all its dups or use the number and go to next

Key Insight:
Backtracking base cases = success + failure stop condition
Tree base cases = structure ends

Backtracking has no left and right subtree to recurse over
we have to define the state of what left and right subtree
means. (e.g. left subtree in this problem is to skip number)

For each choice:
    we change the state
    explore all possibilities from that choice
    then restore the original state before trying the next choice

sort to avoid dups by skipping dups when we decide to not use a number
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        combination = []
        def dfs(total, index):
            #Base cases: success and failure
            if total == target:
                res.append(combination.copy())
                return
            
            if index >= len(candidates) or total > target:
                return

            #Recursive case
            #Choice 1:
            next_index = index
            while next_index < len(candidates) - 1 and candidates[next_index + 1] == candidates[next_index]:
                next_index += 1
            dfs(total, next_index + 1)
            


            #Choice 2:
            combination.append(candidates[index])
            total += candidates[index]
            dfs(total, index + 1)
            #need to undo after finished exploring that path

            combination.pop()
            total -= candidates[index]

        dfs(0, 0)
        return res