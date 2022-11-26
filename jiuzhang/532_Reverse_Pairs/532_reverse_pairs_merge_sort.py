from typing import (
    List,
)

class Solution:
    """
    @param a: an array
    @return: total of reverse pairs
    """
    def reverse_pairs(self, a: List[int]) -> int:
        # write your code here
        
        return self.mergeSort(a, 0, len(a) - 1, list(a))

    def mergeSort(self, A, start, end, temp):
        if start > end:
            return 0
        if start == end:
            return 0
        
        mid = (start + end) // 2
        leftPairs = self.mergeSort(A, start, mid, temp)
        rightPairs = self.mergeSort(A, mid + 1, end, temp)
        
        i, j = mid, end
        index = end
        reversePairs = 0
        while i >= start and j >= mid + 1:
            if A[i] > A[j]:
                temp[index] = A[i]
                index, i = index - 1, i - 1
                reversePairs += j - mid
            else:
                temp[index] = A[j]
                index, j = index - 1, j - 1
        while i >= start:
            temp[index] = A[i]
            index, i = index - 1, i - 1
        while j >= mid + 1:
            temp[index] = A[j]
            index, j = index - 1, j - 1

        for i in range(start, end + 1):
            A[i] = temp[i]
        
        return reversePairs + leftPairs + rightPairs