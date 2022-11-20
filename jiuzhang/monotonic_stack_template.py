for i from 0 to n - 1:
    while stack and 单调性不存在:
        记录此时的答案
        stack.pop()
    stack.push(i)