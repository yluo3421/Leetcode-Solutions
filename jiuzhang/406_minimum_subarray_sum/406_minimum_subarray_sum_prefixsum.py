from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    这个方法使用了前缀和
    O(n^2) Time | O(n) Space
    O(n)计算前缀和， O(n^2)遍历start和end
    
    """

    def minimum_size(self, nums: List[int], s: int) -> int:
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        
        n = len(nums)
        minLength = float("inf")
        prefix_sum = self.get_prefix_sum(nums)
        for start in range(n):
            for end in range(start, n):
                if prefix_sum[end + 1] - prefix_sum[start] >= s:
                    minLength = min(minLength, end + 1 - start)
        if minLength == float("inf"):
            return -1
        return minLength

    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for i in range(1, len(nums) + 1):
            prefix_sum.append(prefix_sum[i - 1] + nums[i - 1])
        return prefix_sum

    