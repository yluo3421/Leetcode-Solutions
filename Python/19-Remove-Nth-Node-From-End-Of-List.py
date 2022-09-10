# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        
        while n > 0:
            n -= 1
            right = right.next
        
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        # possibility that only one value that we need to return a None
        return dummy.next
            