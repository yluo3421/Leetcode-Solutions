class Timemap:

    def __init__(self) -> None:
        # initialize with empty dict
        self.keyStorage = {}
        # the intended storeage will be 
        # {"key": [value1, timeStamp1], [value2, timeStamp2]}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        # the set method is simple
        # You can use defaultdict to avoid the first check
        if key not in self.keyStorage:
            self.keyStorage[key] = []
        self.keyStorage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # find the closest timestamp's key value
        # if no timestamp exactly equal to target, find the lower but closer one
        # if the timestamp at mid value is larger than target
        # keep searching for the left half
        ans = ""
        values = self.keyStorage.get(key, [])

        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return ans