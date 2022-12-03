class SparseVector:
    def __init__(self, nums: List[int]):
        """
        Thoughts:
        Store the nums as it is
        Then calculate the sum of product
        To better perform, because 0 times any number is 0
        we can save some calculation
        We can also store the sparse vecotr as a list of
        (idx, value) pairs.
        Then we can use two pointers to calculate the dot 
        product.
        """
        # brutal method
        # self.vector = nums
        self.pairs = []
        for idx, value in enumerate(nums):
            if value != 0:
                self.pairs.append([idx, value])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # brutal method
        # ans = 0
        # for i, j in zip(self.vector, vec.vector):
        #     if i == 0 or j == 0:
        #         continue
        #     ans += i * j
        # return ans
        ans = 0
        left, right = 0, 0
        n, m = len(self.pairs), len(vec.pairs)
        
        while left < n and right < m:
            if self.pairs[left][0] == vec.pairs[right][0]:
                ans += self.pairs[left][1] * vec.pairs[right][1]
                left += 1
                right += 1
            elif self.pairs[left][0] < vec.pairs[right][0]:
                left += 1
            else:
                right += 1
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)