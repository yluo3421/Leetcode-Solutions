class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # thoughts
        # use dict to record both string
        # add up absolute of diff of each char in both dict
        # then divided by 2
        char_s, char_t = {}, {}
        for char in s:
            char_s[char] = char_s.get(char, 0) + 1
        for char in t:
            char_t[char] = char_t.get(char, 0) + 1
        for char in t:
            if char not in s:
                char_s[char] = 0
        for char in s:
            if char not in t:
                char_t[char] = 0
        ans = 0       
        for char in char_s.keys():
            ans += abs(char_s[char] - char_t[char])
        return int(ans/2)
        