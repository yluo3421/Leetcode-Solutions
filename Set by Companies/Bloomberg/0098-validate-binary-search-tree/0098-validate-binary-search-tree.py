# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        use a dfs to check each node if they are in the boundary
        The left and right boundary are initialized with -inf and inf
        if node.val is within the range, meaning we can use
        node.val as right boundary for node.left
        node.val as left boundary for node.right
        if node.val is out of the range, meaning the tree not valid
        if node is none, meaning we meet the final node return True
        """
        def dfs(node, left_boundary, right_boundary):
            if node is None:
                return True
            elif node.val > left_boundary and node.val < right_boundary:
                return dfs(node.left, left_boundary, node.val) and dfs(node.right, node.val, right_boundary)
            else:
                return False
            
        return dfs(root, float("-inf"), float("inf"))
        