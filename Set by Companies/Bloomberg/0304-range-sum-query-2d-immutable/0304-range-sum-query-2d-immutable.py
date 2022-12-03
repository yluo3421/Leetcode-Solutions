
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        brutal force will be just calculating all elements
        between two points.
        But to do better than O(n^2)
        We can learn from the prefix sum method
        here we use the each row as prefix sum
        
        so that the sum += each row prefix_sum[col2 + 1] - prefix_sum[col1]
        [[3, 0, 1, 4, 2], 
        [5, 6, 3, 2, 1], 
        [1, 2, 0, 1, 5], 
        [4, 1, 0, 1, 7], 
        [1, 0, 3, 0, 5]], 
        
        dp
        [[0, 3, 3, 4, 8, 10], 
        [0, 5, 11, 14, 16, 17], 
        [0, 1, 3, 3, 4, 9], 
        [0, 4, 5, 5, 6, 13], 
        [0, 1, 1, 4, 4, 9]]
        Time O(m) per query, initialization O(n*m)
        
        I can also try initialize it further more
        So time complexity becomes O(1) per query
        The idea is that the sum of a rectangle can be looked
        as a bigger rectangle minus some other rectangles
        [x,x,a,a,a,a
         b,b,c,c,c,c
         b,b,c,c,c,c
         b,b,c,c,c,c]
         if I want to calculate sum of all c
         it is equal to sum of all - sum of x - sum of a - sum of b
         I can take a, b, x as sub problem. emm wait
         this doesnt sound right
         Cause my previous idea is that they all start from origin
         But here a and b area are not 
         sum of all - sum(x+a) - sum(x+b) + sum(x)
         This way they are all from origin
         dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] - dp[i][j] + matrix[i][j]
         
         """
        n = len(matrix)
        m = len(matrix[0])
        if n == 0 or m == 0:
            return
        
        self.dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                self.dp[i + 1][j + 1] = self.dp[i + 1][j] + self.dp[i][j + 1] - self.dp[i][j] + matrix[i][j]
        print(self.dp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        brutal force will be just calculating all elements
        between two points.
        But to do better than O(n^2)
        We can learn from the prefix sum method
        here we use the each row as prefix sum
        
        so that the sum += each row prefix_sum[col2 + 1] - prefix_sum[col1]
        [[3, 0, 1, 4, 2], 
        [5, 6, 3, 2, 1], 
        [1, 2, 0, 1, 5], 
        [4, 1, 0, 1, 7], 
        [1, 0, 3, 0, 5]], 
        
        dp
        [[0, 3, 3, 4, 8, 10], 
        [0, 5, 11, 14, 16, 17], 
        [0, 1, 3, 3, 4, 9], 
        [0, 4, 5, 5, 6, 13], 
        [0, 1, 1, 4, 4, 9]]

        """
        n = len(matrix)
        m = len(matrix[0])
        if n == 0 or m == 0:
            return
        
        self.dp = [[0] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                self.dp[i][j + 1] = self.dp[i][j] + matrix[i][j]
        print(self.dp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            sum += self.dp[i][col2 + 1] - self.dp[i][col1]
        return sum
