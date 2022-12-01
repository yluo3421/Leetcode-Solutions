# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        The first method that comes to me is simple
        I will transfer the l1 and l2 to integer and
        then add the two integer together.
        Afterwards the result will be transformed into string
        Finally the string will be retruned into a newly created
        linked list
        Time O(n+m) | Space O(n+m)
        Is this the method you are looking for?
        I have see questions regrading adding two linked list
        but the number comes in opposite order
        That way we can use digit addition and carry to do the thing
        This reminds me that I can reverse both linked lists
        and use digit and carry method.

        """
        num1, num2 = 0, 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        result = num1 + num2
        result = str(result)

        dummy = ListNode(0)
        curr = dummy
        for char in result:
            curr.next = ListNode(int(char))
            curr = curr.next
        return dummy.next

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
            
        