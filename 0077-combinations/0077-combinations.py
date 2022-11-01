class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # thoughts
        # pick a number from the 1,n, then pick the next number from the remaining list
        # use a count to check how many are chosen
        nums = [i for i in range(1, n + 1)]
        ans = []
        
        def helper(nums, ans, combination, k):
            if len(combination) == k:
                ans.append(combination)
            for i in range(len(nums)):
                helper(nums[i+1:], ans, combination + [nums[i]], k)
        helper(nums, ans, [], k)
        return ans