import random
class RandomizedSet:

    def __init__(self):
        # thoughts:
        # cannot use set() because the getRandom wont work
        # the storage has to be using random generator with index
        # only dict or array available
        
        # dict can make insert O(1)
        # can make remove O(1)
        # use an array to allow using random.choice to get O(1)
        self.dict_storage = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.dict_storage:
            return False
        # assign current list size to the val inserted
        # this way it can be used as idx to refer val in array
        self.dict_storage[val] = len(self.array)
        self.array.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.dict_storage:
            # swap the last element with the val in array
            # so that pop can be used to remove at O(1) in array
            last_element, idx = self.array[-1], self.dict_storage[val]
            # temp = self.array[idx]
            # self.array[idx] = last_element # self.array[-1]
            # self.dict_storage[last_element] = idx
            # self.array.pop()
            self.array[idx], self.dict_storage[last_element] = last_element, idx
            self.array.pop()
            del self.dict_storage[val]
            return True
        return False
            

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()