class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        As we know now, it is a problem of Eulerian path, except that we have a fixed starting point.

More importantly, as stated in the problem, the given input is guaranteed to have a solution. So we have one less issue to consider.

As a result, our final algorithm is a bit simpler than the above Eulerian path algorithm, without the backtracking step.
The essential step is that starting from the fixed starting vertex (airport 'JFK'), we keep following the ordered and unused edges (flights) until we get stuck at certain vertex where we have no more unvisited outgoing edges.
        """
        
    
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.route = []
        self.adj_list = defaultdict(list)
        for i,j in tickets:
            self.adj_list[i].append(j)
        for key in self.adj_list: 
            self.adj_list[key] = sorted(self.adj_list[key], reverse=True)
            
        self.dfs("JFK")
        return self.route[::-1]
    def dfs(self, airport):
        while self.adj_list[airport]:
            candidate = self.adj_list[airport].pop()
            self.dfs(candidate)
        self.route.append(airport)
            