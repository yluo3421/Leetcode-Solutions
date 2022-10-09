class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        # thoughts:
        # go through each log to find out each time and record them
        # find the one with max and return the smaller id
        currStartTime = 0
        employeeWorkTime = {}
        for item in logs:
            currId, currEndTime = item
            currWorkTime = currEndTime - currStartTime
            if currId in employeeWorkTime:
                if currWorkTime > employeeWorkTime[currId]:
                    employeeWorkTime[currId] = currWorkTime
            else:
                employeeWorkTime[currId] = currWorkTime
            
            currStartTime = currEndTime
        maxWorkTime = max(employeeWorkTime.values())
        print(maxWorkTime)
        print(employeeWorkTime)
        valid_keys = []
        for key in employeeWorkTime.keys():
            if employeeWorkTime[key] == maxWorkTime:
                valid_keys.append(key)
        return min(valid_keys)
        