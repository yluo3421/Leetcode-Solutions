class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        thoughts:
        we can use a stack to check which paranthese is not valid
        we will always append ( idx to the stack
        if there is ( in stack and we found a ), pop stack
        if stack is empty, the curr one idx needs to be removed
        "lee(t(c)o)de)"
            ^
        after the string is traversed, we will combine
        whatever left in the stack with index removal set
        Together we have the set of idx to be removed.
        
        """
        idx_to_remove = set()
        stack = []
        for i, char in enumerate(s):
            if char not in "()":
                continue
            if char == "(":
                stack.append(i)
            elif not stack:
                idx_to_remove.add(i)
            else:
                stack.pop()
        idx_to_remove = idx_to_remove.union(set(stack))
        ans = []
        for i, char in enumerate(s):
            if i not in idx_to_remove:
                ans.append(char)
        return "".join(ans)
        