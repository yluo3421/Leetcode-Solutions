class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # thoughts:
        # burtal 
        # sort and find consecutive sequence
        # [100,4,200,1,3,2]
        #   ^
        max_len = 0
        nums_set = set(nums)
        
        for num in nums:
            if num - 1 not in nums_set:
                curr_num = num
                curr_streak = 1
                
                while curr_num + 1 in nums_set:
                    curr_streak += 1
                    curr_num += 1
                max_len = max(max_len, curr_streak)
        return max_len