# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        thoughts:
        use dummy head as a start
        if l1.val <= l2.val
        newList.next = l1
        else
        newList.enxt = l2
        check l1, l2 if there is any remaining parts
        """
        l1 = list1
        l2 = list2
        dummy = ListNode()
        newHead = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                newHead.next = l1
                l1 = l1.next
            else:
                newHead.next = l2
                l2 = l2.next
            newHead = newHead.next
        if l1:
            newHead.next = l1
        if l2:
            newHead.next = l2
        return dummy.next