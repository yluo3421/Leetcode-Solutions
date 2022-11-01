class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # thoughts:
        # sort the interval based on starting time
        # then push them into a new array
        # if the coming interval[0] > merged[-1][1]
        # meaning there is no conflict, append
        # if the coming interval[0] < merged[-1][1], change merged[-1][1] to max
        # of interval[1] merged[-1][1]
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        merged = []
        for interval in sorted_intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged