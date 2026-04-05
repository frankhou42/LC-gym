"""
Sol:
go through each element if its marked as 1 do a dfs and mark all surroundings
as 0s.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        def mark(r, c):
            #base case stop condition
            if not (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1"):
                return #tells func to stop

            #Recursive case
            grid[r][c] = "0"
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in dirs:
                mark(r + dr, c + dc) 

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    mark(r, c)
                    islands += 1
        
        return islands