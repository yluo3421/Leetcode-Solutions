# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # thoughts:
        # use dfs to find all path sum
        # record the node.val during the process
        # if at the end it matches targetSum, append to ans
        ans = []
        if not root:
            return []
        def dfs(root, targetSum, path, path_sum, ans):
            if root is None:
                return None
            path.append(root.val)
            path_sum += root.val
            if root.left is None and root.right is None:
                if path_sum == targetSum:
                    ans.append(path.copy())
                
            else:
                dfs(root.left, targetSum, path, path_sum, ans)
                dfs(root.right, targetSum, path, path_sum, ans)
            path.pop()
        dfs(root, targetSum, [], 0, ans)
        """
        root:   4     8      11     N
        path:   5, 4  5,8    5,4,11 5,4,N
        path_sum9     13     20     

        """
        return ans
            