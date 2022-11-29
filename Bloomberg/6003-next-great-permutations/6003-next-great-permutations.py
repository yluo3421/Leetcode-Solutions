# 1.

# 123
# nums = [1,2,3]
# output => [1,3,2]  
# permutation = 1,3,2    2,1,3    3,1,2

# nums = [3,2,1] 
# output = [1,2,3]

# nums = [1,2]
# output = [2,1]

# nums = [1,2,3,4,5]
# output = [1,2,3,5,4]

# [7,1,2] output = [7,2,1]

# [9, 1, 6, 4, 3] 
# [9, 3, 6, 4, 1] => [9,3,1,4,6]

#   9, 2, 7, 5, 4, 1
# =>9, 4, 7, 5, 2, 1
# =>9, 4, 1, 2, 5, 7

  
# [7,8,2] => [8,2,7]
class Solution:
    def next_greater_permutation(self, nums):
        pivot = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i
                break
            else:
                continue
        if pivot == 0:
            return nums[::-1]
        for i in range(len(nums) - 1, pivot - 1, -1):
            if nums[i] > nums[pivot - 1]:
                """
                  9, 2, 7, 5, 4, 1
                     ^.       ^
                  pivot - 1.  i
        				=>9, 4, 7, 5, 2, 1
                     ^
                """
                nums[i], nums[pivot - 1] = nums[pivot - 1], nums[i]
        """
          9, 2, 7, 5, 4, 1
        =>9, 4, 7, 5, 2, 1----
        =>9, 4, 1, 2, 5, 7
        nums[:pivot] = [9,4]
        nums[pivot:] = [7,5,2,1]
        nums[pivot:][::-1] = [1,2,5,7]
        """
        return nums[:pivot] + nums[pivot:][::-1]