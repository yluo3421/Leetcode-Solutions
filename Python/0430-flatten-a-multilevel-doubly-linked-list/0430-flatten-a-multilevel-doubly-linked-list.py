"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # similar to binary tree
        # whenever there is a child tree, go for child
        # the next will be implemented later
        if not head:
            return head
        dummy = Node(0)
        root = head
        stack = [root]
        curr = dummy
        while stack:
            last = stack.pop()
            if last.next:
                stack.append(last.next)
            if last.child:
                stack.append(last.child)
            curr.next = last
            last.prev = curr
            last.child = None
            curr = last
        ans = dummy.next
        ans.prev = None
        return ans
            
            