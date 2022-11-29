# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # first convert linked list to nums array
        # then set the mid point to root
        # set root.left as mid point of [:mid]
        # set root.right as mid point of [mid + 1:]
        if head is None:
            return None

        nums = []
        start = head
        while start:
            nums.append(start.val)
            start = start.next
        
        def arrayToBST(nums):
            if len(nums) == 0:
                return None
            else:
                mid = len(nums) // 2
                root = TreeNode(nums[mid])
                root.left = arrayToBST(nums[:mid])
                root.right = arrayToBST(nums[mid + 1:])
                return root
        return arrayToBST(nums)