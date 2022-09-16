class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # thougths:
        # go throught whole array
        # use two pointer
        # [0,0,1,1,1,1,2,3,3]
        #                ^
        #                    ^
        # number of duplicate of nums[left] is right - left
        # ans = []
        # if the right - left == 1
        # ans.append[]
        # if   >= 2
        # append two times
        left, right = 0, 1
        
        k = 0
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                if right - left == 1:
                    nums[k] = nums[left]
                    k += 1
                elif right - left >= 2:
                    nums[k] = nums[left]
                    k += 1
                    nums[k] = nums[left]
                    k += 1
                
                left = right
                right += 1
        if right - left == 1:
            nums[k] = nums[left]
            k += 1
        elif right - left >= 2:
                    nums[k] = nums[left]
                    k += 1
                    nums[k] = nums[left]
                    k += 1
        
        return k