import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # to allow duplicates, we will save list of index in dict
        self.array = []
        self.dict_storage = collections.defaultdict(set)
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.dict_storage[val].add(len(self.array))
        self.array.append(val)
        return len(self.dict_storage[val]) == 1
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.dict_storage[val]:
            return False
        curr_idx = self.dict_storage[val].pop()
        last_element = self.array[-1]
        self.dict_storage[last_element].add(curr_idx)
        self.array[curr_idx] = last_element
        self.dict_storage[last_element].discard(len(self.array) - 1)
        self.array.pop()
        if len(self.dict_storage[val]) == 0:
            del self.dict_storage[val]
        return True
        


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.array)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()