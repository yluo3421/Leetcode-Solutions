# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # pointer initialized with a non-existent number smaller than any element
        # meaning the first next element is the smallest in the BST
        # then we are going to pop in increasing order
        # in order traversal is a great example here
        # use a stack to store all of the left child until the smallest
        # after poping one, push all its right child into it
        self.stack = []
        self.pushAll(root)
    
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        temp = self.stack.pop()
        self.pushAll(temp.right)
        return temp.val

    def hasNext(self) -> bool:
        return self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()