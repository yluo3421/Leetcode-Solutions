class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        Bottom Up
        Define a function dp to return the maximum 
        coins obtainable, if we burst all balloons 
        on the interval [left, right], inclusively.

        The base case is that the interval is empty,
        which yields 0 coin.

        For general cases, we iterate over every 
        index i in [left, right], and mark the balloon 
        at that index as the last one burst.

        First, We burst all balloons expect the ith one. 
        What we gain is:

        dp(left, i - 1) + dp(i + 1, right)
        Then, we burst the ith one:

        nums[left - 1] * nums[i] * nums[right + 1]
        Just return the maximum sum of those two among all possible is.

        Finally, return dp(1, len(dp) - 2).

        Do not return dp(0, len(dp) - 1) since the 
        first and the last balloons were added by us and we cannot burst them.
        """
        # special case
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        # handle edge case
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[i][j] represents
        # maximum if we burst all nums[left]...nums[right], inclusive
        dp = [[0] * n for _ in range(n)]

        # do not include the first one and the last one
        # since they are both fake balloons added by ourselves and we can not
        # burst them
        for left in range(n - 2, 0, -1):
            for right in range(left, n - 1):
                # find the last burst one in nums[left]...nums[right]
                for i in range(left, right + 1):
                    # nums[i] is the last burst one
                    gain = nums[left - 1] * nums[i] * nums[right + 1]
                    # recursively call left side and right side
                    remaining = dp[left][i - 1] + dp[i + 1][right]
                    # update
                    dp[left][right] = max(remaining + gain, dp[left][right])
        # burst nums[1]...nums[n-2], excluding the first one and the last one
        return dp[1][n - 2]
    
        """
        Top Down
        Time O(n^3) | Space O(n^2)
        """
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
        
        nums = [1] + nums + [1]
        
        @lru_cache(None)
        def dp(left, right):
            # reach maximum if we burst all nums[left]...nums[right]
            # inclusive
            if right - left < 0:
                return 0
            
            # find the last burst one in [left...right]
            result = 0
            for i in range(left, right + 1):
                # if nums[i] is the last burst one
                gain = nums[left - 1] * nums[i] * nums[right + 1]
                
                remaining = dp(left, i - 1) + dp(i + 1, right)
                result = max(result, remaining + gain)
            return result
        # we can not burst the first one and the last one
        # since they are both fake balloons added by ourselves
        return dp(1, len(nums) - 2)