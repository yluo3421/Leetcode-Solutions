# Time: log(min(n, m))


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # thoughts
        # find mid point of A & B
        # check if they can make the new array's left and right part
        # cause median will fall on the end of two parts
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        if len(A) > len(B):
            A, B = B, A
        left, right = 0 , len(A) - 1
        while True:
            i = (left + right) // 2
            j = half - i - 2
            
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aright > Bright:
                right = i - 1
            else:
                left = i + 1
            
            