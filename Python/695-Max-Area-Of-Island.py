class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_row, max_col = len(grid), len(grid[0])
        # thoughts:
        # similar to find each island
        # but this time to record the area,
        # every time in dfs find a 1, meaning the area of the curr island
        # increased by 1
        #
        def dfs(row, col):
            if (
                row not in range(max_row)
                or col not in range(max_col)
                or grid[row][col] == 0
                or (row, col) in visited
            ):
                return 0
            visited.add((row, col))
            
            
            return 1 + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1) + dfs(row - 1, col)
        
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0 or (row, col) in visited:
                    continue
                
                maxArea = max(maxArea, dfs(row, col))
        return maxArea
        