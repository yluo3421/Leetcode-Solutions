class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # thoughts:
        # loop through the array, find the max from k elements
        # if every time check for max, it's going to be O(k * (n - k)) Time
        # to simplify the method
        # if the prev max is still in window
        # so every time compare the new number with the prev max
        # if the prev max is out of window, updated with the new max
        
        # better method, use stack to record max only,
        # every time we move window, peak stack to add to output array
        # array      [1, 3, -1, -3, 5, 3, 6, 7]
        # window      [         ]
        # stack       [3]
        
        output = []
        queue = collections.deque() #takes index
        left, right = 0, 0
        
        while right < len(nums):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            
            if left > queue[0]:
                queue.popleft()
            
            if right + 1 >= k:
                output.append(nums[queue[0]])
                left += 1
            right += 1
        return output
        