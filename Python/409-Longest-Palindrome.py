class Solution:
    def longestPalindrome(self, s: str) -> int:
        # thoughts:
        # record all char's occurance using a dict
        # if the occurance can be divided by 2
        # meaning it can become part of the palindrom
        # if not, there still value // 2 * 2 number of char can be used
        # but at the end, one more char can be added as the center
        charDict = {}
        for char in s:
            charDict[char] = charDict.get(char, 0) + 1
        ans = 0
        temp = False
        for value in charDict.values():
            if value % 2 == 0:
                ans += value / 2 * 2
            if ans % 2 == 0 and value % 2 == 1:
                ans += value // 2 * 2
                
        
        return int(ans)
        