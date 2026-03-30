class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #1. Count all fresh fruits and put rotten fruit coordinate in q
        #2. multi-source BFS, for each fruit turn rotten decrement counter
        #3. Each layer added increment minutes by 1
        #4. If count of fresh = 0, return minutes, If q is empty but still fresh return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0
        q = deque()
        visited = set()
        

        def addRotten(r, c):
            nonlocal count
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r, c) in visited):
                return
            count -= 1
            q.append((r, c))
            visited.add((r, c))
            


        #1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
        
        #2
        minute = 0
        while q and count != 0:
            #each layer
            for i in range(len(q)):
                r, c = q.popleft()
                addRotten(r + 1, c)
                addRotten(r - 1, c)
                addRotten(r, c + 1)
                addRotten(r, c - 1)
            minute += 1



            

        return minute if count == 0 else -1
            
        

