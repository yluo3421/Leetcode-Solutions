from typing import (
    List,
)
class GridType:
    EMPTY = 0
    HOUSE = 1
    WALL = 2
class Solution:
    """
    
    """
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        min_dist = float("inf")

        for i in range(n):
            for j in range(m):
                if grid[i][j] == GridType.EMPTY:
                    distance = self.bfs(grid, i, j)
                    min_dist = min(min_dist, self.get_distance_sum(distance, grid))
        return min_dist if min_dist != float("inf") else -1
    
    def bfs(self, grid, i, j):
        distance = {(i, j): 0}
        queue = collections.deque([(i, j)])

        while queue:
            x, y = queue.popleft()
            DIRECTIONS = [(1,0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in DIRECTIONS:
                adj_x, adj_y = x + dx, y + dy
                if not self.is_valid(adj_x, adj_y, grid):
                    continue
                if (adj_x, adj_y) in distance:
                    continue
                distance[(adj_x, adj_y)] = distance[(x, y)] + 1
                if grid[(adj_x, adj_y)] == GridType.EMPTY:
                    queue.append((adj_x, adj_y))
        return distance
    
    def get_distance_sum(self, distance, grid):
        distance_sum = 0
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val == GridType.HOUSE:
                    if (x, y) not in distance:
                        return float("inf")
                    distance_sum += distance[(x, y)]
        return distance_sum
    
    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return grid[x][y] in [GridType.EMPTY,GridType.HOUSE]


