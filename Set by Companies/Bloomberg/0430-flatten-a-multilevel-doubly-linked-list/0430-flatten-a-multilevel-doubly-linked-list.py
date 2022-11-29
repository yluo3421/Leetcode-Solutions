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
        # basically whenever we see a child,
        # we can save next as temp, insert child to curr.next
        # then assign temp to end of child
        # to ensure all children going back to where they supposed to be
        # I want to use a stack to store them
        # the idea is like this
        # putting the root into stack
        # wait we need a dummy node to hold the new one
        # lets call dummy node curr
        # then the stack.pop() is last
        # we first put last.next into stack, then last.child, because we want
        # to prioritize children's case
        # after then we will assign curr.next as last, last.prev = curr
        # most importantly, last.child = None
        # finally update curr to = last
        if not head:
            return head
        root = head
        stack = [root]
        dummy = Node(0)
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
        res = dummy.next
        res.prev = None
        return res

        