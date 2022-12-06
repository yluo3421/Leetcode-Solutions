class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_array = [0] * 26
        n = len(s)
        for i in range(n):
            char_array[ord(s[i]) - ord("a")] += 1
            char_array[ord(t[i]) - ord("a")] -= 1
        for count in char_array:
            if count != 0:
                return False
            
        return True