"""
Sol:
Decisions -> add "(" if open < m, add ")" if open > close

Key Insight:
when doing backtracking problem draw out what the decision tree is and what constitutes
as a possibility (leaf node)

1. Do I need all answers? Yes -> backtracking
2. What am I choosing at each step? ( or )
3. What counts as valid choice? ( if open < m, ) if open > close
4. When do I stop? close == open == n

Backtracking is trying to find all leaf, need to undo
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        valid = []

        def dfs(open_p, close_p):
            if open_p == close_p == n:
                res.append("".join(valid))
                return
            
            if open_p < n:
                valid.append("(")
                dfs(open_p + 1, close_p)
                valid.pop()
            
            if close_p < open_p:
                valid.append(")")
                dfs(open_p, close_p + 1)
                valid.pop()
        
        dfs(0, 0)
            
        return res