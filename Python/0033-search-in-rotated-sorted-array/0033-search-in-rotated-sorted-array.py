class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(N)
        # array has to be sorted
        # left, right = 0, len(nums)
        # mid = (left + right) // 2 math.floor()
        # nums[mid] == target, return mid
        # nums[mid] < target by moving left pointer to index of mid + 1
        # nums[mid] > target by moving right pointer to index of mid - 1
        # O(log(N))
        
        """
        thoughts
        to find the pivot point by binary search then go for the correct half
        to perform another round of binary search until target found
        
        """
        
        
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # left sorted
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # right sorted
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
        
    