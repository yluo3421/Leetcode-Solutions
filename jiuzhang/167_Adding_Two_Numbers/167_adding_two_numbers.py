from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def add_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here
        dummy = ListNode(0)
        newHead = dummy
        carry = 0
        while l1 or l2:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0

            digit = (d1 + d2 + carry) % 10
            carry = (d1 + d2 + carry) // 10

            newHead.next = ListNode(digit)
            newHead = newHead.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            newHead.next = ListNode(carry)
            newHead = newHead.next
        return dummy.next
