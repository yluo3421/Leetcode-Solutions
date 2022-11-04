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
        # dp[i] = min(dp[j] + 1, 0)
        # direct connected nodes will be 0
        graph = self.build_graph(length, connections)

        dp = [float("inf")] * (length + 1)
        dp[length] = 0
        for i in range(length + 1, 0, -1):
            for j in range(i + 1, min(i + 7, length + 1)):
                dp[i] = min(dp[i], dp[j] + 1)
            for j in graph[i]:
                dp[i] = min(dp[i], dp[j])
        return dp[1]

    def build_graph(self, length, connections):
        graph = {i : set() for i in range(1, length + 1)}

        for start, end in connections:
            graph[start].add(end)
        return graph