# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        ans = []
        queue = collections.deque()
        if root:
            queue.append(root)
        #       3
        #   9       20
        #       15      7
        # queue         len(queue)     popleft      levelVal    ans
        #   3           1                           []          []
        #                               3           [3]         []
        #   9,20                                                [[3]]
        #   9,20        2                           []          [[3]]
        #    20                         9           [9]         [[3]]
        #                               20          [9,20]      [[3]]
        #   15,7                                                [[3],[9,20]]
        #   15,7        2                           []
        while queue:
            levelVal = []
            for i in range(len(queue)):
                node = queue.popleft()
                levelVal.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            ans.append(levelVal)
        return ans
        


        """
        Better method
        """
    def level_order(self, root: UndirectedGraphNode) -> List[List[int]]:
    # write your code here
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            currLevel = []
            n = len(queue)
            for _ in range(n):
                currNode = queue.popleft()
                currLevel.append(currNode.label)
                for neighbor in currNode.neighbors:
                    queue.append(neighbor)
            res.append(currLevel)
        return res