class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check dup for each row
        for i in range(9):
            r_hashset = set()
            c_hashset = set()
            for j in range(9):
                # Row check: only if that cell isn’t “.”
                if board[i][j] != '.':
                    if board[i][j] in r_hashset:
                        return False
                    r_hashset.add(board[i][j])

                # Column check: only if that cell isn’t “.”
                if board[j][i] != '.':
                    if board[j][i] in c_hashset:
                        return False
                    c_hashset.add(board[j][i])


        for r in range(3):
            for c in range(3):
            # check each 3×3 square
                sq_hashset = set()
                for j in range(3*r,3+3*r):
                    for k in range(3*c,3+3*c):                   
                        if board[j][k] == ".":
                            continue
                        if board[j][k] in sq_hashset:
                            return False
                        sq_hashset.add(board[j][k])
        

        return True
