"""
Purpose of dfs is to check if going from a cell we can find word
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, index):
            #base case: stop condition
            if not(0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited and board[r][c] == word[index]):
                return False
            
            if index == len(word) - 1:
                return True

            #Choices:
            visited.add((r, c))
            for dr, dc in dirs:
                if dfs(r + dr, c + dc, index + 1):
                    return True
            visited.remove((r, c))



        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False
