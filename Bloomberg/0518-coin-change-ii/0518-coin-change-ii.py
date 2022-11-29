class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # use dp to solve this
        # dp represents number of ways to make up the amount i
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(1, amount + 1):
                if j >= coin:
                    dp[j] += dp[j - coin]
        return dp[-1]