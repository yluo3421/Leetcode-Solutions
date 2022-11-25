class DataStream:

    def __init__(self):
        # do intialization if necessary
        #use array - hard to delete in the middle - need to keep sequence
        #use linked list
        #for delete use an hashmap
        
        #if already in hashmap: 
            #if marked : do nothing
            #if in the hash: 
                #remove from the linkedlist and mark this value
                #if remove the tail, need to change the value for the tail
        #else 
            #append to the end of linkedlist, add to the linked list
        self.dummy = ListNode(0)
        self.tail = self.dummy
        # hash 的 key 为 num，value 为对应的 linkedlist 上的 previous node
        self.num_to_prev = {}
        self.duplicates = set()
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        if num in self.duplicates:
            return
        
        if num not in self.num_to_prev:
            self.push_back(num)            
            return
        
        # find duplicate, remove it from hash & linked list
        self.duplicates.add(num)
        self.remove(num)
    
    def remove(self, num):
        prev = self.num_to_prev.get(num)
        del self.num_to_prev[num]
        prev.next = prev.next.next
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            # if we removed the tail node, prev will be the new tail
            self.tail = prev

    def push_back(self, num):
        # new num add to the tail
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        if not self.dummy.next:
            return None
        return self.dummy.next.val