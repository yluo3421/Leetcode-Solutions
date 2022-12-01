class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        the idea is to go through all nodes and find all paths
        Since all paths needs to be find, back-tracking with dfs 
        is a good choice
        I want to confirm that we only have one start, one target
        And no inner loop.
        The dfs will be a recursive call until we found one path 
        that ends with target
        After that, we will pop the last node visited and goes to
        the next node

        """
        target = len(graph) - 1
        ans = []
        def dfs(curr_node, path):
            if curr_node == target:
                ans.append(list(path))
                return
            for neighbor in graph[curr_node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()
        path = [0]
        dfs(0, path)
        return ans

