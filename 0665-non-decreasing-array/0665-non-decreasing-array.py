class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
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
        """
        Second method
        Consider the interval [i, j] corresponding to the subarray [A[i], A[i+1], ..., A[j]]. When A[i]≤A[i+1]≤A[i+2], we know we do not need to modify A[i], and we can consider solving the problem on the interval [i+1, j] instead. We use a similar approach for jj.

Afterwards, with the length of the interval under consideration being j - i + 1, if the interval has size 2 or less, then we did not find any problem.

If our interval under consideration has 5 or more elements, then there are two disjoint problems that cannot be fixed with one replacement.

Otherwise, our problem size is now at most 4 elements, which we can easily brute force.


        """

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
        