class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        # brutal thoughts
        # use dfs to find all paths and push all sum into an array
        # check each item in array if divisble by k
        ROW = len(grid)
        COL = len(grid[0])
        MOD = 10 ** 9 + 7
        def dfs(i, j, current):
            current += grid[i][j]
            current %= k
            if i == ROW - 1 and j == COL - 1:
                if current == 0:
                    return 1
                return 0
            total = 0
            if i + 1 < ROW:
                total += dfs(i + 1, j, current)
            if j + 1 < COL:
                total += dfs(i, j + 1, current)
            return total % MOD
        return dfs(0, 0, 0) % MOD
        # this method will run over time limit
        # DP needed to solve this
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        ROW, COL = len(grid), len(grid[0])
        MOD = 10 ** 9 + 7
        dp = [[[0] * k for _ in range(COL)] for _ in range(ROW)]
        dp[0][0][grid[0][0] % k] = 1

        for row in range(ROW):
            for col in range(COL):
                for v in range(k):
                    curr = (v + grid[row][col]) % k
                    if row > 0:
                        dp[row][col][curr] += dp[row - 1][col][v]
                    if col > 0:
                        dp[row][col][curr] += dp[row][col - 1][v]
        return dp[ROW - 1][COL - 1][0] % MOD
        # O(m * n * k) Time | O(m * n * k) Space

            
            
            
            