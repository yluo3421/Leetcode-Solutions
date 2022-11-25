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
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        # use dfs with vertical sides, root is 0
        # left is -1, right is 1
        # record them into a dict with each vertical coordinates
        results = collections.defaultdict(list)
        queue = collections.deque()
        
        queue.append((root, 0))
        # 宽度优先遍历，同时记录列编号
        while queue:
            node, col_idx = queue.popleft()
            if node:
                results[col_idx].append(node.val)
                queue.append((node.left, col_idx - 1))
                queue.append((node.right, col_idx + 1))
        
        return [results[i] for i in sorted(results)]
