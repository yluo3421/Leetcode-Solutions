class Node:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    def deepCopyLinkedList(self, head:'Optional[Node]')-> 'Optional[Node]':
        dummy = Node()
        curr = head
        newHead = dummy
        while curr:
            newHead.next = Node(curr.val)
            newHead = newHead.next
            curr = curr.next
        return dummy.next

        # dry run
        # 3 -> 4 -> 8 -> 1
        """
        curr                    3   4   4       8 
        newHead         dummy       3       4   8 
        newHead.next    None    3   N   4   N

        """