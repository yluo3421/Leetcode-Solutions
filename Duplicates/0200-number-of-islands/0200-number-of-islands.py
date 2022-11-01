class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs, found a 1, check its neighbor, mark all connected
        # 1s as visited. Continue checking untill all checked
        ROW, COL = len(grid), len(grid[0])
        ans = 0
        visited = set()
        
        def dfs(grid, visited, row, col):
            if (
                row not in range(ROW)
                or col not in range(COL)
                or (row, col) in visited
                or grid[row][col] == "0"
            ):
                visited.add((row, col))
                return
            visited.add((row, col))
            dfs(grid, visited, row + 1, col)
            dfs(grid, visited, row, col + 1)
            dfs(grid, visited, row - 1, col)
            dfs(grid, visited, row, col - 1)
            
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(grid, visited, i, j)
                    ans += 1
        return ans
                    
    