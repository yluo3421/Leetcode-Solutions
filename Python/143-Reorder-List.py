# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # remove node at n-1, insert at 1 
        # node 0 has node n
        # node 1 has node n-1
        
        # thoughts:
        # loop through nodes, find their tail node at the end of the linked list
        # change their next
        
        # find middle point of the linked list
        # reverse the second half of the linked list
        # combine the two linked list one after another.
        # Great problem that combines three linked list problems
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalfHead = slow.next
        prev = slow.next = None
        while secondHalfHead:
            temp = secondHalfHead.next
            secondHalfHead.next = prev
            prev = secondHalfHead
            secondHalfHead = temp
        
        
        # prev      curr    curr.next       temp
        #                                   temp = curr.next
        #                   curr.next = prev
        # prev = curr
        #          curr = temp
        
        firstHalfHead = head
        secondHalfHead = prev
        while secondHalfHead:
            # temp1 = firstHalfHead.next
            # firstHalfHead.next = secondHalfHead
            # firstHaflHead = temp1
            # temp2 = secondHalfHead.next
            # secondHalfHead.next = firstHalfHead
            # secondHalfHead = temp2
            temp1, temp2 = firstHalfHead.next, secondHalfHead.next
            firstHalfHead.next = secondHalfHead
            secondHalfHead.next = temp1
            firstHalfHead, secondHalfHead = temp1, temp2
        
        # first, second = head, prev
        # while second:
        #     tmp1, tmp2 = first.next, second.next
        #     first.next = second
        #     second.next = tmp1
        #     first, second = tmp1, tmp2
        
        
            
        
                
        