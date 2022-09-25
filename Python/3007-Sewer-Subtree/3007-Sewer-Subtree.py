"""
We build the map using the array, then we build the tree 
using a recursive algorithm that adds the sum of children 
to the root. To find the connection that will give the 
minimum difference between the floods, we simply go 
through all the elements in the map and try to remove its substree.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
class Solution:
    def calculateFlow(self, node):
        return 0 if node == None else node.val + sum([self.calculateFlow(child) for child in node.children])
    def drainagePartition(parent, inputs):
        nodes = [TreeNode(val) for val in inputs]
        for idx, pidx in enumerate(parent):
            if pidx != -1:
                nodes[pidx].children.append(nodes[idx])
        flows = [self.calculateFlow(nodes) for i in range(len(nodes))]
        return min([abs(flows[0] - 2 * f) for f in flows])