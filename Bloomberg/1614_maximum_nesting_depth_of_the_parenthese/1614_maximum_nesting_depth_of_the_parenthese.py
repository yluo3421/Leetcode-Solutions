class Solution:
    def maxDepth(self, s: str) -> int:
        # idea is that the depth only calculated by number of
        # open parentheses
        # so when see open parenthese we add count by 1
        # and update max count so far
        max_count = 0
        parenthese_count = 0
        n = len(s)
        for i in range(n):
            if s[i] == "(":
                parenthese_count += 1
                max_count = max(max_count, parenthese_count)
            elif s[i] == ")":
                parenthese_count -= 1
        return max_count
        