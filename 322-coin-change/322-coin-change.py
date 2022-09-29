class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # thoughts:
        #                 11
        #        1            2           5
        #  1  2  5          1 2 5      1 2 5
         
        # O(n^h) every level has n choices (where n is different coins we have)
        # h will be the number of choice we need to make
        
        # check the biggest coins I can use with this amount
        # for i in range(coins):
        # find the max_coin
        # amount -= max_coin
        # find max_coin in the new amount
        # until amount = 0
        # use an array to store what coin was chosen and return len()
        
        
#         def find_max_coin(coins, amount):
#             max_coin = 0
#             coins.sort()
#             for coin in coins:
#                 if amount >= coin:
#                     max_coin = coin
#                 else:
#                     break
#             if max_coin == 0:
#                 return max(coins)
#             return max_coin
        
#         ans = []
#         while amount > 0:
#             max_coin = find_max_coin(coins, amount)
#             amount -= max_coin
#             ans.append(max_coin)
#         print(ans)
#         if amount < 0:
#             return -1
#         if amount == 0:
#             return len(ans)
        
        # dp total number of coins used so far for the amount
        # index of dp representing the amount 
        # dp(amount) = min(dp(amount - coin in coins) + 1)
        # coins = [1,2,5]
        # dp = [0, 1, 1, 2]
        # dp[1] = dp[1 - 1] + 1
        #       = dp[0] + 1
        # dp[2] = dp[2 - 2] + 1 or dp[2 - 1] + 1
        #       = min(dp[0] + 1 or dp[1] + 1)
        #       = 1
        # dp[3] = dp[3 - 2] + 1 or dp[3 - 1] + 1
        #       = min(dp[1] + 1, dp[2] + 1)
        #       = 2
        # dp[11] = min(dp[11 - 5] + 1 or dp[11 - 2] + 1 or dp[11 - 1] + 1)
        
        # find out the dp expression
        # intiate the dp array with some inital value 
        # populate the dp array to find the answer
        dp = [(amount + 1) for _ in range(amount + 1)]
        dp[0] = 0
        i = 1 
        while i < amount + 1:
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
            i += 1
        return dp[amount] if dp[amount] != amount + 1 else -1
#                     if dp[i - coin] == -1:
#                         array.append(-1)
#                     else:
#                         array.append(dp[i - coin] + 1)
#             if not array:
#                 dp[i] = -1
#             else:
#                 dp[i] = min(array)
#             i += 1
        
#         return dp[amount]
#         # dp[0,-1,1,]
            