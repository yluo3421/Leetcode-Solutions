class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs, found a 1, check its neighbor, mark all connected
        # 1s as visited. Continue checking untill all checked
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        
        # the function will be called when first 1 found
        # it is to put all connected 1s into visited
        def dfs(row, col):
            if (
                row not in range(ROW) 
                or col not in range(COL)
                or grid[row][col] == "0"
                or (row, col) in visited
            ):
                visited.add((row, col))
                return
            visited.add((row, col))
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        ans = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visited: 
                    dfs(r, c)
                    ans += 1
        return ans
    