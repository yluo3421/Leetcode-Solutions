class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use two pointer
        # right will keep increasing until duplicates
        # left will move until no duplicates
        # use a set to add and remove char
        left = 0
        char_set = set()
        max_length = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
                
        