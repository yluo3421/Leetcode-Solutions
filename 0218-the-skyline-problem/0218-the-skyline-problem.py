class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        Do the second solution first
        In the previous sweep line approach, we had to iterate through all the buildings at each position and ended up with O(n^2)time complexity. 
 
        Notice that the current height is only decided by the tallest "live" building, hence we no longer need to traverse over all the buildings if we can get the tallest "live" building directly! This can be implemented by using a priority queue
        
        2.Iterate over buildings and store each building's edges separately with the building's index as a reference in edges.
3.Sort the entries in edges by their first element.
4.Iterate over the sorted edges and for each edge/index:
        If buildings[b][0] == curr_x, meaning its a left edge and the building[b] is live,we add (height, right) to live.
        While the tallest live building has been passed, remove it from live.
5.Once we finish handling all the edges at the curr_x, we shall move on to the next position.
After the iteration, return answer as the skyline.

        Time O(nlog(n)) | Space O(n)
        we have O(n) live buildings in live, both the pop and push operations take O(logn) time.
        """
        # Iterate over all buildings, for each building i,
        # add (position, i) to edges.
        edges = []
        for i, build in enumerate(buildings):
            edges.append([build[0], i])
            edges.append([build[1], i])

        # Sort edges by non-decreasing order.
        edges.sort()
     
        # Initailize an empty Priority Queue 'live' to store all the 
        # newly added buildings, an empty list answer to store the skyline key points.
        live, answer = [], []
        idx = 0
        
        # Iterate over all the sorted edges.
        while idx < len(edges):
            
            # Since we might have multiple edges at same x,
            # Let the 'curr_x' be the current position.
            curr_x = edges[idx][0]
            
            # While we are handling the edges at 'curr_x':
            while idx < len(edges) and edges[idx][0] == curr_x:
                # The index 'b' of this building in 'buildings'
                b = edges[idx][1]
                
                # If this is a left edge of building 'b', we
                # add (height, right) of building 'b' to 'live'.
                if buildings[b][0] == curr_x:
                    right = buildings[b][1]
                    height = buildings[b][2]
                    heapq.heappush(live, [-height, right])
                    
                # If the tallest live building has been passed,
                # we remove it from 'live'.
                while live and live[0][1] <= curr_x:
                    heapq.heappop(live)
                idx += 1
            
            # Get the maximum height from 'live'.
            max_height = -live[0][0] if live else 0
            
            # If the height changes at this curr_x, we add this
            # skyline key point [curr_x, max_height] to 'answer'.
            if not answer or max_height != answer[-1][1]:
                answer.append([curr_x, max_height])
        
        # Return 'answer' as the skyline.
        return answer
        
        
        """
        Sweep Line O(n^2) needs optimization
        """
        # Collect and sort the unique positions of all the edges.
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))
        
        # 'answer' for skyline key points
        answer = []
        
        # For each position, draw an imaginary vertical line.
        for position in positions:
            # current max height.
            max_height = 0
            
            # Iterate over all the buildings:
            for left, right, height in buildings:
                # Update 'max_height' if necessary.
                if left <= position < right:
                    max_height = max(max_height, height)
            
            # If its the first key point or the height changes, 
            # we add [position, max_height] to 'answer'.
            if not answer or max_height != answer[-1][1]:
                answer.append([position, max_height])
                
        # Return 'answer' as the skyline.
        return answer