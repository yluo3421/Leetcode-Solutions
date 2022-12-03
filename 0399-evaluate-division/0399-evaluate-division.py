# from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        
        We have a/b = 2, b/c = 3
        we can derive b/a = 1/2, c/b = 1/3
        And also a/c = 6
        We can build this into a graph with both direction's weight
        as the values calculated above
        This makes the problem to a graph question to find a path
        between the query's two elements
        I will build a adjacent list using defaultdict and
        then use a dfs here
        During the search, 
        if either of nodes are in the graph, no ans
        if origin and destination are the same, return 1
        
        
        """
        graph = defaultdict(defaultdict)
        graph = self.build_graph(graph, equations, values)
        
        ans = []
        for dividend, divisor in queries:
            print(dividend)
            print(divisor)
            if dividend not in graph or divisor not in graph:
                ret = -1.0
            elif dividend == divisor:
                ret = 1.0
            else:
                visited = set()
                ret = self.dfs(graph, dividend, divisor, 1, visited)
            ans.append(ret)
        return ans
        
    def build_graph(self, graph, equations, values):
        # dividend / divisor = value
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
        return graph
            
    def dfs(self, graph, curr_node, target_node, accumulative_product, visited):
        visited.add(curr_node)
        ret = -1.0
        neighbors = graph[curr_node]
        if target_node in neighbors:
            ret = accumulative_product * neighbors[target_node]
        else:
            for neighbor, value in neighbors.items():
                if neighbor in visited:
                    continue
                ret = self.dfs(graph, neighbor, target_node, accumulative_product * value, visited)
                if ret != -1.0:
                    break
        visited.remove(curr_node)
        return ret
        