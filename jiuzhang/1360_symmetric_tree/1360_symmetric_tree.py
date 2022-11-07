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
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def is_symmetric(self, root: TreeNode) -> bool:
        # Write your code here
    # thoughts:
    # BFS for level order, if each level is palindrome
    # then its symmetric tree.
    # this is a wrong method. None node
    # should be reflected as # in level order traversal
        
        """
        The actual problem is to check if the two child
        tree are symmetrical.
        Use a similar thoughts as preorder
        First check if two subtree's root has the same value
        Then check if their children follow the same pattern
        """
        if not root:
            return True
        return self._is_symetric(root.left, root.right)
    
    def _is_symmetric(self, left_root, right_root):
        if left_root is None and right_root is None:
            return True
        if left_root is None or right_root is None:
            return False

        if left_root.val != right_root.val:
            return False
        return self._is_symmetric(left_root.left, right_root.right) and \
            self._is_symmetric(left_root.right, right_root.left)