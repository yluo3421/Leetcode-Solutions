# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # kth smallest with 1 index means 
        # 4th smallest is [3,1,4,null,2] return 4
        # 1st smallest is [3,1,4,null,2] return 1
        
        # use two pointer
        # the fast pointer is k-1 faster than slow pointer
        # cannot go back to right tree
        
        # slow, fast = root, root
        # n = k
        # while n > 0 and fast:
        #     n -= 1
        #     fast = fast.left
        # while fast
        
        # use stack
        # push left node into stack
        # pop each node and check if they have right
        # if curr has right append to stack and check its left and right
        n = 0
        stack = []
        curr = root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        
        # stack     curr        curr.left   curr.right
        # []        3           1           4
        # [3]       1           None        2
        # 
        
        