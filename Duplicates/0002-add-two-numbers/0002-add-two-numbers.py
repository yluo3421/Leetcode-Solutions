# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # work as the original way we add up two numbers
        # using digit + digit and carry
        # if not list, use 0 for curr digit
        # the new digit is d1 + d2 + carry % 10
        # the carry is d1 + d2 + carry // 10
        # create the new node with digit 
        # also go to the next of l1 & l2 if not use as None
        # at the end, check carry, if carry, create a node with carry
        dummy = ListNode()
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
        
        return dummy.next