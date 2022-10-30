class Solution:
    def reverseWords(self, s: str) -> str:
        # put string into array of words
        # reverse and output
        # remove duplicate space 
        ans = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            else:
                j = i
                while j < len(s):
                    if s[j] != " ":
                        j += 1
                    else:
                        break
                ans.append(s[i:j])
                i = j
        return " ".join(ans[::-1])