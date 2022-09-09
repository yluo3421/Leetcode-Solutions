# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # brute force
        # calculate the height of left and right
        # abs(leftHeight - rightHeight) <= 1
        # return True
        
        # calculate left tree and right tree height
        # if both left and right subtree are balanced, at the same time
        # the subtree's height difference is no larger than 1
        # meaning the current node is balanced
        # return the node's balanced and updated height
        
        # [True, height: int]
        def DFS(root: Optional[TreeNode]) -> int:
            if not root:
                return [True, 0]
            leftHeight, rightHeight = DFS(root.left), DFS(root.right)
            balanced = leftHeight[0] and rightHeight[0] and abs(leftHeight[1] - rightHeight[1]) <= 1
            
            return [balanced, 1 + max(leftHeight[1], rightHeight[1])]
            
        [ans, height] = DFS(root)
        return ans
        