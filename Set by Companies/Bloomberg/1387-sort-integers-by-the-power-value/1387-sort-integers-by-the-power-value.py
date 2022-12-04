class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """
        Thoughts:
        get power of value by helper function
        Then sort them by orders.
        I think this dfs of getting power value can be simplified
        using some memorization.
        Cause numbers like 2,4,8 will be calculated multiple times
        I want to create a dictionary and store the integer and
        its power value
        
        """
        dp = {}
        def power_value(x):
            y, result = x, 0
            while x > 1 and x not in dp:
                result += 1
                if x % 2:
                    x = 3*x + 1
                else:
                    x //= 2
            dp[y] = result + (dp[x] if x > 1 else 0)
            return dp[y], y
        
        return sorted(range(lo, hi+1), key=power_value)[k-1]
        
        
        