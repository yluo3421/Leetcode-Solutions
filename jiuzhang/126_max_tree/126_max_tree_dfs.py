from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param a: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def max_tree(self, a: List[int]) -> TreeNode:
        # write your code here
        return self.dfs(a, 0, len(a) - 1)
    
    def get_max_position(self, A, left, right):
        value, index = float("-inf"), float("inf")
        for i in range(left, right + 1):
            if value < A[i]:
                value, index = A[i], i
        return index
    
    def dfs(self, A, left, right):
        if left > right:
            return None
        index = self.get_max_position(A, left, right)
        root = TreeNode(A[index])
        root.left = self.dfs(A, left, index - 1)
        root.right = self.dfs(A, index + 1, right)
        return root
    
    