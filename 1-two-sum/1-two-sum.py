class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hashmap:
                return [i, hashmap[temp]]
            hashmap[nums[i]] = i