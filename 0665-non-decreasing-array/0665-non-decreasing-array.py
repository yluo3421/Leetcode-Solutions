class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        Second method
        O(n)
        As before, let pp be the unique problem index for which A[p]>A[p+1]. If this is not unique or doesn't exist, the answer is False or True respectively. We analyze the following cases:

If p = 0, then we could make the array good by setting A[p] = A[p+1].
If p = len(A) - 2, then we could make the array good by setting A[p+1] = A[p].
Otherwise, A[p-1], A[p], A[p+1], A[p+2] all exist, and:
We could change A[p] to be between A[p-1] and A[p+1] if possible, or;
We could change A[p+1] to be between A[p] and A[p+2] if possible


        """

        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i

        return (p is None or p == 0 or p == len(nums)-2 or
                nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2])
        
        """
        The criteria is to modify one number
        O(n^2)
        
        For the given array A, if we are changing at most one element A[i], we should change A[i] toA[i-1], as it would be guaranteed that A[i-1]≤A[i], and A[i] would be the smallest possible to try and achieve A[i]≤A[i+1].

Algorithm

For each possible change A[i], check if the sequence is monotone increasing. We'll modify new, a copy of the array A.
        """
        
        #Same as in approach 1
        def monotone_increasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        new = nums[:]
        for i in range(len(nums)):
            old_numsi = nums[i]
            new[i] = new[i-1] if i > 0 else float('-inf')
            if monotone_increasing(new):
                return True
            new[i] = old_numsi

        return False
        