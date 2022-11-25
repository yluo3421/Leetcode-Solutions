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
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    # method 1
    def is_valid_b_s_t(self, root: TreeNode) -> bool:
        def helper(root, left_boundary, right_boundary):
            if root is None:
                return True
            if root.val > left_boundary and root.val < right_boundary:
                return helper(root.left, left_boundary, root.val) and helper(root.right, root.val, right_boundary)
            else:
                return False
        return helper(root, float("-inf"), float("inf"))
    
    # method 2 with global variable
    def is_valid_b_s_t(self, root: TreeNode) -> bool:
        # write your code here
        self.lastVal = None
        self.isBST = True
        self.validate(root)
        return self.isBST

    def validate(self, root):
        if root is None:
            return
        self.validate(root.left)
        if self.lastVal is not None and self.lastVal >= root.val:
            self.isBST = False
            return
        self.lastVal = root.val
        self.validate(root.right)