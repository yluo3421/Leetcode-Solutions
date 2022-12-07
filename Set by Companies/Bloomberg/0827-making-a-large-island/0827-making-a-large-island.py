class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        Thoughts
        The brutal force method that comes to me
        Is that we can use a dfs every time we change a 0 to 1
        from that point we can check how large this island is
        And return the max island found
        I think the edge case is if there is no 0 in the grid
        The answer will be the size of the whole grid
        This method has a time complexity of O(n^4) SpaceO(n^2)
        """
#         n = len(grid)

#         def find_curr_island(r, c):
#             seen = {(r, c)}
#             stack = [(r, c)]
#             while stack:
#                 r, c = stack.pop()
#                 for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
#                     if (
#                         (nr, nc) not in seen 
#                         and 0 <= nr < n 
#                         and 0 <= nc < n 
#                         and grid[nr][nc]
#                     ):
#                         stack.append((nr, nc))
#                         seen.add((nr, nc))
#             return len(seen)
#         ans = 0
#         has_zero = False
#         for r, row in enumerate(grid):
#             for c, val in enumerate(row):
#                 if val == 0:
#                     has_zero = True
#                     grid[r][c] = 1
#                     ans = max(ans, find_curr_island(r, c))
#                     grid[r][c] = 0

#         return ans if has_zero else n*n
        """
        To make this time complexity better.
        One idea that I have right now is to see them as
        connected components.
        For example if the current 0 change to 1 will connect
        itself to a island next to it, we can store the
        islands size and use it right away.
        What we need to do is to find all islands first 
        we can do it in place: for each island we paint
        them with different color, so they got their own
        mark, it can be useing integer to represent color
        (we start enumerate from 2, 
        because 0 and 1 already reserved), 
        also we evaluate size of each island in island Counter. 
        Then we need to traverse our grid once again and 
        for each empty cell check four neighbors: and 
        create set off all unique islands (it can happen 
        that for example left neighbor and upper neighbor 
        are the same island). Then we evaluate sum of sizes 
        of all neighbours and choose the biggest one.
        """
        n = len(grid)
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        islands, paint_count, ans = Counter(), 2, 0

        def dfs(paint_count, i, j):
            if not 0 <= i < n or not 0 <= j < n or grid[i][j] != 1: return
            islands[paint_count] += 1
            grid[i][j] = paint_count
            for x, y in directions: 
                dfs(paint_count, x+i, y+j)

        for x, y in product(range(n), range(n)):
            if grid[x][y] == 1:
                dfs(paint_count, x, y)
                paint_count += 1

        for x, y in product(range(n), range(n)):
            if grid[x][y] != 0: continue
            neighbors = set()
            for dx, dy in directions:
                if 0 <= x + dx < n and 0 <= y + dy < n and grid[x+dx][y+dy] != 0:
                    neighbors.add(grid[x+dx][y+dy])
            ans = max(ans, sum(islands[i] for i in neighbors) + 1)

        return ans if ans != 0 else n*n
        
    