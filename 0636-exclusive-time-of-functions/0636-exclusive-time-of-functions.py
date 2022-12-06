class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        Use a stack to do all the work
        we will go through the log and find out the function id
        we are dealing with 
        With the middle element telling us if it is a start time or end time
        If start time, we should push this log into stack
        but before that we need to check if there
        is any other funciton in the stack
        We will give the top of stack function the running time between
        the two function's start time.
        If end time, we should pop out the curr stack top function
        and give it the time it has ran so far
        and if there are more function in the stack waiting for record
        we need to update its time.
        """
        ans, stack = [0]*n, []
        for log in logs:
            f_id, event, time = log.split(':') 
            f_id, time = int(f_id), int(time)
            if event == 'start':
                if stack:
                    ans[stack[-1][0]] += time - stack[-1][1]
                stack.append([f_id, time])
            else:
                curr = stack.pop()
                ans[curr[0]] += time - curr[1] + 1
                if stack:
                    stack[-1][1] = time + 1
        return ans