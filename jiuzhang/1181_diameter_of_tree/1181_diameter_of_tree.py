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
    @param root: a root of binary tree
    @return: return a integer
    """
    def __init__(self):
        self.ans = 0

    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        # write your code here
        # use dfs on root to find the farthest node
        # then use dfs on the farthest node to find next
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if node is None:
            return 0
        
        left_depth = self.dfs(node.left)
        right_depth = self.dfs(node.right)
        self.ans = max(self.ans, left_depth + right_depth)
        return max(left_depth, right_depth) + 1

