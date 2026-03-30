class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() # set is used for O(1) look up
        maxArea = 0

        #Find total area of the island and 
        #update max if necessary
        def dfsArea(r, c) -> int:
            #base case
            #if out of bound or has been visited or not an island
            #stop searching this path
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
               grid[r][c] == 0 or (r, c) in visited):
               return 0
            
            #check if cell is valid area
            if (r, c) not in visited:
                #mark visited
                visited.add((r, c))
                return (1 + dfsArea(r + 1, c) + dfsArea(r - 1, c) 
                        + dfsArea(r, c + 1) + dfsArea(r, c - 1) )
        
        for r in range(ROWS):
            for c in range(COLS):
                #new island found! mark land area and update
                #the max area
                if (grid[r][c] == 1 and (r, c) not in visited):
                    area = dfsArea(r, c)
                    if area > maxArea:
                        maxArea = area
                
        return maxArea

        #Time Complexity: O(m*n), traversing the whole grid
        #Space Complexity: O(m*n), call stack is the whole grid if the grid is all land