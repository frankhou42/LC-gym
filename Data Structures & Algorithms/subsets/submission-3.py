class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        #Recursively find all possible subsets
        def backtrack(index, stack):
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
            backtrack(index + 1, stack)

            #Choice 2: Not add the number
            stack.pop()
            backtrack(index + 1, stack)

        backtrack(0,[])

        return res
            
        #time: O(2^n * n) because there are 2^n leaves and n because each leaf needs
        #n computation for .copy() method

        #space: O(n) since the recursive stack is O(n)
            
