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
    @param root: a TreeNode
    @return: return a boolean
    """
    def check_equal_tree(self, root: TreeNode) -> bool:
        # write your code here
        sum_set = set()
        # this avoid putting sum of total tree into set
        sum = root.val + self.dfs(root.left, sum_set) + \
            self.dfs(root.right, sum_set)
        return sum % 2 == 0 and (sum / 2) in sum_set
    
    def dfs(self, root, sum_set):
        if root is None:
            return 0
        sum = root.val + self.dfs(root.left, sum_set) + \
            self.dfs(root.right, sum_set)
        sum_set.add(sum)
        return sum
    """
    WRONG METHOD
    Method below we found all sum of subtree
    add those sum to the set
    return when half of sum is in set
    Also check if total sum is even or not
       1
      / \
    2    -3
    set = 0, 2, -3
    total_sum = 0, so we are trying to find subtree of sum of 0
    One of the subtree which is the root itself has sum of 0
    
    The problem is that if the total sum is 0
    But none of the node /subtree sum is 0

    def check_equal_tree(self, root: TreeNode) -> bool:
        # write your code here
        sum_set = set()
        sum = self.dfs(root, sum_set)
        return sum % 2 == 0 and (sum / 2) in sum_set
    
    def dfs(self, root, sum_set):
        if root is None:
            return 0
        sum = root.val + self.dfs(root.left, sum_set) + \
            self.dfs(root.right, sum_set)
        sum_set.add(sum)
        return sum
    """