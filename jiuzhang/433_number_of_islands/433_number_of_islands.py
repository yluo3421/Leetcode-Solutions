from typing import (
    List,
)
from collections import deque
DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    BFS
    """
    def num_islands(self, grid: List[List[bool]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return 0
            
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
                    
        return islands                    
    
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]

# LeetCode 的用户请用下面的代码，因为 LeetCode 上的输入是 2D string array 而不是 boolean array
# from collections import deque

# class Solution:
#     """
#     @param grid: a boolean 2D matrix
#     @return: an integer
#     """
#     def numIslands(self, grid):
#         if not grid or not grid[0]:
#             return 0
        
#         islands = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     self.bfs(grid, i, j)
#                     islands += 1
                    
#         return islands                    
    
#     def bfs(self, grid, x, y):
#         queue = deque([(x, y)])
#         grid[x][y] = '0'
#         while queue:
#             x, y = queue.popleft()
#             for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
#                 next_x = x + delta_x
#                 next_y = y + delta_y
#                 if not self.is_valid(grid, next_x, next_y):
#                     continue
#                 queue.append((next_x, next_y))
#                 grid[next_x][next_y] = '0'
                
#     def is_valid(self, grid, x, y):
#         n, m = len(grid), len(grid[0])
#         return 0 <= x < n and 0 <= y < m and grid[x][y] == '1'