class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        #include self
        def isPali(s, index, j):
            substring = s[index:j+1]
            l, r = index, j
            while l < r:
                if (s[l] == s[r]):
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def backtrack(index):
            #base case:
            if len(s) == index:
                res.append(part.copy())
                return
            
            #choices: partition at every single gap, keep making
            #partitions of parttioned string through recursive call
            #to uncover all cases
            for j in range(index, len(s)):
                if isPali(s, index, j):
                    part.append(s[index:j+1])
                    #backtrack to make the next partition at every single gap
                    #in the partitioned str
                    backtrack(j + 1)
                    #backtrack after dfs hits base case
                    part.pop()#!!!very important

        backtrack(0)
        return res

        #time complexity: O(n * 2^n-1) since there are 2^n-1 possible ways to partition the string
        #since deciding to partition at each gap is each a step to complete the partitioning
        #the time complexity is thus 2^n-1

        #space compelxity: O(n) where n is the depth of the decision tree