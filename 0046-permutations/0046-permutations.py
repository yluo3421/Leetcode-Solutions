class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        self.dfs(nums, path, ans)
        return ans
    
    def dfs(self, nums, path, ans):
        if not nums:
            ans.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], ans)