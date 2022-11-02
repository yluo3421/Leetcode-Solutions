class RandomizedCollection:

    def __init__(self):
        self.val_idx_dict = defaultdict(set)
        self.storage = []

    def insert(self, val: int) -> bool:
        self.val_idx_dict[val].add(len(self.storage))
        self.storage.append(val)
        return len(self.val_idx_dict[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.val_idx_dict[val]:
            return False
        else:
            last = self.storage[-1]
            to_be_removed = self.val_idx_dict[val].pop()
            self.storage[to_be_removed] = last
            self.val_idx_dict[last].add(to_be_removed)
            self.val_idx_dict[last].discard(len(self.storage) - 1)
            self.storage.pop()
            return True

    def getRandom(self) -> int:
        return choice(self.storage)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()