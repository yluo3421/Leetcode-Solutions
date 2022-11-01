"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # use level order traversal
        # for each node in the level, assign their next as the i + 1 node
        # because we assign node into queue from left to right
        # when get the curr node from popleft, the next node is queue[0]
        # only the last node in curr level will have next as none
        if not root:
            return None
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root