class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c) -> None:
            #base case
            #if out of bounds of island area or has been visited, stop!
            if (r < 0 or r == rows or c < 0 or c == cols or
                grid[r][c] == '0' or (r, c) in visited):
                return
            
            #if node hasn't been visited we dfs to all 4 directions
            #to continue find parts of island
            if (r, c) not in visited:
                visited.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

         
        for r in range(rows):
            for c in range(cols):
                #visit each cell and check if it has not been visited
                #and is "1" -> increment count and bfs to mark all the 
                #"1"s on the island
                if (r,c) not in visited and grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count 