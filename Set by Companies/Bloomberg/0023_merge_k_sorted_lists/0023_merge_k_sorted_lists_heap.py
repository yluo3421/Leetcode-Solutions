# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
First, we form the initial heap with tuples containing val and node itself. 
Notice that in Python implementation of the heap, the first element of the 
tuple is considered as a priority. In case the heap already has an element 
with the same priority, the Python compares the next element of the tuple. 
That is why we need index i in the second place.

Then we run a cycle until the heap is empty. On every step, we pop out 
the smallest node and attach it to the result. Right away we push to
 the heap the next node.

Time: O(k * n * log(k)) - scan and manipulation with heap
Space: O(k) - for the heap
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap, dummy = [], ListNode()
        for i, linked_list in enumerate(lists):
            if linked_list:
                heappush(heap, (linked_list.val, i, linked_list))
        curr = dummy
        while heap:
            _, i, linked_list = heappop(heap)
            if linked_list.next:
                heappush(heap, (linked_list.next.val, i, linked_list.next))
            curr.next = linked_list
            curr = curr.next
        
        return dummy.next