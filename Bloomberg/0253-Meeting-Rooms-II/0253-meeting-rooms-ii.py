class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # thoughts
        # if there is a conflict, meaning needs two meeting room
        
        # we will have meetings ongoing and we need to check
        # ongoing's end time against coming start time
        # we could use stack but it doesn't allow us to manipulate
        # multiple meeting rooms
        # another thought is to use minheap to keep track of the 
        # cloest room to be freed
        if not intervals:
            return 0
        free_rooms = []
        
        sorted_intervals = sorted(intervals, key = lambda x:x[0])
        
        heapq.heappush(free_rooms, sorted_intervals[0][1])
        for interval in sorted_intervals[1:]:
            if free_rooms[0] <= interval[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, interval[1])
        
        return len(free_rooms)
        
        
            
        