# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force
        # first merge 2
        # merge the finished one with the next until all
        
        # 5     7       3       8
        #   5-7
        #       3-5-7
        #           3-5-7-8
        # O(k*n) Time
        
        # 5     7       3       8
        #   5-7             3-8
        #           3-5-7-8
        # O(log(k) * n) Time  because using merge sort method
        # even each merge takes O(n)
        # but only O(log(k)) times of merge
        
        if not lists or len(lists) == 0:
            return None
        
        # merge until only output list
        while len(lists) > 1:
            mergedLists = []
            
            # the step is two because two linked lists are merged each time
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                # check if i + 1 is in range
                # merge None is ok
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeSortedLists(list1, list2))
            lists = mergedLists
        return lists[0]
        
    def mergeSortedLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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