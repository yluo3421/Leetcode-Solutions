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
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]