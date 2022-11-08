from collections import deque
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # thoughts:
        # use bfs, starting from the start
        # choose one direction, and move until the wall or side of maze
        # append the curr location to the queue
        # check if the curr location is destination
        
        queue = deque(start)
        n = len(maze)
        m = len(maze[0])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while queue:
            i,j = queue.popleft()
            maze[i][j] = 2
            if i == destination[0] and j == destination[1]:
                return True
            
            for dx, dy in dirs:
                row = i + dx
                col = j + dy
                while row in range(n) and col in range(m) and maze[row][col] != 1:
                    row += dx
                    col += dy
                row -= dx
                col -= dy
                if maze[row][col] == 0:
                    queue.append([row, col])
        return False
        """
        dry run
        Input:
map = 
[
 [0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0,4]
end = [3,2]
Output:
false

        """
