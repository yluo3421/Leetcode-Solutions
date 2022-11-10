from typing import (
    List,
)

class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    """
    thoughts
    find the total sum of the array,
    if its odd, return -1
    if its even, find the subarray that can make sum / 2

    """
    def can_partition(self, nums: List[int]) -> bool:
        total_sum = sum()
        if total_sum % 2 == 1:
            return False
        total = total_sum // 2
        dp = [False for _ in range(total + 1)]
        dp[0] = True
        for i in range(len(nums)):
            for j in range(total, nums[i] - 1, -1):
                if dp[j - nums[i]]:
                    dp[j] = True
        return dp[total]


