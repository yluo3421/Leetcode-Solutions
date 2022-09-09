# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # i have to both directions
        # check until no more child nodes
        # record each level and max level so far
        
        #       3(3)
        #   9(1)      20(2)
        #       15(1)     7(1)
        #   left0. right0
        if not root:
            return 0
    
        
        currMax = max(self.maxDepth(root.left), self.maxDepth(root.right)) #0
        return currMax + 1
        