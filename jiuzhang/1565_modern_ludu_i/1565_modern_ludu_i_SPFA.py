from typing import (
    List,
)

class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    """
    有的时候在遍历过程中一个点的distance被update到了一个更小的数字
    解决办法是当一个点的distance被更新的更短的时候要重新进入队列
    Shortest Path Fast Algorithm
    这个算法可以解决非简单图
    普通BFS不能解决复杂图的原因是我通过三层BFS找到的点可能比两层BFS能达到的点distance更小
            1
            /\
           4  2
          /  /
         5 - 3
    distance {1:0,4:2,2:1,3:1,5:3}

    我们可以用heap queue去优化
    在每个点的distance比较random的时候  heapqueue可以保证我们找到最佳的出发点
    
    """
    def modern_ludo(self, length: int, connections: List[List[int]]) -> int:
        # Write your code here
        graph = self.build_graph(length, connections)

        queue = collections.deque([1])
        distance = {
            i: float("inf")
            for i in range(1, length + 1)

        }
        distance[1] = 0
        # loop through all nodes
        while queue:
            node = queue.popleft()
            # go through all neighbors
            for next_node in graph[node]:
                if distance[next_node] > distance[node]:
                    distance[next_node] = distance[node]
                    queue.append(next_node)
            for next_node in range(node + 1, min(node + 7, length + 1)):
                if distance[next_node] > distance[node] + 1:
                    distance[next_node] = distance[node] + 1
                    queue.append(next_node)
        return distance(length)
            
    def build_graph(self, length, connections):
        graph = {i : set() for i in range(1, length + 1)}

        for start, end in connections:
            graph[start].add(end)
        return graph

    