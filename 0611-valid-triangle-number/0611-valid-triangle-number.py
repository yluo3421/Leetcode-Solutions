class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # take all combinations
        # and sort and check if they match a + b > c
        # this method exceeds time limit
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            k = i + 2
            j = i + 1
            while j < len(nums) - 1 and nums[i] != 0:
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                count += k - j - 1
                j += 1
        return count
        
        
        """
        def combination(nums, k):
            ans = []
            def helper(ans, nums, combination, k):
                if len(combination) == k:
                    ans.append(combination)
                    return
                for i in range(len(nums)):
                    
                    
                    helper(ans, nums[i+1:], combination+[nums[i]], k)
            
            helper(ans, nums, [], k)
            return ans
        
        all_combinations = combination(nums, 3)
        
        ans = []
        for comb in all_combinations:
            comb.sort()
            if comb[0] + comb[1] > comb[2]:
                ans.append(comb)
        return len(ans)
        """
        
    
    