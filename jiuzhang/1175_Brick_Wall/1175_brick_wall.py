from typing import (
    List,
)

class Solution:
    """
    @param wall: a list of rows
    @return: the number of crossed bricks
    """
    def least_bricks(self, wall: List[List[int]]) -> int:
        # write your code here
        # we can use hashtable to record each level
        # each brik's right edge, by its ditance from brick's right to start of
        # the brick row.
        # except the rightmost one because
        # they dont want us to use the two side edge
        # then we will go through the hash table again to check 
        # the most frequent edge
        # that means along this edge if we draw a line, it touches most bricks'
        # edges
        # using total heights to minus the number if the answer

        n = len(wall)
        brick_edge = {}
        edge_freq = {}
        for i in range(n):
            brick_edge[i] = []
            distance = 0
            for j in range(len(wall[i]) - 1):
                distance += wall[i][j]
                brick_edge[i].append(distance)
                edge_freq[distance] = edge_freq.get(distance, 0) + 1
        max_freq = 0
        for key, value in edge_freq.items():
            max_freq = max(max_freq, value)
        return n - max_freq
            
