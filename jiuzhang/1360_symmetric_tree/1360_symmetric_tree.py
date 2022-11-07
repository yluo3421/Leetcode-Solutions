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
    # wrong thoughts:
    # BFS for level order, if each level is palindrome
    # then its symmetric tree.
    # this is a wrong method. None node
    # should be reflected as # in level order traversal
    
    # left,root, right and right root left to generate
    # the order of the tree, if they are palindrome.
    # This will not prove symmetric
        """
        O(n) Time | O(h) Space
        Recursion times * Recursion each time = (n/2) * O(1)
        Recursion depth * each recursion space

        The actual problem is to check if the two child
        tree are symmetrical.
        Use a similar thoughts as preorder
        First check if two subtree's root has the same value
        Then check if their children follow the same pattern

        Preorder, Inorder, Postorder can all be used here
        But preorder is the best because we check root val
        If root value are different we dont need to check 
        sub tree any more.
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