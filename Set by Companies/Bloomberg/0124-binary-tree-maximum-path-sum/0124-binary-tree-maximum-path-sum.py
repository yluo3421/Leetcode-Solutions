# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -float("inf")
        
        def findSubtreeMax(node):
            nonlocal max_path
            
            if not node:
                return 0
            
            left_subtree_max = max(findSubtreeMax(node.left), 0)
            right_subtree_max = max(findSubtreeMax(node.right), 0)
            max_path = max(max_path, left_subtree_max + right_subtree_max + node.val)
            return max(left_subtree_max + node.val, right_subtree_max + node.val)
        
        findSubtreeMax(root)
        return max_path