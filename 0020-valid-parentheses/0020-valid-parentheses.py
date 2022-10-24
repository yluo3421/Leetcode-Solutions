class Solution:
    def isValid(self, s: str) -> bool:
        BRACKETS = {"}":"{", "]":"[", ")":"("}
        stack = []
        for char in s:
            if char not in BRACKETS:
                stack.append(char)
                continue
            if not stack or stack[-1] != BRACKETS[char]:
                return False
            stack.pop()
        return len(stack) == 0