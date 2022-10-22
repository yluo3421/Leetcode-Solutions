class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # its each element, choose or not
        # call combination n times to find all of them
        ans = []
        for i in range(len(nums) + 1):
            sub = self.combinations(nums, i)
            ans += sub
        return ans
            
    
    def combinations(self, nums, k):
        def helper(nums, ans, path, k):
            if len(path) == k:
                ans.append(path)
                return
            for i in range(len(nums)):
                helper(nums[i+1:], ans, path + [nums[i]], k)
        
        ans = []
        helper(nums, ans, [], k)
        return ans