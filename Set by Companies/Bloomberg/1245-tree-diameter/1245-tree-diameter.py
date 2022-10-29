from collections import deque
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # diameter = longest tree path sum
        # thoughts:
        # we use bfs find the node that is farthest from start,
        # then next bfs finr the farthest from the curr node
        # to make this happend, we need to create a graph using edges

        # this graph is set for each nodes
        # every edge connects two nodes
        # both nodes set should be added with each other
        graph = [set() for i in range(len(edges) + 1)]
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)
        
        # use bfs to find the farthest node
        def bfs(start: int):
            visited = [False] * len(graph)
            visited[start] = True
            queue = deque([start])
            distance = -1
            last_node = -1
            while queue:
                n = len(queue)
                for i in range(n):
                    next_node = queue.popleft()
                    for neighbor in graph[next_node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                            last_node = neighbor
                distance += 1
            return last_node, distance
        
        farthest_node, distance_1 = bfs(0)
        
        next_farthest_node, distance_2 = bfs(farthest_node)

        return distance_2

