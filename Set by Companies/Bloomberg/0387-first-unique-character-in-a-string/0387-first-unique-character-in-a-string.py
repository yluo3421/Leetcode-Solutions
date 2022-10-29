class Solution:
    def firstUniqChar(self, s: str) -> int:
        # use dict to record freq of each char
        char_dict = collections.Counter(s)
        for idx, char in enumerate(s):
            if char_dict[char] == 1:
                return idx
        return -1
            