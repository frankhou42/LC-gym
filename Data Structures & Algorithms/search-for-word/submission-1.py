class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        #needed to prevent dup check, infinite recursion
        visited = set()

        def backtrack(r, c, i):
            #base cases
            #when word is found
            if i == len(word):
                return True
            
            #when out of bound of board or r,c of board 
            if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or
            board[r][c] != word[i] or (r, c) in visited):
                return False
            
            #mark this box as visited
            visited.add((r, c))

            #search every dir from this box for the next letter
            #if any dir is true, we found the next letter
            #found is the total outcome of the 4 dir search. 
            found = (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)
            )

            #after seraching all we bubble back up, this is so that other times when backtracking is called
            #this cell can be used. After the entire check of a cell, we clean up all visited to ensure next time
            #checking for cells we can use the same cells
            visited.remove((r, c))
            #passing the signal to previous call
            return found
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                #put backtrack here so that we check every cell's so that we don't just check
                #the first cell that match the first letter, if it fails we continue to go through
                #the graph
                if board[r][c] == str(word[0]) and backtrack(r, c, 0):
                    return True
        return False

                    

