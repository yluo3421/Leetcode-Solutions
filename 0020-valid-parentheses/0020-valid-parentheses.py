class Solution:
    def isValid(self, s: str) -> bool:
        """
        thoughts:
        prepare a stack to store the curr char of the s
        if it's a open bracket
        push it into stack
        if its a close bracket, check dict this bracket's corresponding
        open bracket, compare with the top of stack
        if they matches, pop and move to the next
        if they dont, return False
        at the end, return len(stack) == 0
        
        """
        BRACKETS = {"}":"{", "]":"[",")":"("}
        stack = []
        for char in s:
            if char not in BRACKETS:
                stack.append(char)
                continue
            if not stack or stack[-1] != BRACKETS[char]:
                return False
            stack.pop()
        return len(stack) == 0