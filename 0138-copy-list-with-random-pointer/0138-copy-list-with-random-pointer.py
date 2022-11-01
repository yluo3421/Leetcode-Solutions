"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # thoguhts:
        # create a dict of connection between curr to deep copy of its node
        # then next round, we have mirror images of all nodes
        # no matter what next, random given we can find through the dict
        # Remember to initialize with None:None
        # this is for when pointing to None
        
        deepCopyDict = {None:None}
        
        curr = head
        while curr:
            curr_copy = Node(curr.val)
            deepCopyDict[curr] = curr_copy
            curr = curr.next
        
        curr = head
        while curr:
            curr_copy = deepCopyDict[curr]
            curr_copy.next = deepCopyDict[curr.next]
            curr_copy.random = deepCopyDict[curr.random]
            curr = curr.next
        
        return deepCopyDict[head]