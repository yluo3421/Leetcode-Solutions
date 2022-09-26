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
def calculateFlow(node):
    return 0 if node == None else node.val + sum(calculateFlow(child) for child in node.children)
    
def drainagePartition(parent, inputs):
    nodes = [TreeNode(val) for val in inputs]
    for idx, parentIdx in enumerate(parent):
        if parentIdx != -1:
            nodes[parentIdx].children.append(nodes[idx])
            
    flows = [calculateFlow(nodes[i]) for i in range(len(nodes))]
    return min([abs(flows[0] - 2 * f) for f in flows])