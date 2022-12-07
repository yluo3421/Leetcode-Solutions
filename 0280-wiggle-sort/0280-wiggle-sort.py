class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # first thoughts:
        # sort the nums and swap every pair
        direction = True # nums[i] <= nums[i + 1]
        for i in range(len(nums) - 1):
            if direction:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            direction = not direction
        return nums
                    
                
            
