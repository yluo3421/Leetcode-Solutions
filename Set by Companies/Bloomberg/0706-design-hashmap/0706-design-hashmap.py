class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for idx, key_value_pair in enumerate(self.bucket):
            if key == key_value_pair[0]:
                self.bucket[idx] = (key, value)
                found = True
                break 
        
        if not found:
            self.bucket.append((key, value))
    
    def remove(self, key):
        for idx, key_value_pair in enumerate(self.bucket):
            if key == key_value_pair[0]:
                del self.bucket[idx]


class MyHashMap:
    """
    to implement a hashmap, we need a way to hash the key entered
    The easier way is to modulo by a large prime number
    lets use 10007 as our prime

    There are still chances that we run into same hash_key,
    So we need a bucket to hold (key, value) pairs with the same has
    hash_key.
    In this case we are using array of array to store it.
    To simplify the coding, class of bucket will be implemented
    In side class Bucket, we need get, update, remove.
    hash_table = [0,1,3,4...,prime_num - 1]
    hash_tabel[i] = Bucket() = [(key1, value1), (key2, value2)...]
    
    """
    def __init__(self):
        self.prime_num = 10007
        self.hash_table = [Bucket() for _ in range(self.prime_num)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.prime_num
        self.hash_table[hash_key].update(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.prime_num
        return self.hash_table[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.prime_num
        self.hash_table[hash_key].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)