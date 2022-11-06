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
    O(n) Time | O(1) Space
    """
    def minimum_size(self, nums: List[int], s: int) -> int:
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        
        n = len(nums)
        minLength = float("inf")
        total_sum = 0
        end = 0
        for start in range(n):
            while end < n and total_sum < s:
                total_sum += nums[end]
                end += 1
            if total_sum >= s:
                minLength = min(minLength, end - start)
            total_sum -= nums[start]
        if minLength == float("inf"):
            return -1
        return minLength

    """
    [2,3,1,2,4,3], s = 7
       ^
             ^
    start = 0
    end = 4     
    total_sum = 10
    minLength = 3
    """
    