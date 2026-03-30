class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #each key value pair is a set for a col/row/sq
        cols = defaultdict(set)
        rows = defaultdict(set)
        sq = defaultdict(set)
        #Possible keys: (0,0), (0,1)... (2,2) for 9 sqs

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                #conditions that board is invalid when element alr in set
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in sq[(r//3, c//3)]):
                    return False

                #add element to its corresponding set in the dicts for rows/cols/sqs
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sq[(r//3), (c//3)].add(board[r][c])

        return True