class LRUCache:

    def __init__(self, capacity: int):
        # we need something to store the information
        # dict because we have a key dict {key: value}
        self.capacity = capacity
        self.cache = {}   #{key: Node((key,value))}
        self.curr_size = 0
        self.doubly_linked_list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            # cache[key] is returning the node
            self.updateRecentUsed(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.curr_size == self.capacity:
                self.removeLeastUsed()
            else:
                self.curr_size += 1
            self.cache[key] = Node(key, value)
        else:
            self.cache[key].value = value
        self.updateRecentUsed(self.cache[key])
        
    def updateRecentUsed(self, node):
        self.doubly_linked_list.setHead(node)
        
    def removeLeastUsed(self):
        keyToRemove = self.doubly_linked_list.tail.key
        self.doubly_linked_list.removeTail()
        del self.cache[keyToRemove]
        
        
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def removeBinds(self):
        # remove prev and next bindings
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
        """
lRUCache.put(1, 1); // cache is {1=Node(1)}
                                    instead of {key: value}
                                                {key: node}
                                    setHead = Node(1)
                                    
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
                                    
    lRUCache.get(2);    // return 2
                                    linked list if we know the reference of node we are updating
                                    look up a value in linked list its O(n)
                                    3 <-> 1 <-> 2  <->  4
                                    get(3)
                                    cache[3] -> Node(3)
                                    Node(3)
                                    head
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
                                    
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4
        
        """