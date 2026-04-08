"""
choices: we can split at each index, if the first half ispali
add to path and we continue to dfs, otherwise we backtrack and
try another path
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPali(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def dfs(i):
            #base case: stopping condition
            if i == len(s):
                res.append(path.copy())
                return

            #Choices: try split at every index
            for j in range(i + 1, len(s) + 1):
                if isPali(s[i : j]):
                    path.append(s[i : j])
                    dfs(j)
                    path.pop()
            
        dfs(0)
        return res