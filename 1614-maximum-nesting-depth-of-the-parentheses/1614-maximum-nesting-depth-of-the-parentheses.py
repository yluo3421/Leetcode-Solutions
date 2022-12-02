class Solution:
    def maxDepth(self, s: str) -> int:
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