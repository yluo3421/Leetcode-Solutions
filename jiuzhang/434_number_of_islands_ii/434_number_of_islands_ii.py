from typing import (
    List,
)

from lintcode import (
    Point,
)

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def num_islands2(self, n: int, m: int, operators: List[Point]) -> List[int]:
        # write your code here
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        if not operators:
            return []
        
        uf = UnionFind()
        is_land = set()
        num_of_lands = []

        for operator in operators:
            if (operator.x, operator.y) in is_land:
                num_of_lands.append(uf.get_num_of_set())
                continue
            
            is_land.add((operator.x, operator.y))
            uf.add((operator.x, operator.y))
            for direction in DIRECTIONS:
                neighbor_x = operator.x + direction[0]
                neighbor_y = operator.y + direction[1]
                if self.is_valid(neighbor_x, neighbor_y, n, m, is_land):
                    uf.union((operator.x, operator.y), (neighbor_x, neighbor_y))
            num_of_lands.append(uf.get_num_of_set())
        return num_of_lands
    
    def is_valid(self, x, y, n, m, is_land):
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) not in is_land:
            return False
        return True
        
