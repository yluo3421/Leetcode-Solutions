class Solution:
    def robotWithString(self, s: str) -> str:
        # thoughts
        # go through string 
        # if next char is smaller than or equal to the curr char
        # continuer counter 
        # if next char is larger than curr char
        # push current section to t
        # print t
        # repeat above process untill all char printed
        
        left, right = 0, 1
        ans = ""
        while left < len(s) and right < len(s):
            if ord(s[left]) <= ord(s[right]):
                right += 1
            else:
                for i in range(right, left - 1, -1):
                    ans += s[i]
                left = right + 1
                right = left + 1
        
        if left == len(s) - 1:
            ans += s[left]
        return ans
            