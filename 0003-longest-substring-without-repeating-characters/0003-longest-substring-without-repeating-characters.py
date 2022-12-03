class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Thoughts:
        The brutal force is to check all chars
        That will take about O(n^3) time
        I want to use a sliding window method,
        that right pointer will move when no duplicates
        if there is a duplicate, left will start to move
        until right pointer char count reduce to 1
        This way I can do it in O(n) because the two pointer
        are moving seperately.
        The worst case is O(2n) where each char visited by
        left and right pointer.
        Space O(min(m, n))
        window needs O(k) where k is size of dict
        dict has upper bound of size of string size n and
        size of charset/alphabet m.
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
        