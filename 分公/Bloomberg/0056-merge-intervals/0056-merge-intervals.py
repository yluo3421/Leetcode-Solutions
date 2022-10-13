class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # thoughts:
        # go through all intervals and compare their start time and end time
        # if the 2ndStart is less than 1stEnd, two can be merged
        # keep merging until no more merge can be done
        
        # not sure if they are sorted
        
        if len(intervals) == 1:
            return intervals
        sorted_intervals = sorted(intervals, key=lambda x: x[0] )
        merged = []
        for interval in sorted_intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
        
        """ 
        The method below was the original thoughts
        I over complicate the process
        I only need to append the current one, and compare the next one
        and compared the last item in merged with the current one
        
        
        if len(intervals) == 1:
            return intervals
        sorted_intervals = sorted(intervals, key=lambda x: x[0] )
        def merge_helper(first_interval, second_interval):
            start1, end1 = first_interval[0], first_interval[1]
            start2, end2 = second_interval[0], second_interval[1]
            if end1 >= start2:
                new_start = min(start1, start2)
                new_end = max(end1, end2)
                return [new_start, new_end]
            else:
                return False
        ans = []
        i = 0
        while i < len(sorted_intervals) - 1:
            first_interval = sorted_intervals[i]
            second_interval = sorted_intervals[i + 1]
            print(first_interval)
            print(second_interval)
            if not merge_helper(first_interval, second_interval):
                
                ans.append(first_interval)
                if i == len(sorted_intervals) - 2:
                    ans.append(second_interval)
                i += 1
            else:
                ans.append(merge_helper(first_interval, second_interval))
                i += 2
        return ans
        """