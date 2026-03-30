class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        #use backtrack to explore all cases, if doesn't meet condition we go back
        def backtrack(open_p, close_p):
            #base case
            if open_p == close_p == n:
                res.append("".join(stack))
                #this puts the valid parenthesis strs in stack into a string
            #Now write out the logic for the two choices: add ( or )
            
            #if we have close_p < open_p we can add )
            if close_p < open_p:
                stack.append(")")
                backtrack(open_p, close_p + 1)
                stack.pop()
            #if we have open_p < n we can add (
            if open_p < n:
                stack.append("(")
                #start a new backtrack cycle with new inputs
                backtrack(open_p + 1, close_p)
                #after 
                stack.pop()
            
            
        
        backtrack(0,0)
        return res
            

            
