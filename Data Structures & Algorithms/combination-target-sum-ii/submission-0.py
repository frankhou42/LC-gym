class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        #duplicate mauy occur because we can take duplicate value in candidates
        #so after skipping the first num we can possibly take the second num
        #which is exact same as first num and consider it as solution

        #to avoid, we first sort the candidates and if we choose not to take a num,
        #we skip all dups of that num
        candidates.sort()
        
        #function is used to find potential candidates combination
        #index needed to traverse the candidates
        #stack needed to backtrack to previous state of candidates
        #total needed to see sum at current recursive call
        def dfs(index, stack, total):

            #if total == target we can add it to res and return to prev call
            #Since we check and append stack in the next recursive call, index maybe out of boudns
            #so we will perform the target check first to ensure last element before index out of bound is checked
            if total == target:
                res.append(stack.copy())
                return

            #base cases:(cases where we end recursion)
            #if the index out of bounds return to prev call
            if index > len(candidates) - 1:
                return
            
            #if total greater than target return to prev call
            if total > target:
                return

            
            #Choices: at the moment witht the current index  we can decide to add that number or not

            #Choice 1: we can add the number and move on to the next
            stack.append(candidates[index])
            dfs(index + 1, stack, total + candidates[index])

            #Choice 2: we can skip the number, if we skip the number, skip all variation of it to avoid dup
            stack.pop()
            while index < len(candidates) - 1 and candidates[index + 1] == candidates[index]:
                index += 1
            dfs(index + 1, stack, total)

        dfs(0, [], 0)
        return res