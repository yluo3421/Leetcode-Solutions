class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # thoughts
        # find all elemetns that are able to flow to both Pacific and Atlantic
        # flow to Pacific means flow to first row or first col
        # florw to Atlantic means flwo to last row or last col
        
        # [2][2] height = 5
        # go to [1][2] height = 3, then [0][2] hegith = 2, proves this can get to Pac
        # go left can make to [2][0] which is Pacific as well
        # go right to [2][3] height = 3, then [2][4] height 1, this is Atlantic
        # go bottom can make to [3][2] height = 1, then [4][2] height = 1
        
        # to go thorugh all elements
        # Depth first search
        # for one single element, check one direction until no further elements can be checked or criteria made.
        # dfs(2,2,visited,height):
        #       dfs(left row, left col, visited, height[2][2])
        #       dfs right
        #       dfs top
        #       dfs bot
        # left row = 2, left element's col = 2 - 1 = 1
        # dfs(2,1,vistied, heighht[2][2])
        #      dfs left
        #       dfs right
        #       dfs top
        #       dfs bot
        
        # one way to check if we make to the other ocean is to see
        # if coordinates meet the four sides
        
        # started from the elements that are already in one ocean
        # dfs gives me all elements can flow from the current flow
        # We should check all four sides' elements
        
        max_row, max_col = len(heights), len(heights[0])
        arrive_pacific, arrive_atlantic = set(), set()
        
        def dfs(row, col, visited, prevHeight):
            # put element that can make to the ocean into their set
            if (
                row not in range(max_row)
                or col not in range(max_col)
                or (row, col) in visited
                or heights[row][col] < prevHeight
            ):
                return
            visited.add((row, col))
            # all four neighbors
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row + 1, col, visited, heights[row][col])
        # start from [0][0]
        # dfs(0,0,arrive_pacific, heights[0][0])
        # row = 0 col = 0 visited = arrive_pacific, prevHeight = heights[0][0]
        # row not in range(max_row)? No
        # col not in range(max_col)? No
        # (row, col) in visited ?    No
        # heights[row][col] < prevHeight No
        # dfs right
        # dfs(0, 1, arrive_pacific, heights[0][0])
        # row = 0, col = 1, visited = arrive_pacific, prevHeight = heights[0][0]
        # height[row][col] = heights[0][1] comapre to prevHeight = heights[0][0]
        #                           2           comapre         1
        #                           2        >       1
        # heights[row][col] < prevHeight No
        #   2                   1
        for col in range(max_col): #[0, 4]
            dfs(0, col, arrive_pacific, heights[0][col])
            dfs(max_row - 1, col, arrive_atlantic, heights[max_row - 1][col])
        
        for row in range(max_row):
            dfs(row, 0, arrive_pacific, heights[row][0])
            dfs(row, max_col - 1, arrive_atlantic, heights[row][max_col - 1])
            
        # the two set are updated with element can make to the ocean
        # check the intersetcion of the two sets will give us answers
        ans = []
        for row in range(max_row):
            for col in range(max_col):
                if (row, col) in arrive_pacific and (row, col) in arrive_atlantic:
                    ans.append([row, col])
        return ans
        
        # O(m*n) Time | O(m*n) Space