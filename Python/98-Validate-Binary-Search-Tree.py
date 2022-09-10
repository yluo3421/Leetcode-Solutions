# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        leftBoundary, rightBoundary = float("-inf"), float("inf")
        def validNode(root, leftBoundary, rightBoundary):
            if not root:
                return True
            # a root is valid if it is larger than left boundary
            # and less than right boundary
            # if it doesnt fit, return False
            
            if not (root.val > leftBoundary and root.val < rightBoundary):
                return False
            
            return validNode(root.left, leftBoundary, root.val) and validNode(root.right, root.val, rightBoundary)
        
        return validNode(root, leftBoundary, rightBoundary)
            
        