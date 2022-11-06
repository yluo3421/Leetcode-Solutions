from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    """
    双指针做法
    O(n^2) Time | O(1) Space
    """
    def minimum_size(self, nums: List[int], s: int) -> int:
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        
        n = len(nums)
        minLength = n + 1
        total_sum = 0
        j = 0
        for i in range(n):
            while j < n and total_sum < s:
                total_sum += nums[j]
                j += 1
            if total_sum >= s:
                minLength = min(minLength, j - i)
            total_sum -= nums[i]
        if minLength == n + 1:
            return -1
        return minLength

    