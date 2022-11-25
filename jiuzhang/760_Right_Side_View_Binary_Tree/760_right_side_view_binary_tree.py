from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """
    def right_side_view(self, root: TreeNode) -> List[int]:
        # write your code here
        if not root:
            return []
        queue = collections.deque([root])
        ans = []
        
        while queue:
            level = []
            size = len(queue)
            while size > 0:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            ans.append(level[-1])
        return ans

