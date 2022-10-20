# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # same structure of level order traversal
        # but every other level, change from starting with left to starting
        # with right
        
        if not root:
            return []
        
        ans = []
        queue = collections.deque()
        queue.append(root)
        leftOrRight = False
        while queue:
            size = len(queue)
            level = []
            
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if leftOrRight:
                ans.append(level[::-1])
            else:
                ans.append(level)
            leftOrRight = not leftOrRight
        return ans
                        