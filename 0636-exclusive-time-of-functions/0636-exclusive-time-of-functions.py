class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans, stack = [0]*n, []
        for log in logs:
            f_id, event, time = log.split(':') 
            f_id, time = int(f_id), int(time)
            if event=='start':
                if stack:
                    ans[stack[-1][0]] += time-stack[-1][1]
                stack.append([f_id, time])
            else:
                curr = stack.pop()
                ans[curr[0]] += time - curr[1] + 1
                if stack:
                    stack[-1][1] = time + 1
        return ans