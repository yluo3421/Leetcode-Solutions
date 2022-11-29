class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def min_cut(self, s: str) -> int:
        # write your code here
        # dp[i] representing the min number of ways to partition string to all 
        # palindromes
        # first we need to go through the stirng once
        # if dp[j:i] is palindrome, we can confirm dp[i] = dp[j] + 1
        # so with the information we can derive dp[i] = min(dp[i], dp[j + 1] + 1)
        
        n = len(s)
        dp = []
        p = [[False for _ in range(n)] for _ in range(n)]

        # dp[n] = -1
        for i in range(n + 1):
            dp.append(n - 1 - i)

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if (s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1])):
                    p[i][j] = True
                    dp[i] = min(dp[i], dp[j + 1] + 1)
        print(dp)
        return dp[0]

        
