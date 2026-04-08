class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        valid_p = []

        def dfs(close_p, open_p):
            #base case: stop condition to return to previous choice
            if close_p == open_p == n:
                res.append("".join(valid_p))
                return
            
            #recursive case: each choice
            if open_p < n:
                valid_p.append("(")
                dfs(close_p, open_p + 1)
                valid_p.pop()

            if open_p > close_p:
                valid_p.append(")")
                dfs(close_p + 1, open_p)
                valid_p.pop()
        
        dfs(0, 0)
        return res