class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # find the longest palindrom within the string,
        # everyting outside of it needs to be compensated
        # aabaacd = aabaa + cd
        # the answer is to add dc at the front dc + aabaa + cd
        # cd is the reverse of prefix added
        # so target is to find the longest palindrome start from beginning
        # then reverse the remaining part and add to front
        if not s:
            return ""
        
        for i in range(len(s), -1, -1):
            substring = s[:i]
            if substring == substring[::-1]:
                suffix = s[i:]
                return suffix[::-1] + s

                
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        j=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==s[j]:
                j+=1
        
        if len(s)==j:
            return s
        # print("index j ",j)
        suffix=s[j:]
        # print("suffix ",suffix)
        # print("reverse suffix ",suffix[::-1])
        return suffix[::-1]+ self.shortestPalindrome(s[0:j])+suffix