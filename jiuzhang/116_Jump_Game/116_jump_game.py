from typing import (
    List,
)

class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    # Greedy
    def can_jump(self, a: List[int]) -> bool:
        # write your code here
        # DP
        dp = [False] * len(a)
        dp[0] = True
        for i in range(len(a)):
            for j in range(i):
                if dp[j] and j + a[j] >= i:
                    dp[i] = True
                    break
        return dp[len(a) - 1]

        # Greedy
        farthest = a[0]
        for i in range(len(a)):
            if i <= farthest and i + a[i] > farthest:
                farthest = i + a[i]
        return farthest >= len(a) - 1
    
    
