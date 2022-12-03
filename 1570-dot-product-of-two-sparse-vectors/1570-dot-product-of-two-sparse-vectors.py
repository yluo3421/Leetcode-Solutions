class SparseVector:
    def __init__(self, nums: List[int]):
        """
        Thoughts:
        Store the nums as it is
        Then calculate the sum of product
        """
        self.vector = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i, j in zip(self.vector, vec.vector):
            ans += i * j
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)