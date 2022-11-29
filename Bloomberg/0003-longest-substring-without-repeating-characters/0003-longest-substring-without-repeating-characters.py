class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # thoughts
        # loop through the s and push char into set
        # record curr max
        # use left and right pointer, move left while meet duplicate
        # the left will move until no duplicates
        # the right will move until duplicate
        
        left, right = 0, 0
        char_set = set()
        max_length = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
            
                
        
            