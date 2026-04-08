"""
Key Insight:
Recursive case shows what decisions to make to choose which path and we backtrack back up

Make sure I return in base case after found a correct solution as we
now need to go find different path solution
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        res = []
        path = []

        def dfs(index):
            #base case
            if len(digits) == index:
                res.append("".join(path))
                return
                
            for c in hashmap[digits[index]]:
                path.append(c)
                dfs(index + 1)
                path.pop()
        
        dfs(0)

        return res
