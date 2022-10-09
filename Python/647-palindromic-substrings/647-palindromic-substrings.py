class Solution:
    def countSubstrings(self, s: str) -> int:
        # thoughts:
        # instead of checking all substrings by using two for loops
        # we can check possible palindrom from each char
        # Meaning we need to start from char, and make sure left and right pointer
        # has the same char
        # but there is two posibility
        # palindrome length of odd number or length of even number
        # if it is odd, meaning the starting char is the center
        # if it is even, meaning the starting char and the next char are center
        # thus develop a method check palindrom from center
        # and use that method for i in range(len(s))
        ans = 0
        for i in range(len(s)):
            ans += self.checkPalindromeFromCenter(s, i, i)
            ans += self.checkPalindromeFromCenter(s, i, i + 1)
        return ans
    # to make this generic to both options
    # odd number, left = right
    # even number, right = left += 1
    # it should return number of palidrome found
    def checkPalindromeFromCenter(self, s, left, right):
        ans = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            ans += 1
            left -= 1
            right += 1
        return ans
    
        