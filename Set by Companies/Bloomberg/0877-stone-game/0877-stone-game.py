class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        Thoughts
        For alice to win, after she takes one, the next round
        Bob can only found lower or equal picks
        Actually we can use a dp and change the game to
        the number of stones Bob picks will be deducted from
        Alice's score. This becomes calculating the max score
        Alice can reach at the end
        
        """
        n = len(piles)
        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            parity = (j - i - n) % 2
            if parity == 1:
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:
                return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))
        return dp(0, n - 1) > 0