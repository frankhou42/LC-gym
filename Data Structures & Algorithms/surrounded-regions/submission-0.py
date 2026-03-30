class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        The core idea is that border cells gurantees that its not surrounded, but the inside
        cells doesn't gurantee its surrounded. Prioritize certainty over uncertainty
        """

        ROWS = len(board)
        COLS = len(board[0])

        not_surrounded_cells = set()

        #find all cells that is certainly not surrounded
        def dfs(r, c):
            not_surrounded_cells.add((r, c))
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for d in directions:
                new_r = r + d[0]
                new_c = c + d[1]
                #in grid and not in set and is "O"
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in not_surrounded_cells and board[new_r][new_c] == "O":
                    dfs(new_r, new_c)


        for r in range(ROWS):
            for c in range(COLS):
                #only border AND!!! "O" cells
                if not(1 <= r < ROWS - 1 and 1 <= c < COLS - 1) and board[r][c] == "O":
                    dfs(r, c) #find all not surrounded cells
        
        for r in range(ROWS):
            for c in range(COLS):
                #if the cell is definitely not a not surrounded cell
                if (r, c) not in not_surrounded_cells:
                    board[r][c] = "X"


        """
        Reflection:
        1. Intuition on using border cell that gurantees that counter opposite to then prove
        instead of using potentially defect interior cells
        2. DFS from only border cells that are "O"
        3. We can still use intutiive approach, it is just that when we hit a cell that is
        not correct we have to backtrack, messy logic.
        """

        """
        DFS vs BFS
        DFS: Depth first, uses less memory
        BFS: Gurantees shortest path for unweighted graph, but uses more memory
        """

            

                

        