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
        # first draw the graph, including both nodes from start and from end
        adj_list = self.build_graph(starts, ends, lens)
        _, path = self.dfs(0, -1, adj_list)
        return path
    
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
    
    # pass parent to avoid backward dfs
    def dfs(self, root, parent, adj_list):
        longest_chain = 0
        longest_path = 0

        child_longest_chain = 0
        child_second_longest_chain = 0

        for neighbor, dist in adj_list[root]:
            if neighbor == parent:
                continue
                
            child_chain, child_path = self.dfs(neighbor, root, adj_list)
            child_chain += dist

            longest_chain = max(child_chain, longest_chain)
            longest_path = max(child_path, longest_path)

            _, child_second_longest_chain, child_longest_chain = \
                sorted([child_longest_chain, child_second_longest_chain, child_chain])
        
        longest_path = max(child_longest_chain + child_second_longest_chain, longest_path)

        return [longest_chain, longest_path]