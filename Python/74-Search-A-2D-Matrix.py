class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int)-> bool:
        num_row = len(matrix)
        num_col = len(matrix[0])
        top, bot = 0, num_row - 1

        while top <= bot:
            row_mid = (top + bot) // 2
            if matrix[row_mid][-1] < target:
                top = row_mid + 1
            elif matrix[row_mid][0] > target:
                bot = row_mid - 1
            else:
                break
        
        row = (top + bot) // 2
        left, right = 0, num_col - 1
        while left < right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True
        return False
