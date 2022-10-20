class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # for each value, we use as little amount of coins as possible
        # dp representing the amount of coins need to make i value
        # dp[i] = 1 + dp[i - coin]
        dp = [(amount + 1) for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != (amount + 1) else -1
    
        # i  0 1 2 3 4 5 6 7 8 9 10 11
        # dp 0 1 1 2 