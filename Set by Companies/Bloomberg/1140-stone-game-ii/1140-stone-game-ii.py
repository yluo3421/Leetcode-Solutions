class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        dp[i, m] = maximum stones the current player can 
        get from piles[i:] with M=m
        A[i]= total stones of piles[i:]
        when current player pick stones from i to i+x-1
        -> the other player's stones: dp[i+x, max(m, x)]
        -> total stones of current player: A[i] - dp[i+x, max(m, x)]
        we want the current player gets maximum 
        means the other player gets minimum
        """
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]
            
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= n:
                return piles[i]
            return piles[i] - min(dp(i + x, max(m, x)) for x in range\
                                 (1, 2 * m + 1))
        return dp(0, 1)
        
        
        