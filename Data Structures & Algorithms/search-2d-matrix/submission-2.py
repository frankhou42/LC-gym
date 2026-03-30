class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        #find the row tgt belongs
        topRow, botRow = 0, ROWS - 1
        tgtRow = -1
        while topRow <= botRow:
            midRow = (topRow + botRow)//2
            #if in row range, return. (since its sorted)
            if matrix[midRow][0] <= target <= matrix[midRow][COLS - 1]:
                tgtRow = midRow
                break # stop loop when found
            #when larger or smaller shift the size of window to search to half accordingly
            elif target < matrix[midRow][0]:
                botRow = midRow - 1
                #make sure change midRow so that it doesn't get stuck in cases where midRow is botRow and infinite loop
            elif target > matrix[midRow][COLS - 1]:
                topRow = midRow + 1
            elif tgtRow == -1:
                return False
        
        l, r = 0, COLS - 1
        #find the element in row
        while l <= r:
            m = (l + r)//2
            #found element
            if matrix[tgtRow][m] == target:
                return True
            elif matrix[tgtRow][m] > target:
                r = m - 1
            elif matrix[tgtRow][m] < target:
                l = m + 1
        return False


            


