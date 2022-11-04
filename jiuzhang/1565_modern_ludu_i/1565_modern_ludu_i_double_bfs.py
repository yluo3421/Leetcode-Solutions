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

        queue = collections.deque([1])
        distance = {1: 0}
        # loop through all nodes
        while queue:
            node = queue.popleft()
            # go through all neighbors
            for neighbor in range(node + 1, min(node + 7, length + 1)):
                # get the direct connected nodes
                connected_nodes = self.get_unvisited_nodes(graph, distance, neighbor)
                # mark direct connected nodes as distance + 1
                for connected_node in connected_nodes:
                    distance[connected_node] = distance[node] + 1
                    queue.append(connected_node)
        return distance[length]

    def build_graph(self, length, connections):
        graph = {i : set() for i in range(1, length + 1)}

        for start, end in connections:
            graph[start].add(end)
        return graph

    # here distance are passed to ensure each node only visited once
    # this way the two BFS time complexity will be added together instead
    # of mutiply together.
    def get_unvisited_nodes(self, graph, distance, node):
        from collections import deque
        queue = deque([node])
        unvisited_nodes = set()
        while queue:
            node = queue.popleft()
            if node in distance:
                continue
            unvisited_nodes.add(node)
            for neighbor in graph[node]:
                if neighbor not in distance and neighbor not in unvisited_nodes:
                    queue.append(neighbor)
                    unvisited_nodes.add(neighbor)
        return unvisited_nodes
        
