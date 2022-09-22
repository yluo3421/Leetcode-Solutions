class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # thoughts:
        # sort the array and return k-1 element in the array
        # O(log(n)) time | O(1) space
        nums.sort()
        print(nums)
        return nums[len(nums) - (k)]

        # other thoughts
        # use minHeap to extract min k-1 one times
        