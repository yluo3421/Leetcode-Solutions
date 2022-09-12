class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # thoughts
        # iterate through the whole matrix
        # find connected 1s using dfs
        # O(mxn) Time | O(mxn) space
        # create a matrix called visited same size mxn
        # use a set to record visited
        # [1,1]
        # use the max_row and max_col to check if current cell is within matrix
        # everytime we found 1, and finsihed all connected 1s, island += 1
        numOfIslands = 0
        visited = set()
        max_row, max_col = len(grid), len(grid[0]) # 4, 5 in example 1
        
        def dfs(row, col):
            # check if current cell in the range
            if (
                row not in range(max_row)
                or col not in range(max_col)
                or grid[row][col] == "0"
                or (row, col) in visited
            ):  
                # add the current cell to visited set
                visited.add((row, col))
                return
            # add the current cell to visited set
            visited.add((row, col))
            
            # check all four neighbors
            directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
            #              up       left      right down
            # [delta_row, delta_col] 
            for delta_row, delta_col in directions:
                dfs(row + delta_row, col + delta_col)
            # cur  [0,2]
            # [0 + -1, 2 + 0] = [-1, 2]
            # dfs(-1,2)
            # [0 + 0, 2 + -1] = [0, 1]
            # dfs(0,1)
            # dfs(0,3)
            # cur = [0,3]
            # dfs(0,4) # 0
            # dfs(1,3) 1
            # all 3 other directions are 0
            # dfs(1,2) # 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    
                    dfs(r, c)
                    numOfIslands += 1
                # example 2
                # 0,0 0,1 0,2 1,1 1,0, 1,2 2,1 2,0
                #  1   1   0   1   1    0  0   0  
        return numOfIslands
            
    
            
        