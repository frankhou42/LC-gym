class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        #multi-source BFS
        visited = set()

        def addNode(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited 
                or grid[r][c] == -1):
                    return
            visited.add((r, c))
            q.append((r, c))


        #add treasure to queue
        q = deque() # q = [(0,2), (1,3)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        #BFS for each node
        dist = 0 #BFS from each source have same layer dist
        while q:
            #nodes in layers of each source
            for i in range(len(q)):
                r, c = q.popleft()
                #set node dist
                grid[r][c] = dist
                #add next layer
                addNode(r + 1, c)
                addNode(r - 1, c)
                addNode(r, c + 1)
                addNode(r, c - 1)
            dist += 1
                
            
                



