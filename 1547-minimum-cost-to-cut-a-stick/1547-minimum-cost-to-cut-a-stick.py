class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0, n]); cuts.sort(); m = len(cuts)        
        dp = [[0] * m for _ in range(m)]
        for l in range(2, m):
            for i in range(m-l):
                j = i + l                        
                dp[i][j] = min(cuts[j] - cuts[i] + dp[i][k] + dp[k][j] for k in range(i+1, j))
        return dp[0][-1]