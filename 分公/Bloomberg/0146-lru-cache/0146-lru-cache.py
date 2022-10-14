from collections import deque
class LRUCache:
    # thoughts:
    # this can be achieved by using dict
    # size can be limited by len(dict)
    # but cannot get who is least used
    # use queue to record recently used 
    # queue cannot be used because we cannot find the duplicate
    # and update the most recent used without removing other items

    # with this in mind, linked list is the last option
    # however i need reference point to remove duplicate's in 
    # linked list.
    # here doubly linked list comes in help
    # It makes removing the least used item, tail of doubly linked
    # list O(1)
    # It makes adding the new item, to head of doubly linked list
    # O(1)
    # Most importantly, for item update, we can remove item with O(1)
    # cause it is remove the node, bind the prev and next together
    # And move this node to head of doubly linked list
    # but still it takes O(n) to find the key   
    
    # i first thought cache = {key:value} 
    # but better way is {key:Node}
    
    # self.doubly_linked_list = DoublyLinkedList()
    # not a good name, it does not tell what this does
    
    # find current head and add a prev to it
    # add next to the current node to current head
    def __init__(self, capacity: int):
        self.capacity = capacity if capacity > 0 else 1        
        self.cache = {}
        self.currSize = 0                
        self.least_recent_list = DoublyLinkedList()
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.updateLeastRecent(self.cache[key])
            return self.cache[key].value
            
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.currSize == self.capacity:
                self.removeLeastUsed()
            else:
                self.currSize += 1
            self.cache[key] = Node(key, value) 
        else:
            self.cache[key].value = value
        self.updateLeastRecent(self.cache[key])
    
    def removeLeastUsed(self):
        print(self.least_recent_list)
        keyToRemove = self.least_recent_list.tail.key
        self.least_recent_list.removeTail()
        del self.cache[keyToRemove]
        
    def updateLeastRecent(self, node):
        self.least_recent_list.setHead(node)
        
            
            
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
    def removeBinds(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def setHead(self, node):
        
        if self.head == node:
            return
        elif self.head == None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBinds()
            self.head.prev = node
            node.next = self.head
            self.head = node
            
            
        
    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None
        
   
        
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)