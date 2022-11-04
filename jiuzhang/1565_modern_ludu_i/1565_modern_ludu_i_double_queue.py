from typing import (
    List,
)

class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modern_ludo(self, length: int, connections: List[List[int]]) -> int:
        # Write your code here
        graph = self.build_graph(length, connections)

        # array will be enough here because we dont need popleft()
        queue = [1]
        distance = {1: 0}
        # loop through all nodes
        while queue:
            next_queue = []
            # we first found all direct connected nodes and add them to the curr queue
            # then next step to check node in next level
            for node in queue:
                for direct_node in graph[node]:
                    if direct_node in distance:
                        continue
                    distance[direct_node] = distance[node]
                    queue.append(direct_node)
            
            for node in queue:
                for next_node in range(node + 1, min(node + 7, length + 1)):
                    if next_node in distance:
                        continue
                    distance[next_node] = distance[node] + 1
                    next_queue.append(next_node)
            queue = next_queue
        return distance[length]

    def build_graph(self, length, connections):
        graph = {i : set() for i in range(1, length + 1)}

        for start, end in connections:
            graph[start].add(end)
        return graph

    