"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # to make deep copy
        # we need to make copy of val and neighbors
        # but neighbors are possible to be not yet constructred
        # use dict to record nodes' val and neighbors
        # grab one node, if it has a neighbor, make the key,value to be                       Node,CopyNode
        # once all nodes are done, go through dict again to assign all nodes
        
        # use dfs while trying to append neighbors
        oldToCopy = {}
        
        def dfs(node):
            if node in oldToCopy:
                return oldToCopy[node]
            
            copy = Node(node.val)
            oldToCopy[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node) if node else None
            
        
            
        
        