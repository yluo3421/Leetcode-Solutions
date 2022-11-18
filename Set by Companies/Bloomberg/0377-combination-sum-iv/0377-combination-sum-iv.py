class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # use a dp to do this
        # dp[i] represents number of combinations that can add to target
        # for all num in nums
        # dp[i] += dp[i - num]
        # number of combination for dp[0] = 1
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        print(dp)
        return dp[target]