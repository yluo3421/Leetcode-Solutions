class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        dp[0] = largest sum which is divisible by 3
        dp[1] = largest sum when divided by 3, remainder = 1
        dp[2] = largest sum when divided by 3, remainder = 2
        """
        dp = [0, 0, 0]
        for num in nums:
            for i in dp[:]:
                dp[(i + num) % 3] = max(dp[(i + num) % 3], i + num)
        return dp[0]