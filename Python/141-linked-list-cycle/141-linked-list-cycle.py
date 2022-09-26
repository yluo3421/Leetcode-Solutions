# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use dict to record all nodes
        # if one nodes next is in the dict, then return True
        
        # nodesMap = {}
        # cur = head
        # while cur:
        #     if cur.next not in nodesMap:
        #         nodesMap[cur] = cur.next
        #     else:
        #         return True
        #     cur = cur.next
        # return False
        
        # slow and fast, the fast going to catch slow eventually
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False