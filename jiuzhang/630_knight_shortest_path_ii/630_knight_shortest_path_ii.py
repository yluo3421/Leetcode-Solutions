from typing import (
    List,
)
DIRECTIONS = [(1, 2), (-1, 2), (2, 1) ,(-2, 1)]
class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    BFS
    """
    def shortest_path2(self, grid: List[List[bool]]) -> int:
        # write your code here
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        
        n = len(grid)
        m = len(grid[0])

        queue = collections.deque([(0, 0)])
        distance = {(0,0): 0}

        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                new_x = x + dx
                new_y = y + dy

                if not self.isvalid(new_x, new_y, distance, grid):
                    continue
                queue.append((new_x, new_y))
                distance[(new_x, new_y)] = distance[(x, y)] + 1
        
        if (n - 1, m - 1) in distance:
            return distance[(n - 1, m - 1)]
        return -1
    
    def isvalid(self, x, y, distance, grid):
        n = len(grid)
        m = len(grid[0])
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        if grid[x][y] == 1:
            return False
        if (x, y) in distance:
            return False
        return True
                