class Solution:
    """
    @param n: int
    @param k: int
    @param r: int
    @param c: int
    @return: the probability
    """
    def knight_probability(self, n: int, k: int, r: int, c: int) -> float:
        # Write your code here.
        # dp[step][i][j] to represent the possibility that knight is 
        # still on the board with current step
        # at position i,j
        # if step == 0, dp[i][j] = 1
        # if knight is out of board, dp[i][j] = 0
        # dp[step][i][j] = 1/8 * sum (dp[step - 1][i + di][j + dj])
        # di, dj has 8 combinations
        DIRECTIONS = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        for step in range(k + 1):
            for i in range(n):
                for j in range(n):
                    if step == 0:
                        dp[step][i][j] = 1
                    else:
                        for di, dj in DIRECTIONS:
                            new_i, new_j = i + di, j + dj
                            if new_i in range(n) and new_j in range(n):
                                dp[step][i][j] += dp[step - 1][new_i][new_j] / 8
        return dp[k][r][c]