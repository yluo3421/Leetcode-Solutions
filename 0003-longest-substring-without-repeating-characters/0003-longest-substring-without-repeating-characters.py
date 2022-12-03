class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Thoughts:
        The brutal force is to check all chars
        That will take about O(n^3) time
        
        """
        chars = defaultdict(int)
        left, right = 0, 0
        ans = 0
        n = len(s)
        
        while right < n:
            right_char = s[right]
            chars[right_char] += 1
            while chars[right_char] > 1:
                left_char = s[left]
                chars[left_char] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
            right += 1
        return ans
        