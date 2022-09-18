class Solution:
    def maxArea(self, height: List[int]) -> int:
        # use two pointer from both sides
        # if left pointer is shorter, move left +1
        # if right pointer is shorter, move right -1
        # if they are the same, move right -1
        # use max to record max area
        # area = min height of the two pointer * distance between two pointer
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return res