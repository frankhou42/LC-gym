"""
multisource bfs

add the coordinates of the 0s into the q and do bfs for 
each

No need for visisted as we only add cells who are infinity
each cell is updated by adding one to the previous cell

q holds all coord
"""
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        
        #find all treasure chests
        ROWS = len(grid)
        COLS = len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        #bfs
        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))