# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        thoughts:
        first thing that comes to my mind is level order traversal
        I need to figure out a way to mark vertical level like 
        horizontal level.
        The problem it will be more vertical levels on both sides
        if I have a tree that left only have left children, right
        only have right children. That will be lots of levels

        I want use what I know to see if it can give me some new
        ideas. Let's say I find a way to mark each node during 
        level order traversal.
        Using the example, I will have [[(3,0)],[(9,1),(20,1)],[(15,0),(7,2)]]
        Oh I can call 9 as -1, and that means every left child will be 
        one less vertical order than its parent, while right child
        will be one more than its parent.
        Ok that means I defnitely needs a dict to record this.
        That way I will have dict key as vertical order while values as
        whatever nodes goes on that line.
        I can sort the dict at the end to make the ans.
        However it was a O(n) method but with sort I will have O(nlog(n))
        I dont have the idea to improve this, but is 
        this method you are looking for. I want to code it out and
        see what I can do with time complexity during the process.

        Wait, since every vertical order has to come from its parent
        We can track the max and min we have so far.
        And loop through that, that will save the sort.
        """
        if not root:
            return []
        ans = collections.defaultdict(list)
        queue = collections.deque()
        queue.append((root, 0))
        min_col_idx, max_col_idx = 0, 0
        while queue:
            node, col_idx = queue.popleft()
            
            if node:
                min_col_idx = min(min_col_idx, col_idx)
                max_col_idx = max(max_col_idx, col_idx)
                ans[col_idx].append(node.val)
                queue.append([node.left, col_idx - 1])
                queue.append([node.right, col_idx + 1])
        return [ans[i] for i in range(min_col_idx, max_col_idx + 1)]