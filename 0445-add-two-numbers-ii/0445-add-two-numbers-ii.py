# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode])-> Optional[ListNode]:
        # 7->2->4->3
        last = None
        while head:
            temp = head.next
            head.next = last
            last = head
            head = temp
        return last
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # brutal force
        # change both linked list into int
        # add them together and make it linked list
        
        # two stacks method
        # use two stack to take both linked list's each node's val
        # pop from two stacks and record their carry and digit
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        head = None
        carry = 0
        while l1 or l2:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            
            digit = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            
            curr = ListNode(digit)
            curr.next = head
            head = curr
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr
        
        return head
            
        