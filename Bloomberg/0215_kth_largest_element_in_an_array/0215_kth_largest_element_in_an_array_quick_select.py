class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # thoughts:
        # use quick select 
        # go through the array and fin elements that is
        # larget than pivot, equal to pivot, less than pivot
        # left,   mid,   right
        # if k < len(left), search in left
        # if k > len(left) and k < len(left) + len(mid)
        # return mid[0]
        # if k > len(left) + len(mid)
        # search in right
        if not nums:
            return 
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        L = len(left)
        M = len(mid)
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]