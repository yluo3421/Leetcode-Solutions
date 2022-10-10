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
        
        # create a min arr to record min char from current char to end of s
        min_arr = []
        stack = []
        for i in range(len(s) - 1, -1, -1):
            stack.append(s[i])
            if min_arr:
                if ord(min_arr[-1]) > ord(s[i]):
                    min_arr.append(s[i])
                else:
                    prev_min = min_arr[-1]
                    min_arr.append(prev_min)
            else:
                min_arr.append(s[i])
        min_arr.reverse()
        
        t = []
        ans = []
        left, right = 0, 0
        while left < len(s) and right < len(s):
            # find where min char is
            while s[right] != min_arr[right]:
                right += 1
            if right + 1 < len(s):
                curr_min_idx = right + 1
            else:
                curr_min_idx = -1
            # push all char till min char to t
            while left <= right:
                t.append(s[left])
                left += 1
               
            right = left
            
            # compare t[-1] and remaining min char
            while t and ord(t[-1]) <= ord(min_arr[curr_min_idx]):
                ans.append(t.pop())
            
        while t:
            ans.append(t.pop())
        return "".join(ans)
            