# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # A function to do inorder tree traversal
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # how to check all nodes 
        # use tarversal and record curr max
        currMax = []
        def dfs(root, currMax):
            if not root:
                return 0
            if root:
                newMaxPathSum = self.calculateMaxPathSum(root)
                # print(newMaxPathSum)
                
                currMax.append(newMaxPathSum)
                
                self.calculateMaxPathSum(root.left)
                self.calculateMaxPathSum(root.right)

            return currMax
        newCurrMax = dfs(root, currMax)
        print(newCurrMax)
        return 
    
        
            
    def calculateMaxPathSum(self, root: Optional[TreeNode]) -> int:
        # thoughts
        # check each nodes left subtree sum and right subtree sum
        # what if the node is negative
        # path sum = left subtree sum + right subtree sum + node.val
        # check each node's max possible path sum
        # if both left and right None, max path sum = node.val
        # if left, max path sum = max(node.val, node.val + left.val)
        # if right, max path sum = max(node.val, node.val + right.val)
        # if left and right, max path sum = 
        #            max(node.val, node.val + left.val, node.val + right.val, 
        #               + node.val + left.val + right.val
        # )
        # node max path sum = max (
        #       maxSub1treeSum(node)
        #       node.val + left(node max 1 tree sum) + right(node max 1 tree sum)
        #)
        # node max sub 1 tree sum = max (
        #       node.val
        #       node.val + left(node max 1 tree sum)
        #       node.val + right(node max 1 tree sum)
        #)
        
        return max(
            self.maxSubtreeSum(root),
            root.val + self.maxSubtreeSum(root.left) + self.maxSubtreeSum(root.right)
        )
    
    def maxSubtreeSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(
            root.val,
            root.val + self.maxSubtreeSum(root.left),
            root.val + self.maxSubtreeSum(root.right)
        )