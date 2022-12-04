class RandomizedSet:

    def __init__(self):
        self.array = []
        self.dict_storage = {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val not in self.dict_storage:
            self.dict_storage[val] = len(self.array)
            self.array.append(val)
            return True
        else:
            False

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val in self.dict_storage:
            curr_idx = self.dict_storage[val]
            last_element = self.array[-1]
            last_idx = self.dict_storage[last_element]
            self.array[curr_idx], self.dict_storage[last_element] = last_element, curr_idx
            self.array.pop()
            del self.dict_storage[val]
            return True

        return False

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()