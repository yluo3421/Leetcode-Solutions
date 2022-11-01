class Solution:
    WHITE = 1 # course not started
    GRAY = 2 # course visited
    BLACK = 3 # course finished, no more course beyond this one
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # thoughts:
        # we run dfs to generate the topological sorted order of the courses
        # first we create a graph of courses based on prerequisites
        # using defaultdict(list)
        # then we create a color dict initialized each course with WHITE
        # inside dfs
        # we are going to check visit the curr course's next array of course
        # if one of them is gray meaning cycle, we cant finish all courses
        # we will run all courses with dfs
        # returning the reverse of the topoligical order
        
        adj_list = defaultdict(list)
        for start, preq in prerequisites:
            adj_list[preq].append(start)
        
        color = {i: Solution.WHITE for i in range(numCourses)}
        topological_sorted_order = []
        
        is_cycle = False
        
        def dfs(node):
            nonlocal is_cycle
            if is_cycle:
                return
            
            color[node] = Solution.GRAY
            for neighbor in adj_list[node]:
                if color[neighbor] == Solution.WHITE:
                    dfs(neighbor)
                elif color[neighbor] == Solution.GRAY:
                    is_cycle = True
            
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)
        
        for node in range(numCourses):
            if color[node] == Solution.WHITE:
                dfs(node)
        return topological_sorted_order[::-1] if not is_cycle else []
                
                
        