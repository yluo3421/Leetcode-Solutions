class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use a defaultdict to create adjacency list
        adj_list = defaultdict(list)
        for dest, preq in prerequisites:
            adj_list[preq].append(dest)
        
        color = {i: Solution.WHITE for i in range(numCourses)}
        topological_sorted_order = []
        
        is_cycle = False
        
        def dfs(node):
            # return when cycle
            # modify topological_sorted_order
            # mark the current visiting node as gray
            # visit neighbors who is still white, and dfs(neighbor)
            # after all neighbors, meaning we reached end node on one path
            # mark this curr node as black
            nonlocal is_cycle
            
            if is_cycle:
                return
            
            color[node] = Solution.GRAY
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                        is_cycle = True
            
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)
            
        for vertex in range(numCourses):
            if color[vertex] == Solution.WHITE:
                dfs(vertex)
        return topological_sorted_order[::-1] if not is_cycle else []
        