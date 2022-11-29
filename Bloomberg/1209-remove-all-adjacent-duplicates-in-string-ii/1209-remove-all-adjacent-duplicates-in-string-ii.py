class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # check each char and its k consecutive chars
        # if they are the same, remove.
        # re run the loop until all gone
        # one way to reduce is to only rerun the previous k chars
        # or to use stack
        # push the first letter in, check the next
        # if same, start counter till k
        # if not, keep pushing
        # if counter made to k, remove all of them 
        # then check next char and stack[-1]
        # store the char and count in the stack
        
        stack = [["#", 0]]
        for char in s:
            if stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        return "".join([k * c for c, k in stack])
                    
                    
                
            
                    