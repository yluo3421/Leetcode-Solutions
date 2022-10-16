class Solution:
    def decodeString(self, s: str) -> str:
        # because the inner most layer cannot be calculated until found
        # its outter layer.
        # thoughts:
        # to use stack to check what is included in the open bracket
        # use another stack to store the corresoponding repeat times
        # not sure if k only < 10
        # push number to a seperate array and combine them to push into stack
        # use two stack
        # one is repeat time
        # one is repeat string
        # how to tell if they are single repeat
        
        # use single stack
        # stack to store currString and currNum
        #
        # the ], grab prevString from stack.pop(), grab prevNum from stack.pop()
        # currString = prevString + currString * prevNum
        # the [, push currString, currNum into stack, reset them to inital value
        # digit use currNum = currNum * 10 + int(c)
        # currString = currString + char
        
        stack = []
        currNum = 0
        currString = ""
        for char in s:
            if char == "[":
                stack.append(currString)
                stack.append(currNum)
                currString = ""
                currNum = 0
            elif char == "]":
                prevNum = stack.pop()
                prevString = stack.pop()
                currString = prevString + currString * prevNum
            elif char.isdigit():
                currNum = currNum * 10 + int(char)
            elif char.isalpha():
                currString += char
        return currString
            
        
        
        