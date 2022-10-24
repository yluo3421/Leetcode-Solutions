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
        # deep copy we need to record them by dict
        # if only a normal linked list
        # we could use recursion to do all nodes
        # but now we have random pointer, its like doubly linked list 
        # however we are not sure which it connects to
        
        # the idea is to go through twice
        # first round put curr_node:Node(curr_node.val) into dict,
        # this is a deep copy of the node
        # the second round find each node's next and random
        # the dict has to be initalized to None
        # the it can be referenced
        deepCopyDict = {None:None}
        
        curr = head
        while curr:
            newCopy = Node(curr.val)
            deepCopyDict[curr] = newCopy
            curr = curr.next
        
        curr = head
        while curr:
            copy = deepCopyDict[curr]
            copy.next = deepCopyDict[curr.next]
            copy.random = deepCopyDict[curr.random]
            curr = curr.next
        
        return deepCopyDict[head]