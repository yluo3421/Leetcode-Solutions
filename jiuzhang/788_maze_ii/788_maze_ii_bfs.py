from typing import (
    List,
)
from collections import deque
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    BFS
    """
    def shortest_distance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # write your code here
        n = len(maze)
        m = len(maze[0])
        distance = [[float("inf") for _ in range(m)] for _ in range(n)]
        distance[start[0]][start[1]] = 0
        queue = deque([start])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            i, j = queue.popleft()
            
            for dx, dy in dirs:
                count = 0
                row = i + dx
                col = j + dy
                while row in range(n) and col in range(m) and maze[row][col] == 0:
                    row += dx
                    col += dy
                    count += 1
                # not sure why count doesnt need to be -= 1
                row -= dx
                col -= dy
                # if start point and count together is less than recorded steps at curr location
                # update the count and add it to queue
                if distance[i][j] + count < distance[row][col]:
                    distance[row][col] = distance[i][j] + count
                    queue.append([row, col])
        return -1 if distance[destination[0]][destination[1]] == float("inf") else distance[destination[0]][destination[1]]
                



