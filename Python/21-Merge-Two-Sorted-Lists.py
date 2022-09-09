# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # thoughts:
        # loop through both linked list and compare each node's val
        # larger one goes after smaller one
        
        # hint use a dummy node
        # set dummy as new node
        # make a clone of head of the new mergerd linked list
        dummy = ListNode()
        newHead = dummy
        

        # 1 2 4
        # 1 3 4
        # dummy
        # list1     list1.next  list2   list2.next  newHead   newHead.next
        # 1         2           1          3        None
        #                       3                    None      1
        #                                           1
        # 1         2           3       4           1       None
        #                                           1       1
        #  2        4           
        # 2         4           3       4           1       1
        while list1 and list2:
            if list1.val >= list2.val:
                newHead.next = list2
                list2 = list2.next
            else:
                newHead.next = list1
                list1 = list1.next
            newHead = newHead.next
            
        # the while loop will be exited if one linked list runs out
        # check both linked list and attach the remaining one to the newHead.next
        if list1:
            newHead.next = list1
        if list2:
            newHead.next = list2
        
        #       None 1 1  2 3 4 4 
        # Newhead               ^
        # Dummy  ^
        # Dummy.next ^
        return dummy.next
        
        
        # 
        
        
        # no extra space
        # my method O(n + m) Time | O(1) Space
        # two array method  O(n+m) Time | O(n+m) Space