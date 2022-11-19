# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # a single node is symmetric
        # a three nodes tree is symmetric if left and right has the same value
        # use a dfs to check
        # first check both left and right
        # then return that left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        
        
        def dfs(root_left, root_right):
            if root_left == None and root_right == None:
                return True
            if root_left is None or root_right is None:
                return False
            return root_left.val == root_right.val and dfs(root_left.left, root_right.right) and dfs(root_left.right, root_right.left)
        
        return dfs(root.left, root.right)
