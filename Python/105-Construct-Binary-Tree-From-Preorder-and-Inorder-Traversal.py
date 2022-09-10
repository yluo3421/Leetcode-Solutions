# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = [3, 9, 20, 15, 7]
        #             ^ 
        #            root
        # inorder = [9, 3, 15, 20, 7]
        #   leftsubtree ^  right subtree
        #           can be removed
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        rootIndexInorder = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:rootIndexInorder + 1], inorder[:rootIndexInorder])
        root.right = self.buildTree(preorder[rootIndexInorder + 1:], inorder[rootIndexInorder + 1:])
        
        return root