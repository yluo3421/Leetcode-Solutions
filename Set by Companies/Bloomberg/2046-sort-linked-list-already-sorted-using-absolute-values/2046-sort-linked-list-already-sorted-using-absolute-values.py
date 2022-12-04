# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Since the given linked list is non-decreasing
        with the absolute values
        The first negative number node should be set as new head
        We can remove it from the linked list and set it as new head
        This is a little too complicated
        Acutally if I can find that next node is larger than the curr
        one, I can directly setHead of the nextNode, otherwise I will
        go for the next
        
        head = [0,2,,5,10,-10]
        curr           ^
        prev         ^
        temp = 5
        
        """
        curr = head
        while curr.next:
            if curr.val > curr.next.val: 
                temp = curr.next
                curr.next = temp.next
                temp.next = head
                head = temp
            else:
                curr = curr.next
        return head
        