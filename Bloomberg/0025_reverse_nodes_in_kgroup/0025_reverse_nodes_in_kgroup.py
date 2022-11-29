# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # thoughts:
        """
        first check if k < 2
        then go for first round find kth node
        mark it as the next_head
        if next_head become none: meaning the length of linked list is not 
        larger than k, return head
        if next_head exist, save it as ans, because this part will be reversed
        and the next_head at first section become final_answer head

        Start reversing
        current = head
        tail of current section needs to be identified every loop
        tail = current
        prev = None
        while we do the reverse here, the next_head will move to 
        its right location in the next section, because both moves k times

        at the end of one reversing
        tail.next needs to be identified.
        If there is one more section to follow
        tail.next is next_head,
        otherwise next_head will be none, and tail.net is current
        """
        if not head or k < 2:
            return head
        
        next_head = head
        for i in range(k - 1):
            next_head = next_head.next
            if next_head is None:
                return head
        ans = next_head

        current = head
        while next_head:
            tail = current
            prev = None
            for i in range(k):
                if next_head:
                    next_head = next_head.next
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            tail.next = next_head or current
        return ans
