from typing import (
    List,
)

class Solution:
    """
    @param n: The number of nodes
    @param starts: One point of the edge
    @param ends: Another point of the edge
    @param lens: The length of the edge
    @return: Return the length of longest path on the tree.
    """
    def longest_path(self, n: int, starts: List[int], ends: List[int], lens: List[int]) -> int:
        # Write your code here
        # if we use BFS on every node, it will become O(n^2)
        # we will run BFS twice, find the furthest node and then come back from that node
        adj_list = self.build_graph(starts, ends, lens)
        first_farthest, _ = self.bfs(0, adj_list)
        second_farthest, ans = self.bfs(first_farthest, adj_list)
        return ans
    
    def build_graph(self, starts, ends, lens):
        adj_list = {}
        for i in range(len(starts)):
            start, end, dist = starts[i], ends[i], lens[i]
            if start not in adj_list:
                adj_list[start] = []
            if end not in adj_list:
                adj_list[end] = []
            adj_list[start].append((end, dist))
            adj_list[end].append((start, dist))
        return adj_list

    # return farthest node, and distance from start to farthest node
    def bfs(self, root, adj_list):
        queue = collections.deque()
        distance_to_root = {}

        queue.append(root)
        distance_to_root[root] = 0

        max_distance = 0
        max_node = -1

        while queue:
            curr = queue.popleft()
            if max_distance < distance_to_root[curr]:
                max_distance = distance_to_root[curr]
                max_node = curr
            
            for neighbor, edge in adj_list[curr]:
                if neighbor in distance_to_root:
                    continue
                queue.append(neighbor)
                distance_to_root[neighbor] = distance_to_root[curr] + edge
        
        return (max_node, max_distance)