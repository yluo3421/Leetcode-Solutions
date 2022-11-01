class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # thoughts:
        # for each cell we have two choices, if the next cell
        # is out of range, return 0
        # if curr row, col == m - 1, n - 1
        # means we reach the target
        # using 2D dp, dp[i][j] representing num of unique ways to this cell
        # dp[i][j] = dp[i - 1][j] + dp[j - 1][i]
        # initialize row = 0 and col = 0 to 1 because 
        # we can only move right or down, so only 1 way to get to them
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]