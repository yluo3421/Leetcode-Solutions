class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [0]*len(nums)
        dp[-1] = nums[-1]
        dp[-2] = nums[-2]
        for i in range(len(nums)-3, -1, -1):
            dp[i] = max(nums[i], nums[i] + max(dp[i+2:]))
        return max(dp[0], dp[1])