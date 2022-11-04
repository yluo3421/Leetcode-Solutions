from typing import (
    List,
)
from xmlrpc.server import DocXMLRPCRequestHandler

class MazeGridType:
        SPACE = 0
        WALL = 1
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    
    一个矩阵中有一个球，一个洞
    矩阵每个格子是空地、洞、或者墙
    球每次可以朝着上下左右方向踢一脚知道碰到墙或者边界停下
    问球滚过的距离最短是多少以及踢球路径
    [4, 3]到[0, 1]

    [[0,0,0,0,0],
     [1,1,0,0,1],
     [0,0,0,0,0],
     [0,1,0,0,1],
     [0,1,0,0,0]
    ]
    输出(7,lul)
    在有相同长度路径的情况下，输出字符串最小的
    """
    DIRECTION_HASH = {
        "d": (1, 0),
        "l": (0, -1),
        "r": (0, 1),
        "u": (-1, 0),
        }
    
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> bool:
        # write your code here
        """
        how to solve every time the moving distance is not 1?
        Use SPFA
        How to record the shortest path
        We used to store distance in the hashmap
        now we store (distance, path)
        How to check where the ball stops?
        Use a function to return the direction chose and stop location

        """
        
        if not ball or not hole:
            return "impossible"
        if not maze or not maze[0]:
            return "impossible"
        
        hole = (hole[0], hole[1])

        {distance, x, y, path}
        queue = collections.deque([(ball[0], ball[1])])
        distance = {(ball[0], ball[1]): (0, "")}

        while queue:
            x, y = queue.popleft()
            dist, path = distance[(x, y)]

            for direction in Solution.DIRECTION_HASH:
                if path and path[-1] == direction:
                    continue

                new_x, new_y = self.kick_ball(x, y, direction, maze, hole)
                new_dist = dist + abs(new_x - x) + abs(new_y - y)
                new_path = path + direction
                if (new_x, new_y) in distance and distance[(new_x, new_y)] <= (new_dist, new_path):
                    continue
                    
                queue.append((new_x, new_y))
                distance[(new_x, new_y)] = (new_dist, new_path)
    
    def kick_ball(self, x, y, direction, maze, hole):
        dx, dy in Solution.DIRECTION_HASH[direction]
        while (x, y) != hole and not self.is_wall(x, y, maze):
            x += dx
            y += dy
        
        if (x, y) == hole:
            return (x, y)
        return x - dx, y - dy
 
    def is_wall(self, x, y, maze):
        if not (x in range(len(maze)) and y in range(len(maze[0]))):
            return True
        return maze[x][y] == MazeGridType.Wall