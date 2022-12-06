class Solution:
    def minimumTime(self, s: str) -> int:
        """
        Thoughts:
        Everytime we have three choices, to reach the best result
        This sounds like to me a dp problem
        I think for those consecutive 1 from both end
        We are able to remove them at 1 unit time
        While for the other one in between, we have to use 2 unit time
        So this game turns into
        | left | middle | right |
        where left and right are consecutive ones
        we need to find out len(left) + 2 * count(middle, 1) + len(right)
        = len(left) + len(middle) + len(right) + 2 * count(middle, 1) - 
        len(middle)
        because len(middle) = count(middle, 1) + count(middle, 0)
        so that = n + count(middle, 1) - count(middle, 0)
        This way means
        we need to find the smallest subarray with smallest
        count(middle, 1) - count(middle, 0) value
        """
        def minSum(nums):
            dp = [0]*len(nums)
            dp[0] = nums[0]
            for i in range(1, len(nums)):
                dp[i] = min(nums[i], nums[i] + dp[i-1])
            return min(0, min(dp))

        n = len(s)
        s1 = [1 if i == "1" else -1 for i in s]
        score = minSum(s1)
       
        return n + score
        
        