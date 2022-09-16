class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n-1
        top = 0
        bottom = m-1
        
        while left < right and top < bottom:
            
            # left to right
            for i in range(left, right+1):
                result.append(matrix[top][i])
            
            top += 1
            
            # top to bottom
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            
            right -= 1
            
            # right to left
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            
            bottom -= 1
            
            # bottom to top
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            
            left += 1
        
        # if there are still remaining num in the matrix
        if len(result) < m * n:
            for row in range(top, bottom+1):
                for col in range(left, right+1):
                    result.append(matrix[row][col])
    
        return result