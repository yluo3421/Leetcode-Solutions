"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
"""
We can use a Hashset (named as seen) to keep track of 
all the child nodes that we visit, then at the end the 
root would not be in this set. We could find out the 
root node with two iterations as follows:

As the first iteration, we traverse the elements in 
the input list. For each element, we put its child nodes 
into the hashset seen. Since the value of each node is 
unique, we could either put the node itself or simply 
its value into the hashset.

Then, we visit the list once again. This time, we have 
all the child nodes in the hashset. Once we come across 
any node that is NOT in the hashset, then this is the root 
node that we are looking for.
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # set that contains all the child nodes.
        seen = set()

        # add all the child nodes into the set
        for node in tree:
            for child in node.children:
                # we could either add the value or the node itself.
                seen.add(child.val)

        # find the node that is not in the child node set.
        for node in tree:
            if node.val not in seen:
                return node
            
"""
Space O(1) Optimization
Again, there are several approaches to implement the above idea. Here we present a solution with the operations of addition and deduction. One could replace the addition and deduction operations with the XOR operation, as one will see later.

The idea is that we use an integer (value_sum) to keep track of the sum of node values. More specifically, we add the value of each node to value_sum and we deduct the value of each child node from the value_sum. At the end, the value_sum would be the value of the root node.

The rational is that the values of non-root nodes are cancelled out during the above addition and deduction operations, i.e. the value of a non-root node is added once as a parent node but deducted as a child node.

For this idea to work, an important condition is that the values of all nodes are unique, as specified in the problem.

Still, we could find the root node with two iterations:

In the first iteration, we traverse each node in the list, we add the value of the node to the value_sum. Moreover, we deduct the value of its child nodes from the value_sum.

At the end of the first iteration, the value_sum would become the value of the root node, as we discussed before.

Once we know the value of the root node, i.e. value_sum, we can run a second iteration on the list to find out the root node.

"""
#     def findRoot(self, tree: List['Node']) -> 'Node':
#         value_sum = 0

#         for node in tree:
#             # the value is added as a parent node
#             value_sum += node.val
#             for child in node.children:
#                 # the value is deducted as a child node.
#                 value_sum -= child.val

#         # the value of the root node is `value_sum`
#         for node in tree:
#             if node.val == value_sum:
#                 return node