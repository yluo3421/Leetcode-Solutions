from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    双指针加上前缀和加上二分法
    二分法是因为前缀和在这里是一个单调递增的数组
    O(nlog(n)) Time | O(n) Space
    """
    def minimum_size(self, nums: List[int], s: int) -> int:
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        
        n = len(nums)
        minLength = float("inf")
        prefix_sum = self.get_prefix_sum(nums)
        for start in range(n):
            # find the end pointer, which makes sum of nums from start to end
            # is less than s
            # nums[end] is included in sum, end is idx for nums
            # end is not idx for prefixSum
            end = self.getEndOfSubarray(prefix_sum, start, s)
            # because returned right might not meet requirement
            # we need to double check the end returned
            if prefix_sum[end + 1] - prefix_sum[start] >= s:
                minLength = min(minLength, end - start + 1)
        if minLength == float("inf"):
            return -1
        return minLength

    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for i in range(1, len(nums) + 1):
            prefix_sum.append(prefix_sum[i - 1] + nums[i - 1])
        return prefix_sum
    
    def getEndOfSubarray(self, prefix_sum, start, s):
        left = start
        right = len(prefix_sum) - 2 # n - 1 = len(prefix_sum) - 2
        while left + 1 < right:
            
            mid = (left + right) // 2
            
            # if sum of nums from start to mid >= s, discard right
            # keep looking for shorter subarray
            # mid needs to be added with 1, because we want sum to include nums[mid]
            if prefix_sum[mid + 1] - prefix_sum[start] >= s:
                right = mid
            else:
                # if sum of nums from start to mid < s, discard left part
                left = mid
        # if left pointer satisfies, return left first, because it is shorter subarray
        if prefix_sum[left + 1] - prefix_sum[start] >= s:
            return left
        # if left not good, return right(right might not satisfy either)
        return right

    