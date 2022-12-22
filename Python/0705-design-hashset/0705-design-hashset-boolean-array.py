class MyHashSet:

    def __init__(self):
        """
        
        The prime should be larger than 1300000, and the 
        prime is 1300003.
        The idea is not to hash each key but use them directly
        as the index, and the array will store Ture or False to show
        if the current key exists in the set
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