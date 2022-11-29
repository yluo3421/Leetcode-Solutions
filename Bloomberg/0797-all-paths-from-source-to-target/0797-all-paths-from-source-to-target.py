class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # thoughts:
        # dfs and stack
        # push node's connected ones to stack, and visit them
        # if node's not connected to any ones, append array of nodes to ans
        ans = []
        
        def dfs(path):
            if path[-1] == len(graph) - 1: 
                ans.append(path)
            else:
                for child in graph[path[-1]]:
                    dfs(path + [child])
        dfs([0])
        return ans
            