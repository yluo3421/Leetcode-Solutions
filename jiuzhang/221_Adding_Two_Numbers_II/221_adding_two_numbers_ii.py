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
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def add_lists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here
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
        s1, s2 = 0, 0
        while l1:
            s1 = s1 * 10 + l1.val
            l1 = l1.next
        while l2:
            s2 = s2 * 10 + l2.val
            l2 = l2.next
        result = s1 + s2
        result = str(result)
        print(result)
        dummy = ListNode(0)
        curr = dummy
        for char in result:
            curr.next = ListNode(int(char))
            curr = curr.next
        return dummy.next
    
    # method 2
    # reverse both linkedlist, add them together
    # reverse the resulting linked list
    # check if it has a 0 at the end
    def addLists2(self, l1, l2):
        # write your code here
        l1 = self.reverse(l1);
        l2 = self.reverse(l2);
        sum = ListNode(0)
        cur = sum
        pre = sum
        while l1!=None and l2!=None:
            cur.val += l1.val+l2.val
            cur.next = ListNode(cur.val/10)
            cur.val = cur.val%10
            l1 = l1.next
            l2 = l2.next
            pre = cur
            cur = cur.next
        while l1!=None:
            cur.val += l1.val
            cur.next = ListNode(cur.val/10)
            cur.val = cur.val%10
            l1 = l1.next
            pre = cur
            cur = cur.next
        while l2!=None:
            cur.val += l2.val
            cur.next = ListNode(cur.val/10)
            cur.val = cur.val%10
            l2 = l2.next
            pre = cur
            cur = cur.next
        if cur.val==0:
            pre.next = None
        return self.reverse(sum)

    def reverse(self, head):
        # write your code here
        curr = None
        next = head
        while next:
            prev = curr
            curr = next
            next = next.next
            curr.next = prev
        return curr
