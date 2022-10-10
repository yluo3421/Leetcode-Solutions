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
        
        endChar = s[-1]
        left, right = 0, 0
        t = []
        ans = []
        # if right < endChar
        # right += 1
        # else append substring to t
        # print t
        # cabepoqf
        
        # bydizefve
        # 
        
        while left < len(s) and right < len(s):
            if ord(s[right]) >= ord(endChar):
                right += 1
            else:
                while left <= right:
                    t.append(s[left])
                    left += 1
                right = left
                while t:
                    if ord(t[-1]) < ord(endChar):
                        ans.append(t.pop())
                    else:
                        break
        
        if left < right:
            for i in range(left, right):
                t.append(s[i])
        while t:
            ans.append(t.pop())
        return "".join(ans)
# some cases not working
            