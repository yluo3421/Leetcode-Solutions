class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        """
        The idea of matrix mutplication is ans[i][j] = sum of product
        of elements of ith row of mat1 and jth column of mat2
        brutal force we can have this multiplication
        And if one of the element is 0, we dont need to
        do it because the whole row or col result will be 0
        
        This way it will be Time O(m*k*n) | Space O(1)
        """
        
        # brutal force
        n = len(mat1) # number of rows in mat1
        m = len(mat1[0]) # should be len(mat2)
        k = len(mat2[0]) # number of colmns in mat2
        ans = [[0] * k for _ in range(n)]
        
        for row_idx, row_elements in enumerate(mat1):
            for element_idx, row_element in enumerate(row_elements):
                if row_element:
                    for col_idx, col_element in enumerate(mat2[element_idx]):
                        ans[row_idx][col_idx] += row_element * col_element
        return ans
    
        """
        beyond this point
        if we have a large matrix over memory we can store
        Since 0 element is not useful maybe we can delete them?
        That way I still need the information of non-zero element
        I can store a tuple of (value, column) into row array
        """
        def compress_matrix(matrix):
            rows, cols = len(matrix), len(matrix[0])
            compressed_matrix = [[] for _ in range(rows)]
            for row in range(rows):
                for col in range(cols):
                    if matrix[row][col]:
                        compressed_matrix[row].append([matrix[row][col], col])
            return compressed_matrix
        
        n = len(mat1) # number of rows in mat1
        m = len(mat1[0]) # should be len(mat2)
        k = len(mat2[0]) # number of colmns in mat2
        ans = [[0] * k for _ in range(n)]
        
        alpha = compress_matrix(mat1)
        beta = compress_matrix(mat2)
        for mat1_row in range(n):
            for element1, mat1_col in alpha[mat1_row]:
                for element2, mat2_col in beta[mat1_col]:
                    # multiply and add all non-zero elements of mat2
                    # where the row is equal to col of current element of mat1
                    ans[mat1_row][mat2_col] += element1 * element2
        