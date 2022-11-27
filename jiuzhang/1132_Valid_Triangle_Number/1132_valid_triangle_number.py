from typing import (
    List,
)

class Solution:
    """
    @param nums: the given array
    @return:  the number of triplets chosen from the array that can make triangles
    """
    def triangle_number(self, nums: List[int]) -> int:
        # Write your code here
        # we can sort it and find all three combinations
        # check all of them and see which are met
        # while 
        
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            k = i
            for j in range(i + 1, n):
                while k + 1 < n and nums[k + 1] < nums[i] + nums[j]:
                    k += 1
                ans += max(k - j, 0)
        return ans
    """
    
    """