class MyHashSet:

    def __init__(self):
        """
        An array with traversal of O(n) can do the trick
        but all methods average O(n)
        To make O(1), we need to hash each key into an index
        If two different keys has same hash_index, traverse
        the bucket at the array[hash_index]
        As long as the hash is big enough, these operations
        can be O(1) average. 
        So I'd like to use the array as a container for all buckets
        where bucket will have index as the hash value of key
        And the bucket at array[hash_index] will store it
        The optimal length of  array should be about 1.3 times
        of actual number of keys to be stored and it should 
        be a prime number.
        Since the question gave us constraint that key is less than 10^6
        The prime should be larger than 130000, and the 
        prime is 130003.
        """
        self.array = [False] * 1300003
        
    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.array[key] = True
        

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.array[key] = False
        return

    def contains(self, key: int) -> bool:
        if self.array[key]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)