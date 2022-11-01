class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # its each element, choose or not
        # call combination n times to find all of them
        ans = []
        for i in range(len(nums) + 1):
            sub = combinations(nums, i)
            ans += sub
        return ans
            
    def combinations(self, nums, k):
        def helper(nums, combination, ans, k):
            if len(combination) == l:
                ans.append(combination)
                return
            for i in range(len(nums)):
                helper(nums[i+1:], combination + [nums[i]], ans, k)
        ans = []
        helper(nums, [], ans, k)
        return ans

        