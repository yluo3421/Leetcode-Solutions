"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""


"""
Serialization

1. We'll do a simple depth first traversal of the tree starting f
rom the root node and the StringBuilder (list in case of Python).
2. The helper function would take one WrappableInt as an input in 
addition to the node itself. The custom integer would represent 
the unique Id of the current node. As for the parent node, we pass 
a simple Integer object since we don't want retention for parentIds across recursion.

3. For every node, we will add 3 values to the 
serialized string. The first would be the unique Id 
of the current node. Next we add the actual value of 
the node and finally, we add the unique Id of the parent node.

4. Remember to use the unicode character trick discussed 
in the introduction section of this article. We will be 
using it heavily to keep down the overall length of the serialized string.

5. For the root node, we will be using a special 
dummy value N. We can use a negative value as well 
since the test cases don't have any negative value. 
However, for achieving as much generalization as possible, 
let's use a dummy character.


Deserialization

1. For deserialization, we are given the string as an 
input. We will always be processing the input in triplets 
since 3 characters represent the information for one node.

2. We will initialize a HashMap that will contain 
the data from the string. It's the hash map from 
the figures before.

3. For every triplet in the input string (a, b, c), 
we will create a new entry in the hash map with a 
being the key and a pair of b, c being the value. 
Remember, a represents the unique Id for the node, 
b represents its actual value and c represents the 
Id of the parent node. Also, in addition to the 2 
values b, c, we will also be adding new TreeNode 
or Node data structures to the dictionary. This is 
because we will be re-using this dictionary to fill 
up the children lists for each node. So the actual 
entry in the hash map would be

a -> (b, c, Node(a, []))

4. Once we are done constructing the dictionary, 
we have to construct the original tree. We have 
already constructed all the nodes of the tree. 
All that remains is establishing the right connections 
in the right order. Remember when we mentioned about 
the ordering of the children nodes, we have to ensure 
we don't mess that up here.

5. We can't process nodes in any random order. So, 
we use the original string itself and use every third 
entry as the node to process.



"""
class WrappableInt:
        def __init__(self, x):
            self.value = x
        def getValue(self):
            return self.value
        def increment(self):
            self.value += 1

class Codec:
    
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serializedList = []
        self._serializeHelper(root, serializedList, WrappableInt(1), None)
        return "".join(serializedList)
    
    def _serializeHelper(self, root, serializedList, identity, parentId):
        if not root:
            return
        
        # Own identity
        serializedList.append(chr(identity.getValue() + 48))
        
        # Actual value
        serializedList.append(chr(root.val + 48))
        
        # Parent's identity
        serializedList.append(chr(parentId + 48) if parentId else 'N')
        
        parentId = identity.getValue()
        for child in root.children:
            identity.increment()
            self._serializeHelper(child, serializedList, identity, parentId)
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        
        if not data:
            return None
        
        return self._deserializeHelper(data)
        
    def _deserializeHelper(self, data):
        
        nodesAndParents = {}
        for i in range(0, len(data), 3):
            identity = ord(data[i]) - 48
            orgValue = ord(data[i + 1]) - 48
            parentId = ord(data[i + 2]) - 48
            nodesAndParents[identity] = (parentId, Node(orgValue, []))
            
        for i in range(3, len(data), 3):
            
            # Current node
            identity = ord(data[i]) - 48
            node = nodesAndParents[identity][1]
            
            # Parent node
            parentId = ord(data[i + 2]) - 48;
            parentNode = nodesAndParents[parentId][1];
            
            # Attach!
            parentNode.children.append(node);
            
        return nodesAndParents[ord(data[0]) - 48][1]    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))