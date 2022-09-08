class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if the nums[left] < nums[right] meaning the array is sorted
        # update the ans to the min of (ans and nums[mid])
        # if nums[mid] >= num[left] meaning array is rotated
        # that the min is in the right half of mid
        # else meaning the min is in the left half of mid
        left, right = 0, len(nums) - 1
        ans = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                ans = min(nums[left], ans)
                break

            mid = (left + right) // 2
            ans = min(nums[mid], ans)

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return ans