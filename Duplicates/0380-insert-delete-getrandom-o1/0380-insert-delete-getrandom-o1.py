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
        if val not in self.dict_storage:
            self.dict_storage[val] = len(self.array)
            self.array.append(val)
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val in self.dict_storage:
            curr_idx = self.dict_storage[val]
            last_element = self.array[-1]
            last_element_idx = self.dict_storage[last_element]
            self.array[curr_idx], self.array[last_element_idx] = self.array[last_element_idx], self.array[curr_idx]
            self.dict_storage[last_element] = curr_idx
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