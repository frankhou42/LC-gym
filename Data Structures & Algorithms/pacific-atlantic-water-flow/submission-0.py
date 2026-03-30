class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """itereate through each border cells and dfs every cell
        and mark each cell as can be flown into ocean if it is greater
        than the value of the current cell. stop if the next cell is smaller
        than the current cell. Compile two lists of cells that can be flown to pacific
        and atlantic and find the common cells from that list as output """

        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()
        res = []
    
        def mark(r, c, ocean) -> None:
            ocean.add((r, c))
            #explore each possible dirs
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for d in dirs:
                new_r = r + d[0]
                new_c = c + d[1]
                if (0 <= new_r <= ROWS - 1) and (0 <= new_c <= COLS - 1) and heights[new_r][new_c] >= heights[r][c] and (new_r, new_c) not in ocean:
                    ocean.add((new_r, new_c))
                    mark(new_r, new_c, ocean)   

        for r in range(ROWS):
            #dfs mark from taht cell to see all the cells that can flow into pacific ocean
            mark(r, 0, pacific)
            mark(r, COLS - 1, atlantic)

        for c in range(COLS):
            mark(0, c, pacific)
            mark(ROWS - 1, c, atlantic) 

        for coordinate in pacific:
            if coordinate in atlantic:
                res.append(coordinate)
        
        return res

        """
        Reflection: 
        1. DFS solution not BFS as this uses recursion to go down a path and return, BFS would be queue
        2. Mark the cell as we go
        3. Keep marking cells that fulfills requirement, if none is met check next direction cell, if all doesn't fullfill function is complete
        4. When solving DFS problems, always mark a node as visited as soon as you enter it.
        5. If your traversal logic depends on global order instead of local recursion order, your DFS logic is probably wrong.
        """