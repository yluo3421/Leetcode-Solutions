class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # i = 0
        # while i < len(nums):
        #     if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
        #         nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        #     else:
        #         i += 1
        # for i in range(len(nums)):
        #     if nums[i] != i + 1:
        #         return (i + 1)
        # return len(nums) + 1
        n = len(nums)
        
        # First put each number in range 1 to n at its correct place
        i = 0
        
        while i < n:
            # Swap
            # Only for the range 1 to n check if a number at any index is not at its correct place
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i]= nums[i], nums[nums[i] - 1]
            else:
                i += 1
        
        # And now just find the first missing number. That would be the smallest
        for i,num in enumerate(nums):
            if num != i + 1: return i + 1
        
        # Otherwise the missing positive number is n + 1 (e,g, for testcases such as [1])
        return n + 1
                