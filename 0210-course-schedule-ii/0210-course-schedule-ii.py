class Solution:
    WHITE = 1 # not started
    GRAY = 2 # checked
    BLACK = 3 # finished
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # thoughts:
        """
        create a adj_list using defaultdict
        mark all courses as WHITE
        we will need to dfs all courses that is WHITE
        inside dfs
        we fist check if is_cycle, return
        find all neighbors of the curr course, 
        if one of the neighbor is gray, meaning cycle
        otherwise mark all visited neighbors as GRAY
        after loop mark curr as BLACK
        append to the topological order
        
        after all nodes, return the reverse of the topological order
        
        """
        adj_list = defaultdict(list)
        for start, end in prerequisites:
            adj_list[end].append(start)
        
        colors = {i: Solution.WHITE for i in range(numCourses)}
        
        topological_sorted_order = []
        
        is_cycle = False
        
        def dfs(node):
            nonlocal is_cycle
            if is_cycle:
                return
            colors[node] = Solution.GRAY
            for neighbor in adj_list[node]:
                if colors[neighbor] == Solution.GRAY:
                    is_cycle = True
                elif colors[neighbor] == Solution.WHITE:
                    dfs(neighbor)
            colors[node] = Solution.BLACK
            topological_sorted_order.append(node)
        
        for node in range(numCourses):
            if colors[node] == Solution.WHITE:
                dfs(node)
        return topological_sorted_order[::-1] if not is_cycle else []
        