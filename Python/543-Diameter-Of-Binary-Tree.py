# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # sounds like max depth at left + max depth at right
        #           1
        #       2       3
        #   4       5
        #6         7
        #      8
        
        # brutal force
        # check all nodes, their max depth to left and right, find the max sum
        # every round return the height of left and right subtree.
        # update the diameter rather than returning it.


        '''
        METHOD NOT WORKING
        '''
        diameter = 0
        def DFS(root: Optional[TreeNode], diameter: int) -> int:
            if not root:
                return 0
            
            leftSubTreeHeight = DFS(root.left, diameter)
            rightSubTreeHeight = DFS(root.right, diameter)
            diameter = max(diameter, leftSubTreeHeight + rightSubTreeHeight)
            return 1 + max(leftSubTreeHeight, rightSubTreeHeight)
        DFS(root, diameter)
        return diameter