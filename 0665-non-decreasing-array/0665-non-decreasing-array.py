class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        The criteria is to modify one number
        
        """
        def brute_force(A):
            #Same as in approach 1
            def monotone_increasing(arr):
                for i in range(len(arr) - 1):
                    if arr[i] > arr[i+1]:
                        return False
                return True

            new = A[:]
            for i in range(len(A)):
                old_ai = A[i]
                new[i] = new[i-1] if i > 0 else float('-inf')
                if monotone_increasing(new):
                    return True
                new[i] = old_ai

            return False

        i, j = 0, len(nums) - 1
        while i+2 < len(nums) and nums[i] <= nums[i+1] <= nums[i+2]:
            i += 1
        while j-2 >= 0 and nums[j-2] <= nums[j-1] <= nums[j]:
            j -= 1

        if j - i + 1 <= 2:
            return True
        if j - i + 1 >= 5:
            return False

        return brute_force(nums[i: j+1])
        