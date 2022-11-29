from typing import (
    List,
)

class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longest_common_prefix(self, strs: List[str]) -> str:
        
        # write your code here
        # brutal force
        # find the lcp of two strings
        # compare all strings one by open
        # because lcp(s1, s2) can be used in lcp(lcp(s1,s2), s3)...
        if not strs:
            return ""
        prefix = strs[0]
        total_number = len(strs)
        for i in range(1, total_number):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        return prefix
    
    def lcp(self, s1, s2):
        length = min(len(s1), len(s2))
        idx = 0
        while idx < length and s1[idx] == s2[idx]:
            idx += 1
        return s1[:idx]

        