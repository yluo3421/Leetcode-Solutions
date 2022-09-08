from xml.dom.minidom import Notation


class Solution:
    def isValid(self, str: str)-> bool:
        # when there is no parentheses, only open parentheses can be added
        # if there is n open parentheses, only n close parenthese can be added
        # NOTATIONS is created to check if the current one is open/close
        # if current char open parentheses, add to stack
        # then jump to next char
        # if current char is close parenthese, check two conditions:
        # 1. no char in stack, we cannot add close parentheses, return False
        # 2. the top of stack is not corresponding parentheses 
        # of current char, return False
        # if both passed, pop the corresponding parenthese of current char
        NOTATIONS = {')': '(', '}':'{', ']':'['}
        stack = []
        for c in str:
            if c not in NOTATIONS:
                stack.append(c)
                continue
            if not stack or stack[-1] != NOTATIONS[c]:
                return False
            stack.pop()
        return not stack
