from typing import (
    List,
)

class Solution:
    """
    @param s: the list of binary string
    @return: the max distance
    """
    def get_ans(self, s: List[str]) -> int:
        # Write your code here
        # find all combinations of two string, find their common
        # prefix length
        # find the max common prefix length 
        max_distance = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                length = self.get_lcp(s[i], s[j])
                max_distance = max(max_distance, len(s[i]) + len(s[j]) - 2 * length)
        return max_distance
    
    def get_lcp(self, a, b):
        n = min(len(a), len(b))
        for i in range(n):
            if a[i] != b[i]:
                return i
        return n