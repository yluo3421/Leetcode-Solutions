class Solution:
    def rob(self, nums: List[int]) -> int:
        # it's similar to the first version but now the last house
        # is connected to the first house.
        # to avoid alert, if last house needs to be robbed to get max
        # the first house cannot be robbed. vice versa
        # we could run house robber I method on two arrays 
        # includind/excluding first house
        if len(nums) == 1:
            return nums[0]
        return max(self.findMaxRob(nums[1:]), self.findMaxRob(nums[:-1]) )
        
    def findMaxRob(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]