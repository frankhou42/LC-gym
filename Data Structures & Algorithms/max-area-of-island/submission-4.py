class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        max_area = 0
        visited = set()
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
 
        #return area of island
        def dfs(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1 and (r, c) not in visited):
                return 0
            
            visited.add((r, c))

            area = 1
            for dr, dc in dirs:
                area += dfs(r + dr, c + dc)
            
            return area


            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(dfs(r, c), max_area)
        
        return max_area