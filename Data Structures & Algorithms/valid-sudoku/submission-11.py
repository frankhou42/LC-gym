"""
Create set for each row, col, box
Iterate through every single num, ignore .
Put each num in correct set

box = (r // 3) * 3 + (c // 3)
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        boxSets = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                #correct box
                box = (r // 3) * 3 + c // 3

                if val in rowSets[r] or val in colSets[c] or val in boxSets[box]:
                    return False
                
                rowSets[r].add(val)
                colSets[c].add(val)
                boxSets[box].add(val)
        return True
