class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # using dynamic programming
        # dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        # use a max_square_side to record the current max
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        max_square_side = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_square_side = max(max_square_side, dp[i][j])
        return max_square_side * max_square_side
                        
        
    """
    
        # largest square meaning, if I find i,j
        # [i][j] to [i+m][j+m] are all 1s. The max size is max m
        # cannot use visited to elminate duplicates
        # brutal force
        # go through all items
        # if found a 1, check till i+m, j+m
        # inside check square, we can use visited to avoid duplicates
        def check_square(matrix, max_square_side, visited, ijStack):
            while ijStack:
                [i, j] = ijStack.pop()
                if i + max_square_side > n or j + max_square_side > m:
                    return max_square_side - 1
                neighbors = [[0, 1], [1, 1], [1, 0]]
                for neighbor in neighbors:
                    new_row = i + neighbor[0]
                    new_col = j + neighbor[1]
                    stack = []
                    if (new_row, new_col) in visited:
                        continue
                    if matrix[new_row][new_col] == 0:
                        return max_square_side - 1
                    else:
                        visited.add((new_row, new_col))
                        stack.append([new_row, new_col])
            return check_square(matrix, max_square_side + 1, visited, stack)
            
                
        n = len(matrix)
        m = len(matrix[0])
        max_square_side = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    visited = set((i,j))
                    ijStack = []
                    ijStack.append([i, j])
                    max_square_side = check_square(matrix, 1, visited, ijStack)
        return max_square_side
    """
        
                    