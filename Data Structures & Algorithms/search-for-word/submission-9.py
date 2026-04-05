"""
Key Insight:
Backtracking traverse paths, Trees & Graphs travers nodes
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set()
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def findWord(r, c, i):
            #Base cases of success and failure
            if i == len(word):
                return True
            if not (0 <= r < ROWS and 0 <= c < COLS and board[r][c] == word[i] and (r, c) not in path):
                return False
            
            #process current word
            path.add((r, c))

            #Explore Each path and backtrack if find answer or false
            res = (findWord(r + 1, c, i + 1) or
                   findWord(r - 1, c, i + 1) or
                   findWord(r, c + 1, i + 1) or
                   findWord(r, c - 1, i + 1))

            path.remove((r, c))
            return res
            
        for r in range(ROWS):
            for c in range(COLS):
                if findWord(r, c, 0):
                    return True
        
        return False