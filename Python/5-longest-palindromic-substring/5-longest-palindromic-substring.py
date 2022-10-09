class Solution:
    def longestPalindrome(self, s: str) -> str:
        # thr brutal thoughts is to find palindrome from current char
        # starting from the char to check all odd and even palindrome
        # for odd and even, use two pointer to check
        
        # please note that left and right range check needs to be placed
        # prior to s[left] == s[right] to avoid out of range.
        ans = s[0]
        for i in range(0, len(s) - 1):
            # odd
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(ans):
                    ans = s[left:right + 1]
                left -= 1
                right += 1
            
            # even
            left, right = i, i + 1
            while right < len(s) and s[left] == s[right] and left >= 0:
                if (right - left + 1) > len(ans):
                    ans = s[left:right + 1]
                left -= 1
                right += 1
            
            
        return ans
            
                
             
        