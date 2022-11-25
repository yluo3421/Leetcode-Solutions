from typing import (
    List,
)
DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberof_distinct_islands(self, grid: List[List[int]]) -> int:
        # write your code here
        # use bfs, found 1 island increse count by 1
        # find a way to record the shape of island
        # record it as path
        if not grid:
            return 0
        
        queue, check, ans = collections.deque(), set(), 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path = " "
                    queue.append((i, j))
                    grid[i][j] = 0
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in DIRECTIONS:
                            new_x, new_y = x+dx, y+dy
                            if self.is_valid(grid, new_x, new_y):
                                queue.append((new_x, new_y))
                                grid[new_x][new_y] = 0
                                path += str(new_x-i) + str(new_y-j)
                    if path not in check:
                        ans += 1
                        check.add(path)
        return ans
    
    def is_valid(self, grid, x, y):
        row, col = len(grid), len(grid[0])
        return x >= 0 and x < row and y >= 0 and y < col and grid[x][y] == 1