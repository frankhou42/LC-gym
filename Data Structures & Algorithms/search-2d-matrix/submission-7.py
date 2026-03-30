"""
first we conduct binary search to find the correct row for tgt then we
do another binary search to find the tgt in that row 

log(m) + log(n) = log(m * n)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        l, r = 0, len(matrix) - 1
        #considered l == r base case for while loop condition
        while l <= r:
            mid = (l + r)//2
            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[0]) - 1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][len(matrix[0]) - 1]:
                l = mid + 1

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r)//2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return False

            